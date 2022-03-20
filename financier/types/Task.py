from datetime import datetime, timedelta
from typing import List
from Tags import Tags
from User import User


class Task(object):
    """
    A Task class

    Attributes:
        name: str
        due: datetime
        user: User
        estimated_time: timedelta
        tags: List[Tags]
        advanced_task: List[Task]
        subsequent_task: List[Task]
    """

    def __init__(self, name: str, due: datetime, user: User, estimated_time: timedelta = timedelta(minutes=30), tags: List[Tags] = [], advanced_task: List["Task"] = [], subsequent_task: List["Task"] = []):
        """
        init
        """
        if name is not str:
            raise TypeError("name is not str")
        self._name: str = name

        if due is not datetime:
            raise TypeError("due is not datetime")
        self._due: datetime = due

        if user is not User:
            raise TypeError("user is not User")
        self._user: User = user

        if estimated_time is not timedelta:
            raise TypeError("estimated_time is not timedelta")
        self._estimated_time: timedelta = estimated_time

        if tags is not List[Tags]:
            raise TypeError("tags is not List[Tags]")
        self._tags: List[Tags] = tags

        if advanced_task is not List[Task]:
            raise TypeError("advanced_task is not List[Task]")
        self._advanced_task: List[Task] = advanced_task

        if subsequent_task is not List[Task]:
            raise TypeError("subsequent_task is not List[Task]")
        self._subsequent_task: List[Task] = subsequent_task

    @property
    def name(self):
        """
        task name
        """
        return self._name

    @name.setter
    def name_setter(self, name: str):
        """
        set name
        """
        if name is not str:
            raise TypeError("the object is not str")
        self._name = name

    @property
    def due(self):
        """
        task due
        """
        return self._due

    @due.setter
    def due_setter(self, due: datetime):
        """
        set due
        """
        if due is not datetime:
            raise TypeError("the object is not datetime")
        self._due = due

    @property
    def estimated_time(self):
        """
        task estimated time
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time_setter(self, estimated_time: timedelta):
        """
        set estimated time
        """
        if estimated_time is not timedelta:
            raise TypeError("the object is not timedelta")
        self._estimated_time = estimated_time

    @property
    def tags(self):
        """
        task tags
        """
        return self._tags

    @tags.setter
    def tags_setter(self, tags: List[Tags]):
        """
        set tags
        """
        self._tags = tags

    @property
    def user(self):
        """
        task user
        """
        return self._user

    @user.setter
    def user_setter(self, user: User):
        """
        set user
        """
        self._user = user

    @property
    def advanced_task(self):
        """
        task advanced task
        """
        return self._advanced_task

    @advanced_task.setter
    def advanced_task_setter(self, advanced_task: list):
        """
        set advanced task
        """
        self._advanced_task = advanced_task

    @property
    def subsequent_task(self):
        """
        task subsequent task
        """
        return self._subsequent_task

    @subsequent_task.setter
    def subsequent_task_setter(self, subsequent_task: List["Task"]):
        """
        set subsequent task
        """
        if subsequent_task is not List[Task]:
            raise TypeError("the object is not List[Task]")
        self._subsequent_task = subsequent_task

    def __str__(self):
        """
        str
        """
        return f"{self._name}"

    def __repr__(self):
        """
        repr
        """
        return f"<Task {self._name}; until {self._due}; by {self._user}>"
