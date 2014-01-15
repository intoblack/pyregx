#!/usr/bin/env python
# coding=utf-8


import regdict
import re


class PyRe(object):

    def __init__(self, pattern):
        self.__pattern = pattern
        self.__start_pattern = self.__pattern
        self.__end_pattern = self.__pattern
        self.__equal_pattern = self.__pattern

        if not pattern.startswith('^'):
            self.__start_pattern = '^%s' % self.__pattern
            self.__equal_pattern = '^%s' % self.__pattern
        if not pattern.endswith('$'):
            self.__end_pattern = '%s$' % self.__pattern
            self.__equal_pattern = '%s$' % self.__pattern
        self.__start_compile = re.compile(self.__start_pattern)
        self.__compile = re.compile(pattern)
        self.__end_compile = re.compile(self.__end_pattern)
        self.__equal_compile = re.compile(self.__equal_pattern)

    def equal(self, data):
        if self.__equal_compile.match(data):
            return True
        return False

    def start_with(self, data):
        if self.__start_compile.match(data):
            return True
        else:
            return False

    def end_with(self, data):
        if self.__end_compile.match(data):
            return True
        else:
            return False

    def __eq__(self, data):
        if data and isinstance(data, (str, unicode)):
            if self.equal(data):
                return True
            return False
        else:
            raise TypeError, 'data must be str or unicode!'

    def __ne__(self, data):
        return not self.__eq__(data)

    # 数据中包含正则表达式数据
    # 如果有数据符合正则
    # 返回 True
    #
    def contain(self, data):
        if self.__compile.search(data):
            return True
        else:
            return False

    def find_all(self, data, callable=None):
        return self.__compile.findall(data)

    def find_iter(self, data, callable=None):
        find_data = []
        find_data.extend([match.group()
                         for match in self.__compile.finditer(data)])
        return find_data


class PPattern(object):

    __pattern_dict = {}

    def __setattr__(self, key, value):
        if key and value and isinstance(key, (str)) and isinstance(value, (PyRe)):
            if not self.__pattern_dict.has_key(key):
                self.__pattern_dict[key] = value
        else:
            raise TypeError, 'key must string and value is PyRe'

    def __getattr__(self, key):
        if isinstance(key, (str)):
            if not self.__pattern_dict.has_key(key):
                if regdict.regx_dict.has_key(key.upper()):
                    self.__pattern_dict[key] = PyRe(
                        regdict.regx_dict[key.upper()])
                else:
                    raise NotImplementedError, 'regx_dict 没有正则'
            return self.__pattern_dict[key]
        raise TypeError, 'key must be sting '

    def __delattr__(self, key):
        if key and isinstance(key, str):
            if self.__pattern_dict.has_key(key):
                del self.__pattern_dict[key]
        else:
            raise TypeError, 'key must be string'


if __name__ == "__main__":

    p = PPattern()
    print p.IP != '123.145.23.45'
    del p.IP
    print p.mail.find_iter('xxx1212@126.com')
    print p.html_tag.find_iter("<html xx=11>")
    print p.date  == '2013/12/05'
    print 'xx'.replace('x', 'y')
