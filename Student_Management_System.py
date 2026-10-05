FILE_NAME = "students.txt"


# Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:

        file.write(roll + "," + name + "," + age + "," +
               department + "," + marks + "\n")

    #file.close()

    print("Student added successfully!")


# View All Students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
        #file.close()

        if len(students) == 0:
            print("No student records found.")
            return

        print("\n----- Student Records -----")

        for student in students:
            data = student.strip().split(",")

            print("Roll No    :", data[0])
            print("Name       :", data[1])
            print("Age        :", data[2])
            print("Department :", data[3])
            print("Marks      :", data[4])
            print("---------------------------")

    except FileNotFoundError:
        print("No student records found.")


# Search Student
def search_student():
    roll = input("Enter Roll No to search: ")

    try:
        file = open(FILE_NAME, "r")
        students = file.readlines()
        file.close()

        found = False

        for student in students:
            data = student.strip().split(",")

            if data[0] == roll:
                print("\nStudent Found!")
                print("Roll No    :", data[0])
                print("Name       :", data[1])
                print("Age        :", data[2])
                print("Department :", data[3])
                print("Marks      :", data[4])

                found = True
                break

        if found == False:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# Update Student
def update_student():
    roll = input("Enter Roll No to update: ")

    try:
        file = open(FILE_NAME, "r")
        students = file.readlines()
        file.close()

        found = False
        new_students = []

        for student in students:
            data = student.strip().split(",")

            if data[0] == roll:
                print("Enter new details:")

                name = input("Enter Name: ")
                age = input("Enter Age: ")
                department = input("Enter Department: ")
                marks = input("Enter Marks: ")

                new_student = roll + "," + name + "," + age + "," + \
                               department + "," + marks + "\n"

                new_students.append(new_student)

                found = True

            else:
                new_students.append(student)

        file = open(FILE_NAME, "w")
        file.writelines(new_students)
        file.close()

        if found:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# Delete Student
def delete_student():
    roll = input("Enter Roll No to delete: ")

    try:
        file = open(FILE_NAME, "r")
        students = file.readlines()
        file.close()

        found = False
        new_students = []

        for student in students:
            data = student.strip().split(",")

            if data[0] == roll:
                found = True
            else:
                new_students.append(student)

        file = open(FILE_NAME, "w")
        file.writelines(new_students)
        file.close()

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# Main Function
def main():
    while True:

        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")


# Program starts here
main()