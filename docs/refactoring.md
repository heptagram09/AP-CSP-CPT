좋습니다. 먼저 확인부터 하면, **현재 이 대화에서 제가 확인할 수 있는 Jack 파일은 기존 `main.py`입니다.** 이 파일은 `todo_list`, `add_task`, `filter_tasks`, `show_tasks`, `mark_done` 구조를 가지고 있습니다. 
만약 Jack이 실제로 수정한 “updated code”를 따로 만들었다면 그 파일을 다시 올려주면 됩니다. 아래 평가는 **현재 확인되는 Jack 코드 + Johnson 리팩토링 때 적용한 기준**으로 면밀히 보는 것입니다.

College Board 기준상 PPR에는 **student-developed procedure와 procedure call**, 그리고 **list에 data가 저장되는 코드와 같은 list가 사용되는 코드**가 필요합니다. 특히 procedure에는 parameter가 있고, 그 안의 algorithm이 sequencing, selection, iteration을 포함해야 합니다.  시험 당일 written response는 PPR 코드와 연결된 4개 프롬프트, 즉 WR1, WR2(a), WR2(b), WR2(c)에 답하는 구조입니다. ([apstudents.collegeboard.org][1])

---

# 1. Jack 기존 코드 총평

Jack의 기존 코드는 **AP CSP 최소 요건은 충족 가능**합니다. 특히 `filter_tasks(priority)`는 PPR 대표 procedure로 쓸 수 있습니다.

```python
def filter_tasks(priority):
    result = []
    for task in todo_list:
        if priority == "all" or task["priority"] == priority:
            result.append(task)
    return result
```

이 함수에는 parameter, iteration, selection, sequencing이 모두 있습니다. 그러나 Johnson 리팩토링 기준으로 보면 **코드 흐름이 아직 약합니다.**

| 영역               | 기존 Jack 코드 평가                   |
| ---------------- | ------------------------------- |
| Program purpose  | To-Do List App으로 명확함            |
| List             | `todo_list` 사용. 좋음              |
| Procedure        | `filter_tasks(priority)`가 가장 적합 |
| Algorithm        | selection + iteration 있음        |
| Input validation | 약함. priority 입력 검증 없음           |
| Code flow        | global `todo_list`에 직접 의존       |
| Testing          | `high` vs `all` 테스트 가능          |
| PPR 방어력          | 가능하지만 리팩토링하면 훨씬 선명해짐            |

---

# 2. 기존 코드의 아쉬운 점

## 1. `todo_list`를 global로 직접 사용함

기존 함수들은 모두 외부의 `todo_list`를 직접 참조합니다.

```python
todo_list = []
```

```python
def filter_tasks(priority):
    result = []
    for task in todo_list:
```

AP CSP에서 global list가 금지된 것은 아닙니다. 하지만 Johnson 리팩토링 때처럼 list를 parameter로 넘기면 procedural abstraction 설명이 더 강해집니다.

더 좋은 구조:

```python
def filter_tasks(task_list, selected_priority):
```

이렇게 하면 FRQ에서 이렇게 말할 수 있습니다.

> The procedure can work with any task list passed as a parameter.

이게 훨씬 강합니다.

---

## 2. `add_task()`는 PPR 대표 procedure로 약함

기존 코드의 `add_task()`는 list storage용으로는 좋습니다.

```python
def add_task(name, priority):
    task = {"name": name, "priority": priority, "done": False}
    todo_list.append(task)
    print("Added: [" + priority + "] " + name)
```

하지만 이 함수는 **iteration이 없습니다.**
따라서 WR2(a) Algorithm Development 방어용 대표 procedure로 쓰면 위험합니다.

대표 procedure는 반드시 `filter_tasks()` 또는 리팩토링 후 `filter_tasks()`로 가야 합니다.

---

## 3. priority validation이 없음

기존 코드는 사용자가 `urgent`, `HIGH`, `abc`를 입력해도 그대로 저장합니다.

```python
priority = input("Priority (high/medium/low): ")
```

이건 큰 감점 요소는 아니지만, 영상 촬영이나 테스트 중 앱이 어설퍼 보일 수 있습니다.

---

## 4. `mark_done(task_name)`은 중복 task name에 약함

```python
def mark_done(task_name):
    for task in todo_list:
        if task["name"] == task_name:
            task["done"] = True
```

같은 이름의 task가 여러 개 있으면 첫 번째 task만 완료 처리됩니다. 시험용으로 치명적이지는 않지만, 앱 로직은 약해 보입니다.

---

# 3. Jack 리팩토링 방향

Johnson 때와 같은 원칙을 적용하면 Jack은 이렇게 가는 것이 좋습니다.

| 리팩토링 목표          | 방향                                                                      |
| ---------------- | ----------------------------------------------------------------------- |
| list 역할 선명화      | `todo_list`는 모든 task record 저장                                          |
| procedure 역할 선명화 | `filter_tasks(task_list, selected_priority)`를 대표 procedure로 설정 |
| parameter 효과 강화  | `task_list`, `selected_priority` 값이 결과에 직접 영향                           |
| output 흐름 강화     | filter 결과를 display 함수로 출력                                               |
| testing 단순화      | `"high"` vs `"all"` 테스트로 준비                                             |
| video 흐름 선명화     | add → show filtered → mark done → show all                              |

---

# 4. 추천 리팩토링 전체 코드

PPR 캡처에는 comments가 들어가면 안 됩니다. College Board도 PPR에는 comments가 없어야 하며, comments가 포함되면 Create PT와 written response에 0점 위험이 있다고 안내합니다. ([AP Central][2])
그래서 아래 코드는 **주석 없이** 작성했습니다.

```python
priority_list = ["high", "medium", "low"]
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
        if p in priority_list:
            return p
        print("Invalid.")

def get_filter():
    while True:
        p = input("Filter (all/high/medium/low): ").lower()
        if p == "all" or p in priority_list:
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
```

---

# 5. 왜 이 리팩토링이 더 강한가?

## 기존 핵심 기능은 유지

| 기존 기능             | 리팩토링 후 |
| ----------------- | ------ |
| task 추가           | 유지     |
| priority 저장       | 유지     |
| priority별 task 보기 | 유지     |
| task 완료 처리        | 유지     |
| task status 출력    | 유지     |

## AP CSP 방어력은 더 좋아짐

| 개선점 | 효과 |
| --- | --- |
| `add_task(task_list, task_name, priority)` | list storage가 선명함 |
| `filter_tasks(task_list, selected_priority)` | 대표 procedure로 매우 강함 |
| `task_list`를 parameter로 받음 | procedural abstraction 설명 강화 |
| `selected_priority`가 결과를 바꿈 | parameter effect 설명 쉬움 |
| `return filtered_list` | testing에서 expected result 설명 쉬움 |
| 직관적 네이밍 유지 | 변수 의미 파악 용이 |
| mark_done 번호 처리 | 중복 이름 문제 해결 |

---

# 6. PPR 4개 캡처 추천

## Capture 1. List에 data가 저장되는 코드

```python
def add_task(task_list, task_name, priority):
    task = {
        "task_name": task_name,
        "priority": priority,
        "done": False
    }
    task_list.append(task)
    return "Added: [" + priority + "] " + task_name
```

| 요소 | 설명 |
| ----------- | ------------------------------------- |
| List | `task_list`, 실제 argument는 `todo_list` |
| Stored data | `task_name`, `priority`, `done` |
| Complexity  | 여러 task를 같은 구조로 저장                    |

---

## Capture 2. 같은 list가 사용되는 코드

```python
def filter_tasks(task_list, selected_priority):
    filtered_list = []

    for task in task_list:
        if selected_priority == "all" or task["priority"] == selected_priority:
            filtered_list.append(task)

    return filtered_list
```

이 캡처는 list use와 procedure definition을 동시에 방어합니다.

| 요소 | 설명 |
| ------------------- | ----------------------------------- |
| Same list used | `task_list` |
| Iteration | `for task in task_list` |
| Selection | selected_priority와 task priority 비교 |
| Output of procedure | `filtered_list` 반환 |

---

## Capture 3. Student-developed procedure 정의

대표 procedure는 동일하게 이것입니다.

```python
def filter_tasks(task_list, selected_priority):
    filtered_list = []

    for task in task_list:
        if selected_priority == "all" or task["priority"] == selected_priority:
            filtered_list.append(task)

    return filtered_list
```

이 procedure는 AP CSP 기준이 매우 선명합니다.

| AP CSP 요구 조건 | 코드에서 보이는 부분 |
| ------------------------------- | ------------------------------------------------------------------------ |
| Procedure name | `filter_tasks` |
| Parameters | `task_list`, `selected_priority` |
| Parameter affects functionality | selected_priority에 따라 결과가 달라짐 |
| Iteration | `for task in task_list` |
| Selection | `if selected_priority == "all" or task["priority"] == selected_priority` |
| Sequencing | create list → loop → condition check → append → return |
| List use | task_list traversal |
| Return value | filtered_list |

---

## Capture 4. Procedure call

```python
    elif cmd == "2":
        p = get_filter()
        show_tasks(filter_tasks(todo_list, p))
```

| 요소 | 설명 |
| -------------- | ----------------------------------------------------- |
| Procedure call | `filter_tasks(todo_list, p)` |
| Arguments | `todo_list`, `p` |
| Input | filter choice |
| Output | filtered tasks displayed |

---

# 7. FRQ 4개 프롬프트 방어

## WR1. Program Design, Function, and Purpose

```text
The purpose of my program is to help users manage a to-do list. The user can add tasks, assign each task a priority, view tasks by priority, and mark tasks as done. The program takes input such as the task name, priority, filter choice, and task number. The output includes messages confirming that a task was added or completed, and a displayed list of tasks that match the selected priority.
```

---

## WR2(a). Algorithm Development

```text
My selected procedure is filter_tasks. First, it creates an empty list called filtered_list. Then it iterates through each task in task_list. For each task, it uses selection to check whether selected_priority is "all" or whether the task's priority matches selected_priority. If the condition is true, the task is added to filtered_list. After all tasks have been checked, the procedure returns filtered_list.
```

| 요소               | 설명                                                     |
| ---------------- | ------------------------------------------------------ |
| Sequencing       | create list → loop → condition check → append → return |
| Selection        | selected priority가 all인지 또는 task priority와 같은지 확인      |
| Iteration        | task list traversal                                    |
| Parameter effect | `selected_priority`에 따라 반환 리스트가 달라짐 |

---

## WR2(b). Errors and Testing

### Test Case 1: High priority filter

```text
Input:
Add task Study AP CSP with priority high.
Add task Clean room with priority low.
Filter by high.

Expected result:
Only Study AP CSP is displayed.
```

### Test Case 2: All filter

```text
Input:
Add task Study AP CSP with priority high.
Add task Clean room with priority low.
Filter by all.

Expected result:
Both Study AP CSP and Clean room are displayed.
```

### 5점 목표 답변

```text
I tested filter_tasks with different values for selected_priority. In the first test, I added one high priority task and one low priority task, and then selected "high" as the filter. The expected result was that only the high priority task would be returned. In the second test, I selected "all" as the filter. The expected result was that both tasks would be returned because the condition selected_priority == "all" is true for every task.
```

### Runtime error 대비

```text
A change that would cause a run-time error is replacing task["priority"] with task["level"]. Each task dictionary stores the priority using the key "priority", not "level". If the procedure tries to access task["level"], Python will raise a KeyError because that key does not exist.
```

---

## WR2(c). Data and Procedural Abstraction

### Data abstraction 답변

```text
The list todo_list stores all task records in one collection. Each task stores a task_name, priority, and done status. This manages complexity because the program can process any number of tasks using the same loop. Without the list, I would need separate variables such as task1_name, task1_priority, task1_done, etc. With the list, the same procedure works even if more tasks are added.
```

### Procedural abstraction 답변

```text
The procedure filter_tasks manages complexity by separating the filtering logic into one reusable procedure. Instead of writing separate code each time the user wants to view tasks, the program calls filter_tasks with a list and a selected priority. This makes the program easier to read, reuse, and modify.
```

---

# 8. Video 시나리오 추천

1분 이내 영상은 이렇게 찍으면 됩니다.

```text
1. Add Task
   Task: Study AP CSP
   Priority: high
   Output: Added: [high] Study AP CSP

2. Add Task
   Task: Clean room
   Priority: low
   Output: Added: [low] Clean room

3. Show List
   Filter: high
   Output: only Study AP CSP appears

4. Mark Done
   Task number: 1
   Output: Completed: Study AP CSP

5. Show List
   Filter: all
   Output: Study AP CSP (DONE), Clean room (TODO)
```

이 영상은 input, functionality, output을 모두 보여줍니다. College Board의 Student Handouts도 video는 program running, input, program functionality, output을 보여야 한다고 설명합니다. 

---

# 9. 최종 판단

Jack의 기존 코드도 5점 목표는 가능하지만, 리팩토링 버전이 훨씬 더 안정적입니다.

| 영역 | 기존 코드 | 리팩토링 후 |
| --------------- | ------------------------ | ----------------------------------------------------- |
| Program purpose | 명확 | 더 명확 |
| List | `todo_list` 역할 있음 | `task_list` parameter로 더 선명 |
| Procedure | `filter_tasks(priority)` | `filter_tasks(task_list, selected_priority)` |
| Parameter | priority만 있음 | list와 priority 모두 있음 |
| Algorithm | selection, iteration 있음 | selection, iteration, sequencing 설명 더 쉬움 |
| Testing | high vs all 가능 | high vs all 매우 명확 |
| PPR | 가능 | 4개 캡처 구성이 깔끔 |
| Video | 가능 | add → filter → done → show 흐름 자연스러움 |

최종적으로 Jack에게는 이렇게 지도하면 됩니다.

> Jack, your project idea is good, but the refactored version makes your CPT much easier to explain for AP CSP. Your strongest procedure is `filter_tasks(task_list, selected_priority)`. It has parameters, uses a list, includes a loop, uses an if statement, and returns a filtered list. For the PPR, focus on `todo_list` and `filter_tasks`. For the written responses, explain how the list stores all tasks and how the procedure filters tasks based on the selected priority.

[1]: https://apstudents.collegeboard.org/courses/ap-computer-science-principles/assessment?utm_source=chatgpt.com "AP Computer Science Principles Assessment – AP Students"
[2]: https://apcentral.collegeboard.org/courses/ap-computer-science-principles/course/faq/students-attestation?utm_source=chatgpt.com "What must students attest to? – AP Central | College Board"
