print("=" * 35)
print("     STUDENT GRADE MANAGER")
print("=" * 35)

students = {}

while True:

    try:
        choice = int(input("""
1. View Students
2. Add Student
3. Update Grade
4. Delete Student
5. Calculate Average
6. Highest Grade
7. Lowest Grade
8. Exit

Choose an option: """))
    except ValueError:
        print("Please enter a number between 1 and 8.")
        continue

    # ================= VIEW =================

    if choice == 1:

        if not students:
            print("\nNo students found.\n")
        else:
            print("\nStudents")
            print("-" * 25)

            for i, (name, grade) in enumerate(students.items(), start=1):
                print(f"{i}. {name} : {grade}")

    # ================= ADD =================

    elif choice == 2:

        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exists.")
            continue

        try:
            grade = float(input("Enter grade (0-100): "))

            if 0 <= grade <= 100:
                students[name] = grade
                print("Student added successfully!")
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid grade.")

    # ================= UPDATE =================

    elif choice == 3:

        name = input("Enter student name: ").strip()

        if name not in students:
            print("Student not found.")
            continue

        try:
            grade = float(input("Enter new grade: "))

            if 0 <= grade <= 100:
                students[name] = grade
                print("Grade updated successfully!")
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid grade.")

    # ================= DELETE =================

    elif choice == 4:

        name = input("Enter student name: ").strip()

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # ================= AVERAGE =================

    elif choice == 5:

        if not students:
            print("No students found.")
        else:
            average = sum(students.values()) / len(students)
            print(f"Average Grade: {average:.2f}")

    # ================= HIGHEST =================

    elif choice == 6:

        if not students:
            print("No students found.")
        else:
            highest = max(students.values())

            print("\nHighest Grade")

            for name, grade in students.items():
                if grade == highest:
                    print(f"{name} : {grade}")

    # ================= LOWEST =================

    elif choice == 7:

        if not students:
            print("No students found.")
        else:
            lowest = min(students.values())

            print("\nLowest Grade")

            for name, grade in students.items():
                if grade == lowest:
                    print(f"{name} : {grade}")

    # ================= EXIT =================

    elif choice == 8:
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Please choose a number between 1 and 8.")