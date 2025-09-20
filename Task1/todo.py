# To-Do List Application (Command Line Version)

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task['completed'] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully!")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            print("1. Mark as Complete\n2. Edit Task Name")
            choice = input("Enter choice: ")
            if choice == "1":
                tasks[task_no - 1]['completed'] = True
                print("Task marked as complete.")
            elif choice == "2":
                new_title = input("Enter new task name: ")
                tasks[task_no - 1]['title'] = new_title
                print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted_task = tasks.pop(task_no - 1)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Have a productive day! ✅")
        break
    else:
        print("Invalid choice! Please try again.")