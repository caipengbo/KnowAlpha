# -*- UTF-8 -*-


class Answer:

    def __init__(self, body, created_date, last_date, score=0, comment_count=0):
        self.body = body
        self.score = score
        self.comment_count = comment_count
        self.created_date = created_date
        self.last_date = last_date

