class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    # 对于set_score(self, score)我们可以借由set方法顺便做参数检查，提高代码安全性
    def set_safe_score(self, score):
        if score >= 0 and score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')