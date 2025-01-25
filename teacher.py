class Teacher:
    teacher_list = []
    id_counter = 1
    def __init__(self, tId, fName, lName):
        self.tId = tId
        self.fName = fName
        self.lName = lName

    def addTeacher():
        teacherId = f"T{Teacher.id_counter:03}"
        Teacher.id_counter += 1
        while True:
            first_Name = input("Enter First Name: ")
            if not first_Name.isalpha():
                print("Wrong Name format")
                continue
            last_Name = input("Enter Last Name: ")
            if not last_Name.isalpha():
                print("Wrong Format")
                continue
            return Teacher(teacherId, first_Name, last_Name)

    def viewTeacher():
        if not Teacher.teacher_list:
            print("No Teacher Found")
            return
        for i,teacher in enumerate(Teacher.teacher_list, start=1):
            print(f"{i}. ID: {teacher.tId}, Name: {teacher.fName} {teacher.lName}")

    def updateTeacher():
        teacherId = input("Enter the Teacher Id: ")
        for teacher in Teacher.teacher_list:
            if teacher.tId == teacherId:
                print(f"The current name is {teacher.fName} {teacher.lName}")
                new_first_name = input("Enter the new first name(Leave Blank to Maintain Current Name): ")
                if new_first_name.strip():
                    if not new_first_name.isalpha():
                        print("Invalid format for First Name. Update aborted.")
                        return
                    teacher.fName = new_first_name
                new_last_name = input("Enter the new last name(Leave Blank to Maintain Current Name): ")
                if new_last_name.strip():
                    if not new_last_name.isalpha():
                        print("Invalid format for Last Name. Update aborted.")
                        return
                    teacher.lName = new_last_name 
                print("Teacher Record updated successfully")
        print("No record found") 

    def deleteTeacher():
        teacherId = input("Enter the student Id to delete: ")
        for teacher in Teacher.teacher_list:
            if teacher.tId == teacherId:
                print(f"Deleting Teacher {teacher.fName} {teacher.lName}")
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    Teacher.teacher_list.remove(teacher)
                    print("Deletion successful")
                    return
                else:
                    print("Deletion Cancelled")
                    return
        print("Teacher Not Found")


for st in range(3):
    Teacher.teacher_list.append(Teacher.addTeacher())
print("Before Deletion")
Teacher.viewTeacher()
Teacher.deleteTeacher()
print("After Deletion")
Teacher.viewTeacher()