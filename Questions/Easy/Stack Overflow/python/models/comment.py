from datetime import datetime


class Comment:
    def __init__(self, author, content):
        self.id = id(self)
        self.author = author
        self.content = content
        self.created_at = datetime.now()
