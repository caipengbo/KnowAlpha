# -*- UTF-8 -*-
import json

from util.preprocessor import PreprocessPostContent


class Answer:

    def __init__(self, body, created_date, score=0, comment_count=0):
        self.body = body
        self.score = score
        self.comment_count = comment_count
        self.created_date = created_date

    def to_dict(self):
        dic = {'body': self.body, 'score': self.score, 'comment_count': self.comment_count,
               'created_date': self.created_date}
        return dic

    def parse_body(self):
        processor = PreprocessPostContent()
        body_para_list = processor.getProcessedParagraphs(self.body)
        body = " ".join(body_para_list)
        return body


if __name__ == '__main__':
    ans = Answer("body1", "2018-08-09", 55, 21)
    s = ans.toJSON()
    print(s)
