import pytest
from lib.task_tracker import *

def test_task_tracker_initiaton():
    task_tracker = TaskTracker()
    assert task_tracker.tasks == []

def test_task_tracker_add_task_number():
    with pytest.raises(TypeError) as e:
        tracker = TaskTracker()
        tracker.add_task(1)
    assert str(e.value) == "Task must be a string"

def test_task_tracker_add_task_list():
    with pytest.raises(TypeError) as e:
        tracker = TaskTracker()
        tracker.add_task([])
    assert str(e.value) == "Task must be a string"

def test_task_tracker_add_task_dict():
    with pytest.raises(TypeError) as e:
        tracker = TaskTracker()
        tracker.add_task({})
    assert str(e.value) == "Task must be a string"

def test_task_tracker_add_task_empty_string():
    with pytest.raises(ValueError) as e:
        tracker = TaskTracker()
        tracker.add_task("")
    assert str(e.value) == "Task must not be empty"

def test_task_tracker_add_task_space():
    with pytest.raises(ValueError) as e:
        tracker = TaskTracker()
        tracker.add_task(" ")
    assert str(e.value) == "Task must not be empty"

def test_task_tracker_add_task():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    assert tracker.tasks == ["Do the dishes"]

def test_task_tracker_add_task_multiple():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    tracker.add_task("Do the laundry")
    assert tracker.tasks == ["Do the dishes", "Do the laundry"]

def test_task_tracker_get_tasks():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    tracker.add_task("Do the laundry")
    assert tracker.get_tasks() == ["Do the dishes", "Do the laundry"]

def test_task_tracker_mark_complete_not_string():
    with pytest.raises(TypeError) as e:
        tracker = TaskTracker()
        tracker.mark_complete(1)
    assert str(e.value) == "Task must be a string"

def test_task_tracker_mark_complete_empty_string():
    with pytest.raises(ValueError) as e:
        tracker = TaskTracker()
        tracker.mark_complete("")
    assert str(e.value) == "Task must not be empty"

def test_task_tracker_mark_complete_space():
    with pytest.raises(ValueError) as e:
        tracker = TaskTracker()
        tracker.mark_complete(" ")
    assert str(e.value) == "Task must not be empty"

def test_task_tracker_task_doesnt_exist():
    with pytest.raises(ValueError) as e:
        tracker = TaskTracker()
        tracker.mark_complete("Do the dishes")
    assert str(e.value) == "Task not found"

def test_task_tracker_mark_complete():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    tracker.mark_complete("Do the dishes")
    assert tracker.tasks == []

def task_tracker_mark_complete_multiple():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    tracker.add_task("Do the laundry")
    tracker.mark_complete("Do the dishes")
    assert tracker.tasks == ["Do the laundry"]

def task_tracker_mark_complete_repeated():
    tracker = TaskTracker()
    tracker.add_task("Do the dishes")
    tracker.add_task("Do the dishes")
    tracker.mark_complete("Do the dishes")
    assert tracker.tasks == []