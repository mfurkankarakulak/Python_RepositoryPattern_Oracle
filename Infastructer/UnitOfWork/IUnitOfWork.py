# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:47:09 2019

@author: furkan.karakulak
"""
from abc import ABC, abstractmethod

class UnitOfWorkManager(ABC):
    """Gives access to a unit of work
        This class is required only to implement Start which returns a
        UnitOfWork.
        Implementors must ensure that there is only a single unit of work
        for a given request context, eg. a web request or command pipeline
    """

    def start(self):
        raise NotImplementedError("start")


class UnitOfWork(ABC):
    """Represents a single logical set of operations against a data-store
        This class is a context manager and represents a db transaction. Kinda.
        If the commit method is not called before the context ends, the
        transaction must be rolled back.
        If the rollback method is called at any time, the tx immediately rolls
        back.
        If an exception occurs, this class ensures that the tx is rolled back
        automatically.
        Repositories are exposed as properties on a unit of work.
        A UnitOfWork must guarantee that database reads and writes occur
        within the same transactional scope"""

    def __enter__(self):
        raise NotImplementedError("enter")

    def __exit__(self, type, value, traceback):
        raise NotImplementedError("exit")

    def commit(self):
        raise NotImplementedError("commit")

    def rollback(self):
        raise NotImplementedError("rollback")
