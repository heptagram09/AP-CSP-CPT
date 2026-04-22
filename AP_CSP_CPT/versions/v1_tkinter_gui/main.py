import tkinter as tk

todoList = []

def addTask(name, priority):
    todoList.append({"id": len(todoList) + 1, "name": name, "priority": priority})

def filterTasks(priority):
    result = []
    for task in todoList:
        if priority == "all":
            result.append(task)
        elif task["priority"] == priority:
            result.append(task)
    return result

def showList(priority):
    tasks = filterTasks(priority)
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, f"--- [{priority}] {len(tasks)} tasks ---")
    if len(tasks) == 0:
        listbox.insert(tk.END, "  No tasks found")
    for task in tasks:
        listbox.insert(tk.END, f"  {task['id']}. [{task['priority']}] {task['name']}")

def onAdd():
    name = nameEntry.get().strip()
    priority = priorityVar.get()
    if not name:
        statusLabel.config(text="Enter a task name")
        return
    addTask(name, priority)
    nameEntry.delete(0, tk.END)
    statusLabel.config(text=f"Added: [{priority}] {name}")
    showList("all")

def onFilter():
    priority = filterVar.get()
    showList(priority)

def delete():
    todoList.clear()
    listbox.delete(0, tk.END)
    statusLabel.config(text="All tasks deleted")

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")
window.resizable(False, False)

tk.Label(window, text="Task name:").pack(pady=(16, 2))
nameEntry = tk.Entry(window, width=36)
nameEntry.pack()

tk.Label(window, text="Priority:").pack(pady=(10, 2))
priorityVar = tk.StringVar(value="normal")
priorityFrame = tk.Frame(window)
priorityFrame.pack()
for p in ["hard", "normal", "easy"]:
    tk.Radiobutton(priorityFrame, text=p, variable=priorityVar, value=p).pack(side=tk.LEFT, padx=8)

tk.Button(window, text="Add Task", command=onAdd, width=16).pack(pady=10)

statusLabel = tk.Label(window, text="", fg="gray")
statusLabel.pack()

tk.Label(window, text="Filter:").pack(pady=(10, 2))
filterVar = tk.StringVar(value="all")
filterFrame = tk.Frame(window)
filterFrame.pack()
for f in ["all", "hard", "normal", "easy"]:
    tk.Radiobutton(filterFrame, text=f, variable=filterVar, value=f).pack(side=tk.LEFT, padx=6)

tk.Button(window, text="SELECT", command=onFilter, width=16).pack(pady=6)

blank = tk.Label(window, text="", fg="gray")
blank.pack()

tk.Button(window, text="DELETE ALL", command=delete, width=16).pack(pady=6)

listbox = tk.Listbox(window, width=48, height=12)
listbox.pack(pady=10)

window.mainloop()
