# Task Manager System

A simple command-line (CLI) Task Manager written in Python. It stores tasks in a local JSON file and lets you add, view, update, complete, and delete tasks.

## Project Goal

Provide a lightweight command-line tool that lets a user add tasks, view them, update them, mark them as completed, and delete them, while persisting data between sessions without needing an external database.

## Features

- **Add a new task**: You enter only the task name and status (Pending / Completed). The ID is generated automatically by the program (last existing ID + 1) — you don't need to type it yourself.
- **View all tasks**: Lists every task with its ID, name, and status. Use this to find out a task's ID.
- **Update a task**: You enter the ID (from "View all tasks") to identify the task, then enter the new name and status.
- **Mark a task as completed**: You enter the task's ID and its status is set to "Completed" directly.
- **Delete a task**: You enter the ID of the task to remove.
- **Auto-save**: Every change is saved immediately to a local data file.
- **Interactive menu**: A simple text menu for navigating between options.

> **Quick summary**: You only need to type an ID for 3 operations — update, mark as completed, and delete — so the program knows exactly which task you mean. When adding a task, the ID is calculated automatically.

## Requirements

- Python 3.6 or later (no external libraries needed, only the built-in `json` and `os` modules).

## How to Run

```bash
python task_manager.py
```

After running, an interactive menu will appear:

```
Welcome to the Task Manager System
Please select an option:
1. Add a new task
2. View all tasks
3. update a task
4. Mark a task as completed
5. Delete a task
6. Exit
```

Enter the number of the option you want (1–6) and follow the on-screen instructions.

### Example: Adding a Task

```
Enter your choice (1-6): 1
Enter task name: Write project report
Enter task status (Pending/Completed): pending
Task ID 1 added.
```

## Data Storage

Tasks are saved in a file called `task_manager.py` (containing JSON text) in the project folder. The file is created automatically when the first task is added.

Example of the stored data format:

```json
[
    {
        "id": 1,
        "name": "Write project report",
        "status": "Pending"
    }
]
```

## Testing

The project currently has no automated (unit) tests. For manual testing:

1. Run the program with `python task_manager.py`.
2. Try every menu option (add, view, update, mark as completed, delete) and confirm the correct messages appear.
3. Check that `task_manager.py` is actually updated after each operation by opening it and inspecting its content.
4. To test error handling, try:
   - Entering a non-numeric ID when updating, deleting, or marking a task as completed.
   - Entering an invalid status (anything other than Pending or Completed).
   - Leaving the task name empty.

### Suggestion for Future Automated Testing

You could use `pytest` with a small refactor that separates the file read/write logic from the interactive `input()` calls (dependency injection). This would make it much easier to write unit tests for functions like `load_tasks` and `save_tasks` in isolation from user interaction.

## Project Structure

```
.
├── task_manager.py   # Main project code
├── tasks.py          # Task storage file (created automatically)
└── README.md         # This file
```

## Suggested Improvements

- Separate the input/output logic from the business logic to make testing easier.
- Add unit tests using `pytest`.
- Add support for sorting/filtering tasks by status.
