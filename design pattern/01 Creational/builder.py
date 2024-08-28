class Course:

    def __init__(self):
        self.fee_structure()
        self.batch_availibility()

    def fee_structure(self):
        raise NotImplementedError

    def batch_availibility(self):
        raise NotImplementedError

    def __repr__(self):
        return 'fee_structure : {0.fee_structure} | Batches Available : {0.batches}'.format(self)


# concrete course
class Python(Course):

    # Class for Python

    def fee_structure(self):
        self.fee_structure = 8000

    def batch_availibility(self):
        self.batches = 5

    def __str__(self):
        return "Python"

    # concrete course


class Swift(Course):

    # Class for swift programming

    def fee_structure(self):
        self.fee_structure = 10000

    def batch_availibility(self):
        self.batches = 4

    def __str__(self):
        return "Swift"

    # concrete course


class Java(Course):

    # Class for Java programming

    def fee_structure(self):
        self.fee_structure = 5000

    def batch_availibility(self):
        self.batches = 7

    def __str__(self):
        return "Java"

    # Complex Course class


class ComplexCourse:

    def __repr__(self):
        return 'fee_structure : {0.fee_structure} | batch_availibility: {0.batches}'.format(self)

    # Complex course class


class Complexcourse(ComplexCourse):

    def fee_structure(self):
        self.fee_structure = 7000

    def batch_availibility(self):
        self.batches = 6

    # construct course


def construct_course(cls):
    course = cls()
    course.fee_structure()
    course.batch_availibility()

    return course  # return the course object


# main method
if __name__ == "__main__":
    P = Python()  # object for Python course
    S = Swift()  # object for Swift course
    J = Java()  # object for Java course

    complex_course = construct_course(Complexcourse)
    print(complex_course)
