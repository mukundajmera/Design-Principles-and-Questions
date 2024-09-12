show_expected_result = False
show_hints = False


class XML:
    """XML processor"""

    def __init__(self):
        self.name = "XML"

    def process_XML(self):
        return "processing XML"


class JSON:
    """JSON processor"""

    def __init__(self):
        self.name = "JSON"

    #Note the different method name here!
    def process_JSON(self):
        return "processing JSON"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        #Add a new dictionary item that establishes the mapping between the generic method name: process() and the concrete method
        #For example, process() will be translated to process_XML() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)


def create_adapter(objects):
    # Your code goes here
    for obj in objects:
        if obj.name == "XML":
            return obj.process()

"""
objects = []

xml = Answer.XML()
json = Answer.JSON()

objects.append(Answer.Adapter(xml,process=xml.process_XML))
objects.append(Answer.Adapter(json,process=json.process_JSON))

result = Answer.create_adapter(objects)

"""