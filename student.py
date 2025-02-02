import csv

class Student:
    student_list = []
    id_counter = 1
    def __init__(self, stId, fName,lName):
        self.stId = stId
        self.fName = fName
        self.lName= lName

    def addStudent():
        studentId = f"S{Student.id_counter:03}"
        Student.id_counter += 1
        while True:
            firstName = input("Enter the First Name: ").strip()
            if not firstName.isalpha():
                print("First Name is in wrong format")
                continue
            lastName  = input("Enter Second Name: ").strip()
            if not lastName.isalpha():
                print("Last Name is in wrong format")
                continue
            for student in Student.student_list:
                if student.stId == studentId:
                    print(f"Error: Student ID {studentId} already exists.")
                    return
            return Student(studentId, firstName, lastName)
    def viewStudents():
        if not Student.student_list:
            print("No student found")
            return
        for i, student in enumerate(Student.student_list, start=1):
             print(f"{i}. ID: {student.stId}, Name: {student.fName} {student.lName}")

    def saveToCSV(file_name="students.csv"):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Id", "First Name", "Last Name"])
            for student in Student.student_list:
                writer.writerow([student.stId, student.fName, student.lName])
        print(f"student data saved to {file_name}.")

    def loadFromCSV(file_name="students.csv"):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    stId, fName, lName = row
                    Student.student_list.append(Student(stId, fName, lName))
                Student.id_counter = len(Student.student_list) + 1
            print(f"Student data loaded from {file_name}.")
        except FileNotFoundError:
            print (f"{file_name} not found.Starting with an empty list")


    def updateStudents():
        studentId = input("Enter the student Id to Update: ")
        for student in Student.student_list:
            if student.stId == studentId:
                print(f"Current Name: {student.fName} {student.lName}")
                new_first_name = input("Enter the New First Name(Leave Blank to Maintain Current Name): ")  
                if new_first_name.strip():
                    if not new_first_name.isalpha():
                        print("Invalid format for First Name. Update aborted.")
                        return
                    student.fName = new_first_name
                new_last_name = input("Enter the New Last Name(Leave Blank to Maintain Current Name): ")  
                if new_last_name.strip():
                    if not new_last_name.isalpha():
                        print("Invalid format for Last Name. Update aborted.")
                        return
                    student.lName = new_last_name
                print("Student Record updated successfully")
                return
        print("Student ID Not found.")

    def deleteStudent():
        studentId = input("Enter the student Id to delete: ")
        for student in Student.student_list:
            if student.stId == studentId:
                print(f"Deleting Name: {student.fName} {student.lName}?")
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    Student.student_list.remove(student)
                    print("Deletion successful")
                    return
                else:
                    print("Deletion Cancelled")
                    return
        print("Student Not Found")