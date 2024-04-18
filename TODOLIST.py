from tkinter import *
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x300+800+400')
        self.master.title('To-Do List')
        self.master.config(bg='#8B4513')
        self.master.resizable(width=True, height=False)

        self.task_list = []

        self.frame = Frame(self.master, bg='#8B4513')
        self.frame.pack(pady=10)

        self.lb = Listbox(
            self.frame,
            width=40,
            height=10,
            font=('Courier', 12, 'bold'),
            bd=0,
            fg='#FFFFFF',
            highlightthickness=0,
            selectbackground='#DAA520',
            activestyle="none",
            bg='#8B4513'
        )
        self.lb.pack(side=LEFT, fill=BOTH)

        self.sb = Scrollbar(self.frame)
        self.sb.pack(side=RIGHT, fill=BOTH)

        self.lb.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.lb.yview)

        self.my_entry = Entry(
            self.master,
            font=('Courier', 12),
            bg='#DAA520'
            )
        self.my_entry.pack(pady=10, padx=10, fill=X)

        self.button_frame = Frame(self.master, bg='#8B4513')
        self.button_frame.pack(pady=5)

        self.addTask_btn = Button(
            self.button_frame,
            text='Add Task',
            font=('Courier', 12),
            bg='#CD853F',
            fg='#FFFFFF',
            padx=15,
            pady=6,
            command=self.newTask
        )
        self.addTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=5)

        self.delTask_btn = Button(
            self.button_frame,
            text='Delete Task',
            font=('Courier', 12),
            bg='#CD853F',
            fg='#FFFFFF',
            padx=15,
            pady=6,
            command=self.deleteTask
        )
        self.delTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=5)

        self.updateTask_btn = Button(
            self.button_frame,
            text='Update Task',
            font=('Courier', 12),
            bg='#CD853F',
            fg='#FFFFFF',
            padx=15,
            pady=6,
            command=self.updateTask
        )
        self.updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=5)

        self.completeTask_btn = Button(
            self.button_frame,
            text='Complete Task',
            font=('Courier', 12),
            bg='#CD853F',
            fg='#FFFFFF',
            padx=15,
            pady=6,
            command=self.completeTask
        )
        self.completeTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5, pady=5)

    def newTask(self):
        task = self.my_entry.get()
        if task.strip():
            self.task_list.append(task)
            self.lb.insert(END, task)
            self.my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter some task.")

    def deleteTask(self):
        selected_index = self.lb.curselection()
        if selected_index:
            self.lb.delete(selected_index)
            del self.task_list[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def updateTask(self):
        selected_index = self.lb.curselection()
        if selected_index:
            updated_task = self.my_entry.get()
            if updated_task.strip():
                self.task_list[selected_index[0]] = updated_task
                self.lb.delete(selected_index)
                self.lb.insert(selected_index, updated_task)
                self.my_entry.delete(0, END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def completeTask(self):
        selected_index = self.lb.curselection()
        if selected_index:
            task = self.task_list[selected_index[0]]
            if not task.startswith("[Done]"):
                updated_task = f"[Done] {task}"
                self.task_list[selected_index[0]] = updated_task
                self.lb.delete(selected_index)
                self.lb.insert(selected_index, updated_task)
            else:
                messagebox.showinfo("Info", "Task is already marked as completed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def main():
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
