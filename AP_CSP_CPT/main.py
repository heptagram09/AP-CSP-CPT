todo_list = []

def add_task(name, priority):
    task = {"name": name, "priority": priority, "done": False}
    todo_list.append(task)
    print("Added: [" + priority + "] " + name)

def filter_tasks(priority):
    result = []
    for task in todo_list:
        if priority == "all":
            result.append(task)
        elif task["priority"] == priority:
            result.append(task)
    return result

def show_tasks(priority):
    tasks = filter_tasks(priority)
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for task in tasks:
        if task["done"]:
            status = "DONE"
        else:
            status = "TODO"
        print("[" + task["priority"] + "] " + task["name"] + " - " + status)

def mark_done(task_name):
    for task in todo_list:
        if task["name"] == task_name:
            task["done"] = True
            print(task_name + " marked as done!")
            return
    print("Error: " + task_name + " not found.")

print("=== To-Do List App ===")

while True:
    print("")
    print("A. Add task")
    print("S. Show tasks")
    print("D. Mark task done")
    print("F. Quit")
    choice = input("Choose: ")

    if choice == "A":
        name = input("Task name: ")
        priority = input("Priority (high/medium/low): ")
        if priority not in ["high", "medium", "low"]:
            print("Invalid priority.")
        else:
            add_task(name, priority)

    elif choice == "S":
        priority = input("Filter (all/high/medium/low): ")
        show_tasks(priority)

    elif choice == "D":
        name = input("Task name to mark done: ")
        mark_done(name)

    elif choice == "F":
        print("See you later..")
        break