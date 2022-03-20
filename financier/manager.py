from types.Task import Task
from typing import List


class Manager(object):
    """
    manager of tasks
    """

    def __init__(self):
        self._tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        docstring
        """
        self._tasks.append(task)

    def get_tasks(self):
        """
        docstring
        """
        return self._tasks
