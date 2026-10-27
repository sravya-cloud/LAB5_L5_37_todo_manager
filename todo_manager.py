
"""Manage tasks, priorities, persistence, and JSON exports."""

import json
import secrets
import smtplib
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from re import fullmatch

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a task and return its unique ID."""
    if priority not in PRIORITY_ORDER:
        raise ValueError("Priority must be high, medium, or low.")

    task_id = max(tasks, default=0) + 1
    task_labels = list(labels) if labels is not None else []
    task_labels.append(priority)

    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "labels": task_labels,
        "done": False,
        "created": datetime.now().isoformat(),
    }
    return task_id


def complete_task(task_id):
    """Mark a task as complete and report whether it exists."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True

    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return pending task titles ordered by priority."""
    pending = [
        task for task in tasks.values() if not task["done"]
    ]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword):
    """Return the ID of the first matching task, or None."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks.json"):
    """Save tasks to a JSON file."""
    with Path(file_name).open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(file_name="tasks.json"):
    """Load tasks from JSON and restore integer task IDs."""
    with Path(file_name).open("r", encoding="utf-8") as file:
        loaded_tasks = json.load(file)
    return {int(task_id): task for task_id, task in loaded_tasks.items()}


def export_json(file_name="tasks.json"):
    """Export the current tasks to a JSON file."""
    with Path(file_name).open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def remind_by_email(address):
    """Email the pending-task list through a configured SMTP server."""
    if not fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", address):
        raise ValueError("Please provide a valid email address.")

    message = EmailMessage()
    message["Subject"] = "Pending tasks"
    message["From"] = "todo-manager@localhost"
    message["To"] = address
    message.set_content("\n".join(pending_tasks()) or "No pending tasks.")

    with smtplib.SMTP("localhost") as server:
        server.send_message(message)


def main():
    """Run a demonstration of the Todo Manager."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")

    complete_task(2)
    complete_task(99)

    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))

    pending = pending_tasks()
    if pending:
        suggestion = secrets.choice(pending)
        print("Try this next:", suggestion)
    else:
        print("No pending tasks to suggest.")

    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
