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
        print self.__end_pattern
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


if __name__ == "__main__":
    p = PyRe(regdict.regx_dict['CLEAR_NUM'])
    print p.find_all('+12 ,-12')
