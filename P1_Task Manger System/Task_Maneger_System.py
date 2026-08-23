# Task Manager System

import json
import os


def load_tasks():
    if not os.path.exists("task_manager.py"):
        return []
    with open("task_manager.py", "r", encoding="UTF-8") as file:
        content = file.read()
        if not content.strip():
            return []
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print("Error: task_manager.py is not a valid JSON file. Starting with an empty task list.")
            return []

"_____________________________________________________________________"

def save_tasks(tasks):
    try:
        with open("task_manager.py", "w", encoding="UTF-8") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

"______________________________________________________________________"
# display menu
def display_menu():
    while True:
        print("Welcome to the Task Manager System")
        print("Please select an option:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. update a task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting the Task Manager System. Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

"______________________________________________________________________"

def task_status():

    while True:
        status = input("Enter task status (Pending/Completed): ").strip().lower()
        if status == "completed":
            return "Completed"
        elif status == "pending":
            return "Pending"
        else:
            print("Invalid status. Please enter 'Pending' or 'Completed'.")

"______________________________________________________________________"            

def tasks_name(): 
    while True:
        task_name = input("Enter task name: ").strip()
        if task_name:
            return task_name
        else:
            print("Task name cannot be empty. Please enter a valid task name.")

"______________________________________________________________________"

# Add a new task
def add_task():
    
    task_id=max([task["id"] for task in load_tasks()], default=0) + 1

    task_name = tasks_name()
    status = task_status()
    tasks = load_tasks()
    tasks.append({"id": task_id, "name": task_name, "status": status})
    save_tasks(tasks)
    print(f"Task ID {task_id} added.")

"______________________________________________________________________"

# view all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("All Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")

"______________________________________________________________________"

# update a task
def update_task():
    try:
        task_id = int(input("Enter the task ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a valid task ID.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            new_name = tasks_name()
            new_status = task_status()
            task["name"] = new_name
            task["status"] = new_status
            save_tasks(tasks)
            print(f"Task ID {task_id} updated.")
            return
    print(f"Task ID {task_id} not found.")

"______________________________________________________________________"

# mark a task as completed
def mark_task_completed():
    try:
        task_id = int(input("Enter the task ID to mark as completed: "))
    except ValueError:
        print("Invalid ID. Please enter a valid task ID.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print(f"Task ID {task_id} marked as completed.")
            return
    print(f"Task ID {task_id} not found.")

"______________________________________________________________________"

# delete a task
def delete_task():
    try:
        task_id = int(input("Enter the task ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a valid task ID.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.pop(tasks.index(task))
            save_tasks(tasks)
            print(f"Task ID {task_id} deleted.")
            return
    print(f"Task ID {task_id} not found.")

"______________________________________________________________________"

if __name__ == "__main__":
    display_menu()
