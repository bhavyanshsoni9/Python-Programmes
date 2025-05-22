import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from plyer import notification
import json
import os
import threading
import time
from datetime import datetime

FILENAME = "tasks.json"

PRIORITY_LEVELS = {"High": 1, "Medium": 2, "Low": 3}  # For sorting

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def notify(task):
    notification.notify(
        title="🔔 Task Reminder",
        message=f"{task['task']} (Priority: {task['priority']}) at {task['time']}",
        timeout=10
    )

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 To-Do List with Reminder & Priority")
        self.root.geometry("450x550")

        self.tasks = load_tasks()

        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.entry_task = PlaceholderEntry(root, placeholder="Enter Task", font=("Arial", 12))
        self.entry_task.pack(pady=5)

        self.entry_time = PlaceholderEntry(root, placeholder="HH:MM (24-hour)", font=("Arial", 12))
        self.entry_time.pack(pady=5)

        # Priority dropdown
        priority_frame = tk.Frame(root)
        priority_frame.pack(pady=5)
        tk.Label(priority_frame, text="Priority:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.priority_var = tk.StringVar()
        self.priority_combo = ttk.Combobox(priority_frame, textvariable=self.priority_var, state="readonly", 
                                           values=["High", "Medium", "Low"], font=("Arial", 12), width=10)
        self.priority_combo.current(1)  # Default to Medium
        self.priority_combo.pack(side=tk.LEFT, padx=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Task ➕", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Task ✨", command=self.update_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Remove Task ➖", command=self.remove_task).grid(row=0, column=2, padx=5)
        tk.Button(root, text="Exit 🚪", command=root.quit).pack(pady=10)

        self.load_listbox()

        self.running = True
        threading.Thread(target=self.reminder_loop, daemon=True).start()

    def load_listbox(self):
        self.task_listbox.delete(0, tk.END)
        # Ensure each task has priority, if missing set Medium by default
        for task in self.tasks:
            if "priority" not in task:
                task["priority"] = "Medium"
        # Sort tasks by priority level
        sorted_tasks = sorted(self.tasks, key=lambda x: PRIORITY_LEVELS.get(x.get("priority", "Medium"), 2))
        self.tasks = sorted_tasks  # update task order
        for t in sorted_tasks:
            self.task_listbox.insert(tk.END, f"{t['task']}  ⏰ {t['time']}  🔥 {t['priority']}")
        # Save updated tasks with priority added
        save_tasks(self.tasks)



    def add_task(self):
        task_name = self.entry_task.get().strip()
        time_str = self.entry_time.get().strip()
        priority = self.priority_var.get()

        if task_name == "" or task_name == "Enter Task":
            messagebox.showwarning("Warning", "Please enter a task name.")
            return
        if time_str == "" or time_str == "HH:MM (24-hour)" or not self.validate_time(time_str):
            messagebox.showwarning("Warning", "Enter time in HH:MM 24-hour format.")
            return
        if priority not in PRIORITY_LEVELS:
            messagebox.showwarning("Warning", "Select a valid priority.")
            return

        self.tasks.append({"task": task_name, "time": time_str, "priority": priority, "notified": False})
        save_tasks(self.tasks)
        self.load_listbox()
        self.entry_task.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_task.put_placeholder()
        self.entry_time.put_placeholder()
        self.priority_combo.current(1)  # Reset to Medium
        messagebox.showinfo("Success", "Task added!")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to update.")
            return
        index = selected[0]

        task_name = simpledialog.askstring("Update Task", "Enter new task name:", initialvalue=self.tasks[index]['task'])
        if task_name is None or task_name.strip() == "":
            return

        time_str = simpledialog.askstring("Update Time", "Enter new time (HH:MM 24-hour):", initialvalue=self.tasks[index]['time'])
        if time_str is None or not self.validate_time(time_str):
            messagebox.showwarning("Warning", "Invalid time format.")
            return

        priority = simpledialog.askstring("Update Priority", "Enter priority (High, Medium, Low):", initialvalue=self.tasks[index]['priority'])
        if priority is None or priority not in PRIORITY_LEVELS:
            messagebox.showwarning("Warning", "Invalid priority.")
            return

        self.tasks[index] = {"task": task_name.strip(), "time": time_str, "priority": priority, "notified": False}
        save_tasks(self.tasks)
        self.load_listbox()
        messagebox.showinfo("Success", "Task updated!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to remove.")
            return
        index = selected[0]
        task = self.tasks.pop(index)
        save_tasks(self.tasks)
        self.load_listbox()
        messagebox.showinfo("Removed", f"Task '{task['task']}' removed!")

    def validate_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except:
            return False

    def reminder_loop(self):
        while self.running:
            now = datetime.now().strftime("%H:%M")
            changed = False
            for task in self.tasks:
                if task["time"] == now and not task.get("notified", False):
                    notify(task)
                    task["notified"] = True
                    changed = True
            if changed:
                save_tasks(self.tasks)
            time.sleep(60)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.stop)
    root.mainloop()
