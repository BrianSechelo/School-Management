import csv
from student import Student

class Subject:
    def __init__(self, name):
        self.name = name

class Grading:
    def __init__(self):
        self.student_subjects = {}

    def addSubject(self, subject_name):
        print(f"Adding subject: {subject_name}")
        subject = Subject(subject_name)
        for student in Student.student_list:
            if student.stId not in self.student_subjects:
                self.student_subjects[student.stId] = {}
            self.student_subjects[student.stId][subject_name] = 0

    def assignMarks(self, student_id, subject_name, marks):
        if student_id in self.student_subjects and subject_name in self.student_subjects[student_id]:
            self.student_subjects[student_id][subject_name] = marks
            print(f"Assigned {marks} marks to {subject_name} for students {student_id}")
        
        else:
             print(f"Invalid student ID or subject name.")

    def viewMarks(self, student_id):
        """View all marks for a specific student."""
        if student_id in self.student_subjects:
            print(f"Marks for student {student_id}:")
            for subject, marks in self.student_subjects[student_id].items():
                print(f"  {subject}: {marks}")

        else:
            print(f"Student ID {student_id} not found.")

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
        TotMarks = 0  # Initialize total marks
        count = 0  # Initialize count of subjects
        if student_id in self.student_subjects:
            for subject, marks in self.student_subjects[student_id].items():
                TotMarks += marks  # Accumulate marks
                count += 1  # Increment count of subjects

        # Calculate average marks
            if count > 0:
                AverageM = TotMarks / count
                print(f"Average Marks for student {student_id}: {AverageM:.2f}")
            else:
                print(f"No marks available for student {student_id}.")
        else:
            print(f"Student ID {student_id} not found.")

from student import Student
from grading import Grading

# Initialize grading system
grading = Grading()

# Load data from files
Student.loadFromCSV()
grading.loadGradesFromCSV()

# Add a new student
Student.student_list.append(Student.addStudent())

# Add subjects and assign marks
grading.addSubject("Math")
grading.addSubject("Science")
grading.assignMarks("S001", "Math", 85)
grading.assignMarks("S001", "Science", 90)

# View all students and their marks
print("\nStudent List:")
Student.viewStudents()

print("\nMarks for S001:")
grading.viewMarks("S001")

# Save updated data
Student.saveToCSV()
grading.saveGradesToCSV()