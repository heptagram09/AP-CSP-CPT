LEVELS = ["high", "medium", "low"]
todo_list = []

def add_task(task_list, task_name, priority):
    task = {
        "task_name": task_name,
        "priority": priority,
        "done": False
    }
    task_list.append(task)
    return "Added: [" + priority + "] " + task_name

def filter_tasks(task_list, selected_priority):
    filtered_list = []
    for task in task_list:
        if selected_priority == "all" or task["priority"] == selected_priority:
            filtered_list.append(task)
    return filtered_list

def show_tasks(task_list):
    if len(task_list) == 0:
        print("\n[Empty]")
        return

    print("\n--- Tasks ---")
    for i in range(len(task_list)):
        task = task_list[i]
        if task["done"]:
            status = "DONE"
        else:
            status = "TODO"
        
        print(str(i + 1) + ". [" + task["priority"] + "] " + task["task_name"] + " (" + status + ")")

def mark_done(task_list, task_num):
    if task_num >= 1 and task_num <= len(task_list):
        task_list[task_num - 1]["done"] = True
        return "Completed: " + task_list[task_num - 1]["task_name"]
    return "Error: Invalid number."

def get_priority():
    while True:
        p = input("Priority (high/medium/low): ").lower()
        if p in LEVELS:
            return p
        print("Invalid.")

def get_filter():
    while True:
        p = input("Filter (all/high/medium/low): ").lower()
        if p == "all" or p in LEVELS:
            return p
        print("Invalid.")

def get_num():
    while True:
        try:
            return int(input("Enter number: "))
        except ValueError:
            print("Enter a number.")

# Main
print("=== PRIORITY PLANNER ===")

while True:
    print("\n1.Add 2.Show 3.Done 4.Exit")
    cmd = input("Select: ")

    if cmd == "1":
        name = input("Task: ")
        p = get_priority()
        print(add_task(todo_list, name, p))

    elif cmd == "2":
        p = get_filter()
        show_tasks(filter_tasks(todo_list, p))

    elif cmd == "3":
        show_tasks(todo_list)
        print(mark_done(todo_list, get_num()))

    elif cmd == "4":
        print("Bye!")
        break
