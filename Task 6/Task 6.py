import json

TASK_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def generate_task_id(tasks):
    if tasks:
        return max(task['id'] for task in tasks) + 1
    else:
        return 1

def add_task(tasks):
    description = input("Enter the task description: ")
    task = {
        'id': generate_task_id(tasks),
        'description': description,
        'status': 'pending'
    }
    tasks.append(task)
    print(f"Task added with ID: {task['id']}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def remove_task(tasks):
    task_id = int(input("Enter the task ID to remove: "))
    task_to_remove = next((task for task in tasks if task['id'] == task_id), None)
    
    if task_to_remove:
        tasks.remove(task_to_remove)
        print(f"Task with ID {task_id} removed.")
    else:
        print(f"No task found with ID {task_id}.")

def mark_completed(tasks):
    task_id = int(input("Enter the task ID to mark as completed: "))
    task_to_complete = next((task for task in tasks if task['id'] == task_id), None)
    
    if task_to_complete:
        task_to_complete['status'] = 'completed'
        print(f"Task with ID {task_id} marked as completed.")
    else:
        print(f"No task found with ID {task_id}.")

def edit_task(tasks):
    task_id = int(input("Enter the task ID to edit: "))
    task_to_edit = next((task for task in tasks if task['id'] == task_id), None)
    
    if task_to_edit:
        new_description = input("Enter the new description: ")
        task_to_edit['description'] = new_description
        print(f"Task with ID {task_id} updated.")
    else:
        print(f"No task found with ID {task_id}.")

def search_task(tasks):
    keyword = input("Enter the keyword to search: ").lower()
    results = [task for task in tasks if keyword in task['description'].lower()]
    
    if results:
        for task in results:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found with the given keyword.")

def filter_tasks(tasks):
    status = input("Enter the status to filter by (pending/completed): ").lower()
    filtered_tasks = [task for task in tasks if task['status'] == status]
    
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print(f"No {status} tasks found.")

def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
    if confirm == 'yes':
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Operation canceled.")

def sort_tasks(tasks):
    sort_by = input("Sort by 'id' or 'status': ").lower()
    
    if sort_by == 'id':
        tasks.sort(key=lambda task: task['id'])
        print("Tasks sorted by ID.")
    elif sort_by == 'status':
        tasks.sort(key=lambda task: task['status'])
        print("Tasks sorted by status.")
    else:
        print("Invalid sorting option.")

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark as Completed")
    print("5. Edit Task")
    print("6. Search Task")
    print("7. Filter Tasks")
    print("8. Clear All Tasks")
    print("9. Sort Tasks")
    print("0. Exit")

def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            search_task(tasks)
        elif choice == '7':
            filter_tasks(tasks)
        elif choice == '8':
            clear_all_tasks(tasks)
        elif choice == '9':
            sort_tasks(tasks)
        elif choice == '0':
            save_tasks(tasks)
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()