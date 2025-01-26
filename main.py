from student import Student
from grading import Grading

def menu():
    grading = Grading()
    Student.loadFromCSV()
    grading.loadGradesFromCSV()

    while True:
        print("\nSchool Management System")
        print("\n 1. Manage Students")
        print("\n 2. Manage Subjects")
        print("\n 3.Manage Marks")
        print("\n 4.Save and Exit")

        choice = input("Enter your choice")

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_subjects(grading)
        elif choice == "3":
            manage_marks(grading)
        elif choice == "4":
            Student.saveToCSV()
            grading.saveGradesToCSV()
            print("Data Saved. Exiting the System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

def manage_students():
    while True:
        print("\Manage Students")
        print("\n 1.Add a Student")
        print("\n 2.View All Student")
        print("\n 3.Update a Student")
        print("\n 4.Delete a Student")
        print("\n 5. Go Back")

        choice = input("Enter your choice")

        if choice == "1":
            Student.student_list.append(Student.addStudent())
        elif choice == "2":
            Student.viewStudents()
        elif choice == "3":
            Student.updateStudents()
        elif choice == "4":
            Student.deleteStudent()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_subjects(grading):
    while True:
        print("/nManage Subjects")
        print("1. Add a Subject")
        print("2. Go Back")

        choice = input("Enter your choice")
        if choice == "1":
            subject_name = input("Enter the subject name: ")
            grading. addSubject(subject_name)
        elif choice == "2":
            break
        else:
             print("Invalid choice. Please try again.")

def manage_marks(grading):
    while True:
        print("/nManage Marks")
        print("1. Asign Marks")
        print("2. View Marks for a student")
        print("3. Calculate and view overall Grade for a student")
        print("4. Go Back")

        choice = input("Enter your choice")

        if choice == "1":
            student_id = input("Enter the student ID: ")
            subject_name = input("Enter the subject name: ")
            try:
                marks = int(input("Enter the marks: "))
                grading.assignMarks(student_id, subject_name, marks)
            except ValueError:
                print("Invalid marks. Please enter a number.")
        elif choice == "2":
            student_id = input("Enter the student ID: ")
            grading.viewMarks(student_id)
        elif choice == "3":
            student_id = input("Enter the student ID: ")
            grading.calculateOverallGrade(student_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

