from student import Student
from grading import Grading

def menu():
    try:
        grading = Grading()
        Student.loadFromCSV()
        grading.loadGradesFromCSV()
        grading.loadSubjectsFromCSV()  

        while True:
            print("\nSchool Management System")
            print("\n 1. Manage Students")
            print("\n 2. Manage Subjects")
            print("\n 3.Manage Marks")
            print("\n 4.Generate Reports")
            print("\n 5.Save and Exit")

            choice = input("Enter your choice")

            if choice == "1":
                manage_students()
            elif choice == "2":
                manage_subjects(grading)
            elif choice == "3":
                manage_marks(grading)
            elif choice == "4":
                manage_reports(grading)
            elif choice == "5":
                Student.saveToCSV()
                grading.saveGradesToCSV()
                grading.saveSubjectsToCSV()
                print("Data Saved. Exiting the System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again")
    except Exception as e:
        print(f"Unexpected Error: {e}")

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
        print("\nManage Subjects")
        print("1. Add a Subject")
        print("2. View Available Subjects")
        print("3. Delete a Subject")
        print("4. Go Back")

        choice = input("Enter your choice")
        if choice == "1":
            subject_name = input("Enter the subject name: ")
            grading. addSubject(subject_name)
        elif choice == "2":
            Grading.viewSubjects()
        elif choice == "3":       
            subject_name = input("Enter the subject name to delete: ")
            Grading.deleteSubject(subject_name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_marks(grading):
    while True:
        print("\nManage Marks")
        print("1. Asign Marks")
        print("2. View Marks for a student")
        print("3. Calculate and view overall Grade for a student")
        print("4. Calculate Subject Average")
        print("5. View Class Topper")
        print("6. View Highest Scorer in a Subject")
        print("7. Go Back")

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
            subject_name = input("Enter the subject name: ")
            grading.calculateSubjectAverage(subject_name)
        elif choice =="5":
            grading.getClassTopper()
        elif choice == "6":
            subject_name = input("Enter the subject name: ")
            grading.getHighestScorerInSubject(subject_name)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_reports(grading):
    while True:
        print("\nGenerate Reports")
        print("1. Generate Student Report")
        print("2. Export Student Report to CSV")
        print("3. Generate Class Report")
        print("4. Export Class Report to CSV")
        print("5. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter the student ID: ")
            grading.generateStudentReport(student_id)
        elif choice == "2":
            student_id = input("Enter the student ID: ")
            grading.exportStudentReportToCSV(student_id)
        elif choice == "3":
            grading.generateClassReport()
        elif choice == "4":
            grading.exportClassReportToCSV()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

