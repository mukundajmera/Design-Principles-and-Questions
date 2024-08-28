class ExmapleSingleton:
    __instance__ = None

    def __init__(self):

        if ExmapleSingleton.__instance__ is None:
            ExmapleSingleton.__instance__ = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not ExmapleSingleton.__instance__:
            ExmapleSingleton()
        return ExmapleSingleton.__instance__


if __name__ == "__main__":
    # Creating an object of above defined class.
    example = ExmapleSingleton()
    print(example)

    #ideal use directly get_instance
    same_example = ExmapleSingleton.get_instance()
    print(same_example)

    another_example = ExmapleSingleton.get_instance()
    print(another_example)

    new_example = ExmapleSingleton()
    print(new_example)
