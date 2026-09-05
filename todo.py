tasks = []


def add_task():
    task = input("Enter a task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== Your To-Do List =====")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== To-Do List App =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice. Please try again.")


main()