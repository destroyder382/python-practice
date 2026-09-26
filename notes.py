def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, index):
    tasks.pop(index)
    return tasks

def safe_tasks(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')
    return tasks

def load_tasks():
    tasks = []
    with open('tasks.txt', 'r', encoding='utf-8') as f:
        for line in f:
            tasks.append(line.strip())
    return tasks

        

tasks = []
tasks = add_task(tasks, "Сходить в зал")
tasks = add_task(tasks, 'Погулять')
try:
    tasks = remove_task(tasks, 10)
except IndexError:
    print('Такого в списке нет')
 

print(tasks) 
print(safe_tasks(tasks))
print(load_tasks())