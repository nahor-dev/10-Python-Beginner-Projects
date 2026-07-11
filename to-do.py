print("======================")
print("     TO-DO LIST")
print("======================")

tasks = []

while True:

    try:
        choice = int(input("""
1. View Tasks
2. Add Task
3. Edit Task
4. Delete Task
5. Exit

Choose an option: """))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Thank you for using the To-Do List!")
        break

    elif choice == 1:
        print("\n======================")
        print("Your Tasks")
        print("======================")

        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == 2:
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 3:

        if not tasks:
            print("No tasks to edit.")
            continue

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        try:
            edit = int(input("Enter the task number to edit: "))

            if 1 <= edit <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[edit - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == 4:

        if not tasks:
            print("No tasks to delete.")
            continue

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        try:
            delete = int(input("Enter the task number to delete: "))

            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete - 1)
                print(f'"{removed}" deleted successfully!')
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Please choose a number between 1 and 5.")