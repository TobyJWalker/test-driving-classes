class TaskTracker():
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        if type(task) != str:
            raise TypeError("Task must be a string")
        elif task == "" or task.isspace():
            raise ValueError("Task must not be empty")
        self.tasks.append(task)
    
    def get_tasks(self):
        return self.tasks
    
    def mark_complete(self, task):
        if type(task) != str:
            raise TypeError("Task must be a string")
        elif task == "" or task.isspace():
            raise ValueError("Task must not be empty")
        elif task not in self.tasks:
            raise ValueError("Task not found")
        self.tasks = [t for t in self.tasks if t != task]