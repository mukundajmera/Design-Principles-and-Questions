from answer import Answer
from models.comment import Comment
from question import Question


class User:

    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []

    def ask_questions(self, title, content, tags):
        question = Question(self, title, content, tags)
        self.questions.append(question)
        self.update_reputation(5)
        return question

    def update_reputation(self, reputation):
        self.reputation += reputation
        self.reputation = max(0, self.reputation)

    def answer_question(self, question: Question, content):
        answer = Answer(self, question, content)
        self.answers.append(answer)
        question.add_answer(answer)
        self.update_reputation(10)
        return answer

    def comment_on(self, commentable: Question, content):
        comment = Comment(self, content)
        self.comments.append(comment)
        commentable.add_comment(comment)
        self.update_reputation(2)
        return comment
