# -*- UTF-8 -*-
from util import tokenizer


class Question:

    def __init__(self, title, body, comment_count, score, tag_list, created_date, last_date):
        self.title = title
        self.body = body
        self.comment_count = comment_count
        self.score = score
        self.tag_list = tag_list
        self.created_date = created_date
        self.last_date = last_date




