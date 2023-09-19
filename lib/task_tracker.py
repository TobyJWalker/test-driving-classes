class TaskTracker():
    def __init__(self):
        self._tasks = []
    
    def add_task(self, task):
        if type(task) != str:
            raise TypeError("Task must be a string")
        elif task == "" or task.isspace():
            raise ValueError("Task must not be empty")
        self._tasks.append(task)
    
    def get_tasks(self):
        return self._tasks
    
    def mark_complete(self, task):
        if type(task) != str:
            raise TypeError("Task must be a string")
        elif task == "" or task.isspace():
            raise ValueError("Task must not be empty")
        elif task not in self._tasks:
            raise ValueError("Task not found")
        self._tasks = [t for t in self._tasks if t != task]