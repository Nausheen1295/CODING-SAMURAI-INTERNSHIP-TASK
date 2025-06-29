import json
from datetime import datetime

# File to store tasks
FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display menu
def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Sort Tasks")
    print("7. Filter Tasks")
    print("8. Search Tasks")
    print("9. Exit")

# Display tasks with color-coded priorities
def display_tasks(tasks):
    print("\n📃 Your Tasks:")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
            priority_color = {
                "high": "\033[91m",  # Red
                "medium": "\033[93m",  # Yellow
                "low": "\033[92m",  # Green
            }.get(task['priority'], "\033[0m")  # Default color
            print(f"{i}. {status} {task['name']}{due_date} [{priority_color}{task['priority']}\033[0m]")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            new_task_name = input("Enter new task: ")
            if not new_task_name:
                print("⚠️ Task name cannot be empty.")
                continue
            priority = input("Enter priority (high, medium, low): ").lower()
            if priority not in ["high", "medium", "low"]:
                print("⚠️ Invalid priority. Please enter 'high', 'medium', or 'low'.")
                continue
            due_date_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = due_date_input if due_date_input else None
            
            # Validate due date format
            if due_date and not validate_date(due_date):
                print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
                continue
            
            new_task = {
                "name": new_task_name,
                "priority": priority,
                "due_date": due_date,
                "completed": False
            }
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added.")

        elif choice == "3":
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to edit: "))
                if 1 <= task_num <= len(tasks):
                    task = tasks[task_num - 1]
                    new_name = input(f"Current task name: {task['name']}. Enter new name (or leave blank to keep it): ")
                    if new_name:
                        task['name'] = new_name
                    new_priority = input(f"Current priority: {task['priority']}. Enter new priority (high, medium, low) (or leave blank to keep it): ").lower()
                    if new_priority in ["high", "medium", "low"]:
                        task['priority'] = new_priority
                    new_due_date = input(f"Current due date: {task['due_date']}. Enter new due date (YYYY-MM-DD) (or leave blank to keep it): ")
                    if new_due_date and not validate_date(new_due_date):
                        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
                        continue
                    if new_due_date:
                        task['due_date'] = new_due_date
                    save_tasks(tasks)
                    print("✅ Task updated.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"❌ Removed: {removed['name']}")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "5":
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    save_tasks(tasks)
                    print("✅ Task marked as completed.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "6":
            print("Sort by:")
            print("1. Priority")
            print("2. Due Date")
            sort_choice = input("Enter your choice (1-2): ")
            if sort_choice == "1":
                tasks.sort(key=lambda x: x['priority'])
                print("✅ Tasks sorted by priority.")
            elif sort_choice == "2":
                tasks.sort(key=lambda x: x['due_date'] if x['due_date'] else datetime.max)
                print("✅ Tasks sorted by due date.")
            else:
                print("⚠️ Invalid choice.")

        elif choice == "7":
            print("Filter by:")
            print("1. Completed Tasks")
            print("2. Incomplete Tasks")
            filter_choice = input("Enter your choice (1-2): ")
            if filter_choice == "1":
                filtered_tasks = [task for task in tasks if task['completed']]
                display_tasks(filtered_tasks)
            elif filter_choice == "2":
                filtered_tasks = [task for task in tasks if not task['completed']]
                display_tasks(filtered_tasks)
            else:
                print("⚠️ Invalid choice.")

        elif choice == "8":
            search_term = input("Enter search term: ").lower()
            found_tasks = [task for task in tasks if search_term in task['name'].lower()]
            if found_tasks:
                print("\n🔍 Search Results:")
                display_tasks(found_tasks)
            else:
                print("No tasks found matching that term.")

        elif choice == "9":
            print("👋 Exiting... Have a productive day!")
            break

        else:
            print("❗ Invalid choice. Please try again.")

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
