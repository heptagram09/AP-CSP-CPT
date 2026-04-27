VALID_PRIORITIES = ["high", "medium", "low"]

todo_list = []


def add_task(task_list, task_name, priority):
    task_list.append({
        "name": task_name,
        "priority": priority,
        "done": False
    })

    return "Added: [" + priority + "] " + task_name


def get_tasks_by_priority(task_list, selected_priority):
    matching_tasks = []

    for task in task_list:
        if selected_priority == "all" or task["priority"] == selected_priority:
            matching_tasks.append(task)

    return matching_tasks


def display_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks found.")
        return

    for index in range(len(task_list)):
        task = task_list[index]

        if task["done"]:
            status = "DONE"
        else:
            status = "TODO"

        print(str(index + 1) + ". [" + task["priority"] + "] " + task["name"] + " - " + status)


def mark_task_done(task_list, task_number):
    if task_number >= 1 and task_number <= len(task_list):
        task_list[task_number - 1]["done"] = True
        return "Marked as done: " + task_list[task_number - 1]["name"]

    return "Error: task number not found."


def get_valid_priority():
    while True:
        priority = input("Priority (high/medium/low): ").lower()

        if priority in VALID_PRIORITIES:
            return priority

        print("Please enter high, medium, or low.")


def get_filter_choice():
    while True:
        selected_priority = input("Filter (all/high/medium/low): ").lower()

        if selected_priority == "all" or selected_priority in VALID_PRIORITIES:
            return selected_priority

        print("Please enter all, high, medium, or low.")


def get_task_number():
    while True:
        try:
            task_number = int(input("Task number to mark done: "))
            return task_number
        except ValueError:
            print("Please enter a number.")


print("=== To-Do List App ===")

while True:
    print("")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task done")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task_name = input("Task name: ")
        priority = get_valid_priority()
        message = add_task(todo_list, task_name, priority)
        print(message)

    elif choice == "2":
        selected_priority = get_filter_choice()
        matching_tasks = get_tasks_by_priority(todo_list, selected_priority)
        display_tasks(matching_tasks)

    elif choice == "3":
        display_tasks(todo_list)
        task_number = get_task_number()
        message = mark_task_done(todo_list, task_number)
        print(message)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")
