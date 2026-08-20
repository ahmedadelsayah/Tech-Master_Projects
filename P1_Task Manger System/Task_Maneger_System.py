# Task Manager System

import json
import os


def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r", encoding="UTF-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []



def save_tasks(tasks):
    with open("tasks.json", "w", encoding="UTF-8") as file:
        json.dump(tasks, file, indent=4)


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


# Add a new task
def add_task():
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID. Please enter a valid task ID.")
        return

    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    task_status = input("Enter task status (Pending/Completed): ")
    tasks = load_tasks()
    tasks.append({"id": task_id, "name": task_name, "status": task_status})
    save_tasks(tasks)
    print(f"Task ID {task_id} added.")


# view all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("All Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")


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
            new_name = input("Enter the new task name: ")
            new_status = input("Enter the new task status (Pending/Completed): ")
            task["name"] = new_name
            task["status"] = new_status
            save_tasks(tasks)
            print(f"Task ID {task_id} updated.")
            return
    print(f"Task ID {task_id} not found.")


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
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task ID {task_id} deleted.")
            return
    print(f"Task ID {task_id} not found.")


if __name__ == "__main__":
    display_menu()
