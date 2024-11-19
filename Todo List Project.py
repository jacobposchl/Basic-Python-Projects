import tkinter as tk


task_list = []



def Add_Task(task):
    task_item = task.get()
    task.destroy()
    input_label.destroy()
    task_list.append(f"- {task_item}")
    update_task_list()

def Remove_Task(task):
    task_item = task.get()
    task.destroy()
    input_label.destroy()
    task_list.remove(f"- {task_item}")
    update_task_list()

def Plus_Icon():
    global input_label
    input_box = tk.Entry(root, width=30)
    input_label = tk.Label(root, text="Type the task to add", font=("Helvetica", 10))
    input_label.place(relx=0.5, rely=0.85, anchor='center')
    input_box.place(relx=0.5, rely=0.9, anchor='center')
    input_box.bind('<Return>', lambda event: Add_Task(input_box))

def Delete_Icon():
    global input_label
    input_box = tk.Entry(root, width=30)
    input_label = tk.Label(root, text="Type the task to delete", font=("Helvetica", 10))
    input_label.place(relx=0.5, rely=0.85, anchor='center')
    input_box.place(relx=0.5, rely=0.9, anchor='center')
    input_box.bind('<Return>', lambda event: Remove_Task(input_box))


def update_task_list():
    task_list_var.set("\n".join(task_list))

root = tk.Tk()

root.title("To-do List")
root.geometry("400x400")

task_list_var = tk.StringVar()
task_list_var.set("")


Title = tk.Label(root, text="Taskboard", font=("Helvetica", 16))
Title.pack(pady=20)

Subtitle = tk.Label(root, text="To-do:", font=("Helvetica", 10))
Subtitle.place(x = 10, y = 40)

Tasks = tk.Label(root, textvariable=task_list_var, font=("Helvetica", 10))
Tasks.place(x = 20, y = 60)


add = tk.Button(root, text="+", fg="black", width=10, height=3, bd=1, bg="white", cursor = "hand2", command = Plus_Icon)
add.place(relx = 1.0, x= -10, y=10, anchor="ne")

delete = tk.Button(root, text="Delete", fg="black", width=10, height=3, bd=1, bg="white", cursor = "hand2", command = Delete_Icon)
delete.place(relx=1.0, x=-10, y=370, anchor="se")


root.mainloop()