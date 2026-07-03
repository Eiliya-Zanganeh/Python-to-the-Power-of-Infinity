import json

with open('data.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

while True:
    print("Todo List App")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Task done")
    print("6. Quit")

    action = int(input('Enter action: '))

    if action == 1:
        if len(tasks) == 0:
            print("Tasks not exist 😶‍🌫️")

        for task in tasks:
            print(f"Task title: {task['title']}")
            print(f"Task description: {task['description']}")
            is_done_mark = '✅' if task['is_done'] else '❌'
            print(f"Task done: {is_done_mark}")
            print("-" * 20)


    elif action == 2:
        task_title = input('Enter task title: ')
        task_description = input('Enter task description: ')
        task = {
            'title': task_title,
            'description': task_description,
            'is_done': False
        }
        tasks.append(task)
        print("Task saved ✅")

    elif action == 3:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1} - Task title: {task['title']}")

        selected_index = int(input('Select task: '))

        task_title = input('Enter task updated title: ')
        task_description = input('Enter task updated description: ')
        task = {
            'title': task_title,
            'description': task_description,
            'is_done': False
        }
        tasks[selected_index - 1] = task
        print(f"Task {selected_index} was updated ✅")

    elif action == 4:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1} - Task title: {task['title']}")

        selected_index = int(input('Select task: '))
        tasks.pop(selected_index - 1)
        print(f"Task {selected_index} removed ✅")

    elif action == 5:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1} - Task title: {task['title']}")

        selected_index = int(input('Select task: '))
        tasks[selected_index - 1]['is_done'] = True
        print(f'Task {selected_index} was updated ✅')


    elif action == 6:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4)
        print("Good Lock 😊")
        break
