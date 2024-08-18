from typing import Dict

from answer import Answer
from models.tag import Tag
from question import Question
from user import User


class StackOverflow:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.questions: Dict[str, Question] = {}
        self.answers: Dict[str, Answer] = {}
        self.tags: Dict[str, Tag] = {}

    def create_user(self, name: str, email: str) -> User:
        user_id = len(self.users) + 1
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def ask_question(self, user: User, title, content, tags) -> Question:
        question = user.ask_questions(title, content, tags)
        self.questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question

    def answer_question(self, user, question, content):
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer

    def add_comment(self, user: User, commentable, content):
        return user.comment_on(commentable, content)

    def vote_question(self, user, question: Question, value):
        question.vote(user, value)

    def vote_answer(self, user, answer: Answer, value):
        answer.vote(user, value)

    def accept_answer(self, answer: Answer):
        answer.accept()

    def search_questions(self, query):
        """
        check on title, content, tags
        :param query:
        :return: list of questions for search result
        """
        return [q for q in self.questions.values() if
                query.lower() in q.title.lower() or
                query.lower() in q.content.lower() or
                any(query.lower() == tag.name.lower() for tag in q.tags)]

    def get_questions_by_user(self, user: User):
        return user.questions

    def get_user(self, user_id) -> User:
        return self.users.get(user_id)

    def get_question(self, question_id) -> Question:
        return self.questions.get(question_id)

    def get_answer(self, answer_id) -> Answer:
        return self.answers.get(answer_id)

    def get_tag(self, name: str) -> Tag:
        return self.tags.get(name)
