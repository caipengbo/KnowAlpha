# -*- UTF-8 -*-

from entity.query import Query
from entity.question import Question
from util import tokenizer


class Post:

    def __init__(self, question_obj, answer_obj_list=None):
        self.question_obj = question_obj
        self.answer_obj_list = answer_obj_list

    def calculate_title_relevance(self, query_obj):
        question_title_word_list = tokenizer.tokenize(self.question_obj.title)
        query_title_word_list = tokenizer.tokenize(query_obj.title)
        # lower
        question_title_word_list = [w.lower() for w in question_title_word_list]
        query_title_word_list = [w.lower() for w in query_title_word_list]

        question_num = len(question_title_word_list)
        query_num = len(query_title_word_list)

        if question_num < query_num:
            overlap = [value for value in question_title_word_list if value in query_title_word_list]
            ret = len(overlap) / question_num
        else:
            overlap = [value for value in query_title_word_list if value in question_title_word_list]
            ret = len(overlap) / query_num

        return ret

    def calculate_tf_idf(self, query_obj):
        return

if __name__ == '__main__':
    tag_list = ['<c++>', '<java>']
    query = Query("Query Title1 and title2", "", tag_list, "2019-5-16")
    question = Question("your title question title title", "", 2, 100, tag_list, "2019-5-16", "2019-5-26")

    p = Post(question)
    print(p.calculate_title_relevance(query))
