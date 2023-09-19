
>>PURPOSE

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

>> CLASS DESIGN

def TaskTracker():
    def __init__(self):
        Purpose: initialise an empty list of tasks
        Input: none
        Output: none
    
    def add_task(self, task):
        Purpose: add a task to the list of tasks
        Input: task (string)
        Output: none
        Errors: type errors, empty string error
    
    def mark_task_complete(self, task):
        Purpose: mark a task as complete
        Input: task (string)
        Output: none
        Errors: type errors, empty string error, task not found error
    
    def get_tasks(self):
        Purpose: return a list of all tasks
        Input: none
        Output: list of tasks (strings)

>> FEATURE TESTS

>> After being initialised, a TaskTracker should have an empty list of tasks
TaskTracker().tasks => []

>> When adding a task, raise an error if input is not a string
TaskTracker().add_task(1) raises TypeError
TaskTracker().add_task([]) raises TypeError
TaskTracker().add_task({}) raises TypeError

>> When adding a task, raise an error if input is an empty string
TaskTracker().add_task('') raises ValueError
TaskTracker().add_task(' ') raises ValueError

>> When adding a task, add it to the list of tasks
tracker = TaskTracker()
tracker.add_task('task 1')
tracker.tasks => ['task 1']
tracker.add_task('task 2')
tracker.tasks => ['task 1', 'task 2']

>> When getting tasks, return the list of tasks
tracker = TaskTracker()
tracker.add_task('task 1')
tracker.get_tasks() => ['task 1']

>> When marking a task as complete, raise an error if input is not a string
TaskTracker().mark_task_complete(1) raises TypeError
TaskTracker().mark_task_complete([]) raises TypeError
TaskTracker().mark_task_complete({}) raises TypeError

>> When marking a task as complete, raise an error if input is an empty string
TaskTracker().mark_task_complete('') raises ValueError
TaskTracker().mark_task_complete(' ') raises ValueError

>> When marking a test as complete, raise an error if the task is not found
tracker = TaskTracker()
tracker.add_task('task 1')
tracker.mark_task_complete('task 2') raises ValueError

>> When marking a task as complete, remove it from the list of tasks
tracker = TaskTracker()
tracker.add_task('task 1')
tracker.mark_task_complete('task 1')
tracker.get_tasks() => []
tracker.add_task('task 1')
tracker.add_task('task 2')
tracker.mark_task_complete('task 1')
tracker.get_tasks() => ['task 2']

>> When marking a task as complete, remove all instances of that task
tracker = TaskTracker()
tracker.add_task('task 1')
tracker.add_task('task 1')
tracker.mark_task_complete('task 1')
tracker.get_tasks() => []