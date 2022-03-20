from typing import List
from types.Task import Task


def sort_tasks(tasks: List[Task]) -> List[Task]:
    """
    sort tasks by due
    """
    return sorted(tasks, key=lambda task: task.due)


def asynchronous_task_scheduling(tasks: List[Task]) -> List[Task]:
    """
    For efficient task execution, asynchronous schedules are returned in List[Task] based on due date, expected time, and dependent tasks.
    """
