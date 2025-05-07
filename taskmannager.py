import tkinter as tk
from tkinter import messagebox
import json

# Load or initialize task list
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    """Save tasks to a file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a task to the list."""
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def update_list():
    """Update the task list display."""
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{i}. {task['task']} [{status}]")

def complete_task():
    """Mark task as completed."""
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["completed"] = True
        save_tasks()
        update_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete.")

def remove_task():
    """Remove a task from the list."""
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        save_tasks()
        update_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# GUI Setup
root = tk.Tk()
root.title("Task Manager")

# Entry Field
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.grid(row=1, column=1, padx=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=1, padx=10)

# Task List
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

update_list()

root.mainloop()
