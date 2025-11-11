students = []

def add_student(name):
    students.append(name)
    print(name, "added")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(name, "removed")
    else:
        print("Student not found")

def show_students():
    if not students:
        print("No students in the list")
    else:
        print("Student list:")
        for s in students:
            print("-", s)

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Show students")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        add_student(name)
    elif choice == "2":
        name = input("Enter name: ")
        remove_student(name)
    elif choice == "3":
        show_students()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
