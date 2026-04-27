# Jack CPT Video 콘티

## To-Do List App

### PPR / FRQ 연결형 1분 영상 시나리오

## 0. 영상의 목표

이 영상은 다음 4가지를 보여주는 데 집중한다.

| 목표              | 영상에서 보여줄 장면                                        |
| --------------- | -------------------------------------------------- |
| Program purpose | 사용자가 할 일을 추가하고 관리함                                 |
| Input           | task name, priority, filter choice, task number 입력 |
| Functionality   | task 추가, priority별 filtering, done 처리              |
| Output          | 추가 메시지, filtered list, done status 출력              |

이 영상은 특히 PPR 대표 procedure인

```python
filter_tasks(task_list, selected_priority)
```

와 잘 연결되어야 한다.

---

# 1. PPR / FRQ / Video 연결 구조

| 요소             | PPR 코드                                                                 | FRQ 답변 방향                                            | Video에서 보여줄 장면        |
| -------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- | --------------------- |
| List storage   | `add_task(task_list, task_name, priority)`                             | `todo_list`가 task data 저장                            | task 2개 추가            |
| List use       | `filter_tasks(...)`                                           | list를 loop로 filtering                                | `high` filter 실행      |
| Procedure      | `filter_tasks(task_list, selected_priority)`                  | selection + iteration + sequencing 설명                | high task만 출력         |
| Procedure call | `show_tasks(filter_tasks(todo_list, p))` | user input에 따라 output 달라짐                            | `high` vs `all` 결과 비교 |
| Testing        | high filter / all filter                                               | different parameter values produce different results | high는 1개, all은 2개 출력  |
| Output         | `show_tasks(...)`                                        | filtered tasks displayed                             | TODO / DONE status 출력 |

---

# 2. 추천 영상 흐름 요약

영상은 **add → add → filter high → mark done → filter all** 순서가 가장 좋습니다.

```text
1. Add task: Study AP CSP, priority high
2. Add task: Clean room, priority low
3. Show tasks with filter high
4. Mark Study AP CSP as done
5. Show tasks with filter all
```

이 흐름이 좋은 이유는 다음과 같습니다.

| 장면             | AP CSP 방어 포인트                              |
| -------------- | ------------------------------------------ |
| Add task 2개    | list에 여러 data가 저장됨                         |
| Filter high    | procedure parameter가 output에 영향을 줌         |
| Mark done      | program functionality가 단순 filtering보다 풍부해짐 |
| Filter all     | testing에서 high vs all 비교 가능                |
| DONE / TODO 출력 | output이 input과 program state에 따라 달라짐       |

---

# 3. 1분 영상 콘티

## Scene 1. 앱 시작 화면

### 0:00–0:05

### 화면

```text
=== PRIORITY PLANNER ===

1.Add 2.Show 3.Done 4.Exit
Select:
```

### Text caption 권장

```text
This program helps users manage tasks by priority.
```

### 보여주는 의미

WR1에서 말할 program purpose를 영상 첫 장면에서 자연스럽게 보여준다.

---

## Scene 2. 첫 번째 task 추가

### 0:05–0:15

### 입력

```text
Select: 1
Task: Study AP CSP
Priority (high/medium/low): high
```

### 출력

```text
Added: [high] Study AP CSP
```

### Text caption 권장

```text
Input: task name and priority
Output: task added
```

### PPR 연결

이 장면은 List storage 캡처와 연결된다.

```python
add_task(todo_list, name, p)
```

### FRQ 연결

WR2(c)에서 이렇게 말할 수 있다.

```text
The list todo_list stores task records. Each task stores a name, priority, and done status.
```

---

## Scene 3. 두 번째 task 추가

### 0:15–0:25

### 입력

```text
Select: 1
Task: Clean room
Priority (high/medium/low): low
```

### 출력

```text
Added: [low] Clean room
```

### Text caption 권장

```text
The list can store multiple tasks.
```

### 보여주는 의미

task가 하나만 있는 것이 아니라, list가 여러 task를 저장한다는 것을 보여준다.

이 장면은 WR2(c)의 complexity 답변을 강화한다.

```text
Without the list, I would need separate variables for each task.
```

---

## Scene 4. priority filter 실행

### 0:25–0:38

### 입력

```text
Select: 2
Filter (all/high/medium/low): high
```

### 출력

```text
--- Tasks ---
1. [high] Study AP CSP (TODO)
```

### Text caption 권장

```text
The procedure filters tasks by selected priority.
```

### PPR 연결

이 장면은 핵심 procedure와 직접 연결된다.

```python
show_tasks(filter_tasks(todo_list, p))
```

그리고 procedure 내부에서는 다음 logic이 실행된다.

```python
for task in task_list:
    if selected_priority == "all" or task["priority"] == selected_priority:
        filtered_list.append(task)
```

### FRQ 연결

WR2(a) Algorithm Development에서 이렇게 설명한다.

```text
The procedure loops through each task in task_list. It uses selection to check whether the selected priority is "all" or matches the task’s priority. If the condition is true, the task is added to filtered_list.
```

WR2(b) Testing에서는 이렇게 말할 수 있다.

```text
When selected_priority is "high", only the high priority task should be returned.
```

---

## Scene 5. task 완료 처리

### 0:38–0:48

### 입력

```text
Select: 3

--- Tasks ---
1. [high] Study AP CSP (TODO)
2. [low] Clean room (TODO)
Enter number: 1
```

### 출력

```text
Completed: Study AP CSP
```

### Text caption 권장

```text
The program updates a task’s status.
```

### 보여주는 의미

이 장면은 필수는 아니지만, 앱이 단순히 출력만 하는 것이 아니라 **data 상태를 바꾸는 기능**이 있음을 보여준다.

WR1에서 “mark tasks as done” 기능을 말할 수 있게 해준다.

---

## Scene 6. all filter로 최종 상태 확인

### 0:48–0:58

### 입력

```text
Select: 2
Filter (all/high/medium/low): all
```

### 출력

```text
--- Tasks ---
1. [high] Study AP CSP (DONE)
2. [low] Clean room (TODO)
```

### Text caption 권장

```text
Using "all" returns every task in the list.
```

### PPR / FRQ 연결

이 장면은 WR2(b) testing에서 아주 중요하다.

```text
When selected_priority is "all", both tasks should be returned because the condition selected_priority == "all" is true for every task.
```

또한 WR2(c) list complexity 답변에도 연결된다.

```text
The same procedure works even if more tasks are added.
```

---

# 4. 최종 추천 영상 대본

## 실제 입력 순서

아래 순서대로 그대로 찍으면 됩니다.

```text
=== PRIORITY PLANNER ===

1.Add 2.Show 3.Done 4.Exit
Select: 1
Task: Study AP CSP
Priority (high/medium/low): high
Added: [high] Study AP CSP

1.Add 2.Show 3.Done 4.Exit
Select: 1
Task: Clean room
Priority (high/medium/low): low
Added: [low] Clean room

1.Add 2.Show 3.Done 4.Exit
Select: 2
Filter (all/high/medium/low): high

--- Tasks ---
1. [high] Study AP CSP (TODO)

1.Add 2.Show 3.Done 4.Exit
Select: 3

--- Tasks ---
1. [high] Study AP CSP (TODO)
2. [low] Clean room (TODO)
Enter number: 1
Completed: Study AP CSP

1.Add 2.Show 3.Done 4.Exit
Select: 2
Filter (all/high/medium/low): all

--- Tasks ---
1. [high] Study AP CSP (DONE)
2. [low] Clean room (TODO)
```

마지막에 `4.Exit`까지 보여줄 필요는 없습니다. 1분 제한 안에서 input, functionality, output을 보여주는 것이 더 중요합니다.

---

# 5. 영상에 넣을 Text Caption 추천

음성 narration은 금지되어 있으므로, 화면 하단에 짧은 caption을 넣는 방식이 좋습니다. College Board는 voice narration은 포함하면 안 되지만 text captions는 허용된다고 안내합니다. 

| 장면           | Caption                                   |
| ------------ | ----------------------------------------- |
| 시작           | `Purpose: Manage tasks by priority`       |
| task 추가      | `Input: task name and priority`           |
| 두 번째 task 추가 | `The list stores multiple tasks`          |
| high filter  | `Functionality: filter tasks by priority` |
| mark done    | `The program updates task status`         |
| all filter   | `Output changes based on selected filter` |

caption은 너무 길지 않게 해야 합니다. 영상은 코드 설명 영상이 아니라 **프로그램 실행 시연 영상**입니다.

---

# 6. PPR 캡처와 영상 장면 매칭

## PPR Capture 1

### List에 data 저장

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

### 영상 매칭

```text
Add task: Study AP CSP
Add task: Clean room
```

### FRQ 연결

```text
The list todo_list stores all task records in one collection.
```

---

## PPR Capture 2 & 3

### 같은 list 사용 & Student-developed procedure

```python
def filter_tasks(task_list, selected_priority):
    filtered_list = []
    for task in task_list:
        if selected_priority == "all" or task["priority"] == selected_priority:
            filtered_list.append(task)
    return filtered_list
```

### 영상 매칭

```text
Filter: high
Filter: all
```

### FRQ 연결

```text
The procedure uses the list by iterating through each task and selecting matching tasks.
The selected_priority parameter changes which tasks are returned.
```

---

## PPR Capture 4

### Procedure call

```python
    elif cmd == "2":
        p = get_filter()
        show_tasks(filter_tasks(todo_list, p))
```

### 영상 매칭

```text
Select 2 → Filter high
Select 2 → Filter all
```

### FRQ 연결

```text
The returned list is displayed to the user.
```

---

# 7. FRQ 4개 프롬프트와 영상 연결

| FRQ                | 답변 핵심                                            | 영상에서 보이는 증거              |
| ------------------ | ------------------------------------------------ | ------------------------ |
| WR1 Program Design | To-do list 관리, task 추가, priority filter, done 처리 | add, show, mark done     |
| WR2(a) Algorithm   | loop + if로 selected priority와 task priority 비교   | high filter 장면           |
| WR2(b) Testing     | high vs all parameter 비교                         | high는 1개, all은 2개        |
| WR2(c) Abstraction | `todo_list`가 여러 task를 하나로 관리                     | task 2개 저장 후 같은 loop로 처리 |

---

# 8. 시간 배분 추천

|        시간 | 장면              | 핵심                      |
| --------: | --------------- | ----------------------- |
| 0:00–0:05 | 앱 시작            | purpose                 |
| 0:05–0:15 | Study AP CSP 추가 | input + list storage    |
| 0:15–0:25 | Clean room 추가   | multiple data           |
| 0:25–0:38 | high filter     | procedure functionality |
| 0:38–0:48 | mark done       | update functionality    |
| 0:48–0:58 | all filter      | output comparison       |
| 0:58–1:00 | 정지              | 여유                      |

1분을 넘기지 않는 것이 중요합니다. AP Digital Portfolio Student User Guide도 video는 60초 이하, 30MB 이하라고 안내합니다. 

---

# 9. 촬영 전 체크리스트

| 체크                 | 기준                                      |
| ------------------ | --------------------------------------- |
| 1분 이하              | 반드시 60초 안에 종료                           |
| 30MB 이하            | 용량 확인                                   |
| 음성 narration 없음    | 녹음 끄기                                   |
| 개인 정보 없음           | 이름, 학교, 얼굴, 계정 정보 노출 금지                 |
| input 보임           | task name, priority, filter 입력          |
| functionality 보임   | add, filter, mark done                  |
| output 보임          | added message, filtered list, DONE/TODO |
| PPR procedure와 연결됨 | high / all filter 장면 포함                 |
| FRQ testing과 연결됨   | high vs all 결과 차이 보임                    |

---

# 10. 최종 콘셉트 문장

Jack 영상의 전체 콘셉트는 이것입니다.

```text
The video demonstrates a to-do list app where the user adds tasks, filters them by priority, marks a task as done, and views the updated list.
```

FRQ와 연결하면 이렇게 정리됩니다.

```text
The same task list is used throughout the video. The filter_tasks procedure changes the output depending on the selected_priority parameter, which makes the video useful for explaining purpose, algorithm, testing, and abstraction.
```
