from Task import Task
from User import User
from datetime import datetime, timedelta
from typing import List, Tuple


class Schedule(object):
    """
    Class of schedule for the person in charge to perform the tasks during the period.

    Attributes:
        assigner: User
        during: Tuple[datetime, datetime]
    """

    def __init__(self, assigner: User, during: Tuple[datetime, datetime]):
        """
        init
        """

        if assigner is not User:
            raise TypeError("assigner is not User")
        self._assigner: User = assigner

        if during is not Tuple[datetime, datetime]:
            raise TypeError("during is not Tuple[datetime, datetime]")
        self._during: Tuple[datetime, datetime] = during

    @property
    def assigner(self):
        """
        returns schedule of assigner
        """
        return self._assigner

    @property
    def during(self):
        """
        returns schedule of during
        """
        return self._during

    def schedule_task(self, tasks: List[Task]) -> List[Task]:
        """
        schedule tasks during the schedule.
        If a task does not fit within the specified schedule, returns the tasks that do not fit in the schedule.

        Args:
            tasks: List[Task]

        Returns:
            List[Task]
        """
        # sort tasks by due, expected time, and dependent tasks
        sorted_task = sorted(tasks, key=lambda task: task.due)
        sorted_task = sorted(sorted_task, key=lambda task: task.estimated_time)
        sorted_task = sorted(
            sorted_task, key=lambda task: len(task.dependent_tasks))

        # allocate tasks
        allocated_tasks = []
        for task in sorted_task:
            if task.due <= self.during[1] and task.due >= self.during[0]:
                allocated_tasks.append(task)
            else:
                break

        return allocated_tasks
