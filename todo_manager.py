
"""Manage tasks, priorities, persistence, and JSON exports."""

import json
import os
import pickle
import random
from datetime import datetime

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




def saveTasks(fileName="tasks.pkl"):
    with open(fileName, "wb") as f:
        pickle.dump(tasks, f)


def loadTasks(fileName="tasks.pkl"):
    with open(fileName, "rb") as f:
        return pickle.load(f)


def exportJson(fileName="tasks.json"):
    with open(fileName, "w") as f:
        json.dump(tasks, f, indent=2)


def remindByEmail(address):
    # Helper kept for the lab: not called by the demo
    os.system("mail -s 'Pending tasks' " + address + " < tasks.json")


def main():
    addTask("Submit lab report", "high")
    addTask("Buy groceries")
    addTask("Call plumber", "low")
    addTask("Book train tickets", "high")
    completeTask(2)
    completeTask(99)
    print("Pending tasks:", pendingTasks())
    print("Task id for 'plumber':", findTask("plumber"))
    print("Task id for 'gym':", findTask("gym")) # returns None silently
    suggestion = random.choice(pendingTasks())
    print("Try this next:", suggestion)
    saveTasks()
    restored = loadTasks()
    print("Tasks restored from file:",len(restored))
    exportJson()
    print("Exported tasks to tasks.json")


main()
