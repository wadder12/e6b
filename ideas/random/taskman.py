import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.configure(bg="white")  # Set background color

        self.task_manager = TaskManager()

        self.create_widgets()

    def create_widgets(self):
        self.tasks_frame = tk.Frame(self, bg="white")
        self.tasks_frame.pack(pady=10)

        self.tasks_listbox = tk.Listbox(self.tasks_frame, width=50, bg="lightgray", selectbackground="lightblue")
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        self.tasks_listbox.bind("<<ListboxSelect>>", self.select_task)

        self.task_details_frame = tk.Frame(self, bg="white")
        self.task_details_frame.pack(pady=10)

        self.task_name_label = tk.Label(self.task_details_frame, text="Task Name:", bg="white")
        self.task_name_label.grid(row=0, column=0, sticky=tk.W)

        self.task_name_entry = tk.Entry(self.task_details_frame)
        self.task_name_entry.grid(row=0, column=1)

        self.task_desc_label = tk.Label(self.task_details_frame, text="Description:", bg="white")
        self.task_desc_label.grid(row=1, column=0, sticky=tk.W)

        self.task_desc_entry = tk.Entry(self.task_details_frame)
        self.task_desc_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task, bg="lightgreen", fg="white")
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self, text="Mark as Completed", command=self.complete_task, bg="orange", fg="white")
        self.complete_button.pack(pady=5)

        self.list_button = tk.Button(self, text="List Tasks", command=self.list_tasks, bg="blue", fg="white")
        self.list_button.pack(pady=5)

    def select_task(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            task = self.task_manager.get_task(index)
            self.task_name_entry.delete(0, tk.END)
            self.task_name_entry.insert(tk.END, task.name)
            self.task_desc_entry.delete(0, tk.END)
            self.task_desc_entry.insert(tk.END, task.description)

    def add_task(self):
        name = self.task_name_entry.get()
        description = self.task_desc_entry.get()
        if name and description:
            self.task_manager.add_task(name, description)
            self.tasks_listbox.insert(tk.END, name)
            messagebox.showinfo("Success", f"Task '{name}' added successfully.")
        else:
            messagebox.showerror("Error", "Please enter both task name and description.")

    def complete_task(self):
        selection = self.tasks_listbox.curselection()
        if selection:
            index = selection[0]
            task = self.task_manager.get_task(index)
            self.task_manager.complete_task(index)
            self.tasks_listbox.itemconfig(index, bg="lightgray", fg="gray")
            messagebox.showinfo("Success", f"Task '{task.name}' marked as completed.")
        else:
            messagebox.showerror("Error", "No task selected.")

    def list_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            status = "Completed" if task.completed else "Not Completed"
            self.tasks_listbox.insert(tk.END, f"{task.name} ({status})")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

    def complete_task(self, index):
        self.tasks[index].completed = True

    def get_task(self, index):
        return self.tasks[index]


# Creating an instance of TaskManagerApp
app = TaskManagerApp()
app.mainloop()
