import csv
from student import Student

class Subject:
    def __init__(self, name):
        self.name = name

class Grading:
    subject_list = []
    def __init__(self):
        self.student_subjects = {}

    @staticmethod
    def addSubject(subject_name):
        if subject_name in Grading.subject_list:
            print(f"{subject_name} already exists.")
            return
        Grading.subject_list.append(subject_name)
        print(f"Subject '{subject_name}' added successfully.")

    def deleteSubject(subject_name):
        for student_id, subjects in Grading.student_subjects.items():
            if subject_name in subjects:
                print(f"Cannot delete '{subject_name}'. Marks have been assigned.")
                return
            if subject_name in Grading.subject_list:
                Grading.subject_list.remove(subject_name)
                print(f"Subject '{subject_name}' deleted successfully.")
            else:
                print(f"Subject '{subject_name}' not found.")
        
    def assignMarks(self, student_id, subject_name, marks):
        if student_id not in [student.stId for student in Student.student_list]:
            print(f"Error: Student ID '{student_id}' does not exist.")
            return
        if subject_name not in Grading.subject_list:
            print(f"Error: Subject '{subject_name}' does not exist. Add it first.")
            return
        try:
            marks = int(marks)
            if marks < 0:
                print("Error: Marks cannot be negative.")
                return
        except ValueError:
            print("Error: Marks must be a valid number.")
            return
        if student_id not in self.student_subjects:
            self.student_subjects[student_id] = {}
        self.student_subjects[student_id][subject_name] = marks
        print(f"Assigned {marks} marks to {subject_name} for student {student_id}.")

    @staticmethod
    def viewSubjects():
        if not Grading.subject_list:
            print("No subjects available.")
            return
        print("\nAvailable Subjects:")
        for index, subject in enumerate(Grading.subject_list, start=1):
            print(f"{index}. {subject}")

    def calculateSubjectAverage(self, subject_name):
        total_marks = 0
        student_count = 0
        for student_id, subjects in self.student_subjects.items():
            if subject_name in subjects:
                total_marks += subjects[subject_name]
                student_count = 1
        if student_count == 0:
            print(f"No marks recorded for subject: {subject_name}.")
            return
        average_marks = total_marks / student_count
        print(f"Subject: {subject_name}, Average Marks: {average_marks:.2f}")

    def getClassTopper(self):
        highest_avg = 0
        topper = None
        for student_id in self.student_subjects:
            total_marks = sum(self.student_subjects[student_id].values())
            subject_count = len(self.student_subjects[student_id])
            if subject_count > 0:
                 average_marks = total_marks / subject_count
                 if average_marks > highest_avg:
                    highest_avg = average_marks
                    topper = student_id
        if topper:
            print(f"Class Topper: Student {topper} with an average of {highest_avg:.2f}")
        else:
            print("No students have been graded yet.")

    def getHighestScorerInSubject(self, subject_name):
        highest_marks = -1
        top_student = None
        for student_id, subjects in self.student_subjects.items():
            if subject_name in subjects and subjects[subject_name] > highest_marks:
                highest_marks = subjects[subject_name]
                top_student = student_id
        if top_student:
            print(f"Highest Scorer in {subject_name}: Student {top_student} with {highest_marks} marks.")
        else:
            print(f"No marks recorded for {subject_name}.")

    def saveSubjectsToCSV(self, file_name="subjects.csv"):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Subjects"])
            for subject in Grading.subject_list:
                writer.writerow([subject])
        print(f"Subject data saved to {file_name}.")

    def loadSubjectsFromCSV(self,file_name="subjects.csv"):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        Grading.subject_list.append(row[0])
            print(f"Subjects loaded from {file_name}.")
        except FileNotFoundError:
            print(f"{file_name} not found. Starting with an empty subject list.")
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
            
    def saveGradesToCSV(self, file_name="grades.csv"):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Id", "Subject", "Marks"])
            for student_id, subjects in self.student_subjects.items():
                for subject, marks in subjects.items():
                    writer.writerow([student_id, subject, marks])
        print(f"student grades data saved to {file_name}.")

    def loadGradesFromCSV(self, file_name="grades.csv"):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    student_id, subject, marks = row
                    marks = int(marks)
                    if student_id not in self.student_subjects:
                        self.student_subjects[student_id] = {}
                        self.student_subjects[student_id][subject] = marks
            print(f"Grading data loaded from {file_name}.")
        except FileNotFoundError:
            print (f"{file_name} not found. Starting with an empty grading system")

    def calculateOverallGrade(self, student_id):
        if student_id not in self.student_subjects:
            print(f"Error: Student ID '{student_id}' not found.")
            return

        total_marks = sum(self.student_subjects[student_id].values())
        subject_count = len(self.student_subjects[student_id])

        if subject_count == 0:
            print(f"Error: No marks available for student {student_id}.")
            return
        average_marks = total_marks / subject_count
        print(f"Average Marks for student {student_id}: {average_marks:.2f}")

    def generateStudentReport(self, student_id):
        if student_id not in self.student_subjects:
            print(f"Error: Student ID '{student_id}' not found.")
            return

        student = next((s for s in Student.student_list if s.stId == student_id), None)
        if not student:
            print(f"Error: Student ID '{student_id}' not found in student list.")
            return

        print("\n--- Student Report ---")
        print(f"Student ID: {student_id}")
        print(f"Name: {student.fName} {student.lName}")

        total_marks = sum(self.student_subjects[student_id].values())
        subject_count = len(self.student_subjects[student_id])
        overall_grade = total_marks / subject_count if subject_count > 0 else 0

        print("\nSubjects and Marks:")
        for subject, marks in self.student_subjects[student_id].items():
             print(f"  {subject}: {marks}")

        print(f"\nOverall Grade: {overall_grade:.2f}")

    def exportStudentReportToCSV(self, student_id, file_name="student_report.csv"):
        if student_id not in self.student_subjects:
            print(f"Error: Student ID '{student_id}' not found.")
            return

        student = next((s for s in Student.student_list if s.stId == student_id), None)
        if not student:
            print(f"Error: Student ID '{student_id}' not found in student list.")
            return

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Id", "Name", "Subject", "Marks"])

            for subject, marks in self.student_subjects[student_id].items():
                writer.writerow([student_id, f"{student.fName} {student.lName}", subject, marks])

            total_marks = sum(self.student_subjects[student_id].values())
            subject_count = len(self.student_subjects[student_id])
            overall_grade = total_marks / subject_count if subject_count > 0 else 0

            writer.writerow(["", "", "Overall Grade", overall_grade])

        print(f"Student report exported to {file_name}.")

    def generateClassReport(self):
        print("\n--- Class Report ---")
        print(f"{'Student ID':<10}{'Name':<20}{'Overall Grade':<15}")

        class_report = []
        for student in Student.student_list:
            student_id = student.stId
            if student_id in self.student_subjects:
                total_marks = sum(self.student_subjects[student_id].values())
                subject_count = len(self.student_subjects[student_id])
                overall_grade = total_marks / subject_count if subject_count > 0 else 0
            else:
                overall_grade = 0

            class_report.append([student_id, f"{student.fName} {student.lName}", overall_grade])
            print(f"{student_id:<10}{student.fName + ' ' + student.lName:<20}{overall_grade:.2f}")

    def exportClassReportToCSV(self, file_name="class_report.csv"):
        """Export a class report to a CSV file."""
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Overall Grade"])

            for student in Student.student_list:
                student_id = student.stId
                if student_id in self.student_subjects:
                    total_marks = sum(self.student_subjects[student_id].values())
                    subject_count = len(self.student_subjects[student_id])
                    overall_grade = total_marks / subject_count if subject_count > 0 else 0
                else:
                    overall_grade = 0

                writer.writerow([student_id, f"{student.fName} {student.lName}", overall_grade])

        print(f"Class report exported to {file_name}.")
