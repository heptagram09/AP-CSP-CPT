todo_list = []

def add_task(name, priority):
    task = {"name": name, "priority": priority, "done": False}
    todo_list.append(task)
    print("Added: [" + priority + "] " + name)

def filter_tasks(priority):
    result = []
    for task in todo_list:
        if priority == "all" or task["priority"] == priority:
            result.append(task)
    return result

def show_tasks(priority):
    tasks = filter_tasks(priority)
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for i in range(len(tasks)):
        task = tasks[i]
        if task["done"]:
            status = "DONE"
        else:
            status = "TODO"
        print(str(i + 1) + ". [" + task["priority"] + "] " + task["name"] + " - " + status)

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
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task done")
    print("4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Task name: ")
        priority = input("Priority (high/medium/low): ")
        add_task(name, priority)

    elif choice == "2":
        priority = input("Filter (all/high/medium/low): ")
        show_tasks(priority)

    elif choice == "3":
        name = input("Task name to mark done: ")
        mark_done(name)

    elif choice == "4":
        print("Goodbye!")
        break
