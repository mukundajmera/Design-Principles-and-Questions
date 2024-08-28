from abc import ABCMeta, abstractmethod
import copy


# class - courses at the institute
class Courses_JTP(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)

    # concrete course


class Python(Courses_JTP):
    # Class for Data Structures and Algorithms"""
    def __init__(self):
        super().__init__()
        self.type = "Python Basic and Algorithm"

    def course(self):
        print(" Inside Python :: course() method ")


# concrete course
class Java(Courses_JTP):
    # Class for Java langauge"""
    def __init__(self):
        super().__init__()
        self.type = "Java Basics and Spring Boot"

    def course(self):
        print(" Inside Python :: course() method. ")

    # concrete course


class R(Courses_JTP):
    # Class for R langauge"""
    def __init__(self):
        super().__init__()
        self.type = "R programming language"

    def course(self):
        print(" Inside Python :: course() method. ")

    # class - Courses At GeeksforGeeks Cache


class Courses_Cache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = Courses_Cache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        python = Python()
        python.set_id("1")
        Courses_Cache.cache[python.get_id()] = python

        java = Java()
        java.set_id("2")
        Courses_Cache.cache[java.get_id()] = java

        r = R()
        r.set_id("3")
        Courses_Cache.cache[r.get_id()] = r

    # main function


if __name__ == '__main__':
    Courses_Cache.load()

    Python = Courses_Cache.get_course("1")
    print(Python.get_type())

    Java = Courses_Cache.get_course("2")
    print(Java.get_type())

    R = Courses_Cache.get_course("3")
    print(R.get_type())
