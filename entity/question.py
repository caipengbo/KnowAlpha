# -*- UTF-8 -*-
import json

from util.preprocessor import PreprocessPostContent


class Question:

    def __init__(self, title, body, comment_count, score, tag_list, created_date):
        self.title = title
        self.body = body
        self.comment_count = comment_count
        self.score = score
        self.tag_list = tag_list
        self.created_date = created_date

    def to_dict(self):
        dic = {'title': self.title, 'body': self.body, 'comment_count': self.comment_count, 'score': self.score,
               'tag_list': self.tag_list, 'created_date': self.created_date}
        return dic

    def parse_body(self):
        processor = PreprocessPostContent()
        body_para_list = processor.getProcessedParagraphs(self.body)
        body = " ".join(body_para_list)
        return body


