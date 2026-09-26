class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        if not task.strip():
            print('Пустая задача, не добавлено')
            return
        self.tasks.append(task)
    
    def remove_task(self, index):
        try:
            self.tasks.pop(index)
        except IndexError:
            print('Такого нет')
    
    def save(self):
        with open('tasks.txt', 'w', encoding='utf-8') as f:
            for task in self.tasks:
                f.write(task + '\n')
    
    def load(self):
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.tasks.append(line.strip())
                
    def __str__(self):
        return f'Задач в списке: {len(self.tasks)}'
    
manager = TaskManager()
manager.add_task('Сходить в зал')
manager.add_task('Погулять')
manager.add_task('Сходить в школу')
manager.add_task('       ')
print(manager.tasks)

manager.save()

manager2 = TaskManager()
manager2.load()
print(manager2.tasks)

print(manager)
        
        