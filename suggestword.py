#!/usr/bin/env python
# coding=utf-8
'''
功能：
    query_suggest_word
    变量：
        word -> 查询词
     从dict.cn获得建议词
    get_suggest_word 分析获得到的建议词 解析

'''

import utils
suggest_url = 'http://dict.cn/apis/suggestion.php?'


def query_suggest_word(word):
    query = {'callback': 'jQuery%s_%s' % (utils.randint(20), utils.timems()),
             'q': word,
             'dict': 'dict',
             's': 'dict'}
    _url = utils.queryurl(suggest_url, query)
    return utils.get_url_data(_url)


def get_suggest_word(word):
    return [i['g'] for i in utils.jsonstrtodict(utils.clear_data(query_suggest_word(word)).replace("&nbsp;", " "))['s']]

if __name__ == '__main__':
    for i in get_suggest_word("angel"):
        try:
            print i
        except Exception, e:
            print e
            continue
