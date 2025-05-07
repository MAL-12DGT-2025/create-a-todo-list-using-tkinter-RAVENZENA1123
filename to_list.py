import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")

tasks = []

# Function to update the task list
def update_listbox():
    listbox.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        listbox.insert(tk.END, task)  # Insert tasks

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)  # Clear entry field
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a selected task
def remove_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        tasks.remove(selected_task)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Creating UI Elements
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Start the application
root.mainloop()
