#!/usr/bin/env  python
# coding=utf-8


import util
import json
import urllib
from BeautifulSoup import BeautifulSoup


class WordMean():

    word = ''
    translation = ''
    meaning = []

    def __init__(self, word='', translation='', meaning=[], examples=[]):
        self.word = word.encode('utf-8')
        self.translation = translation.encode('utf-8')
        self.meaning = '\n'.join([mean.encode('utf-8') for mean in meaning])
        self.example = '\n'.join([sen.encode('utf-8') for sen in examples])

    def __str__(self):
        # meaning_str =
        return 'word : %s \n translation : %s\n meaning : %s\n example : %s ' % (self.word, self.translation, self.meaning, self.example)


class WebDIct(object):
    # query
    #    参数 ： word 查询词
    #    返回 ： WordMean
    # 异常 : 没有 basic

    def query(self, word):
        pass

    def audio(self, word):
        pass

    def suggestword(self, word):
        pass


class YouDao(WebDIct):

    """docstring for YouDao"""
    SUGGEST = 'http://dsuggest.ydstatic.com/suggest/suggest.s?keyfrom=dict.suggest'
    QUERY = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&q='

    def query(self, word):
        QUERY_URL = self.QUERY + word
        return self.__parser(word, util.get_response_with_useragent(QUERY_URL).read())

    def __parser(self, word, data):
        _dict_json = json.loads(data)
        print _dict_json
        if not _dict_json.has_key('translation'):
            return None
        return WordMean(word, _dict_json['translation'][0], _dict_json['basic']['explains'], ['%s:%s' % (value['key'], ','.join([word for word in value['value']])) for value in _dict_json['web']])

    def suggestword(self, word):
        __data = util.get_response_with_useragent(
            self.SUGGEST + '&query=' + word).read()
        suggest_list = None
        if __data:
            __data = __data.strip()
            __html = __data[__data.index('l(') + 3:-3]
            __html = urllib.unquote(__html.decode('utf-8'))
            soup = BeautifulSoup(__html)
            suggest_list = [__sugest.string for __sugest in soup.findAll(
                'td', attrs={'class': 'remindtt75'})]
        return suggest_list


class Baidu(WebDIct):

    QUERY = 'http://fanyi.baidu.com/transapi/'


class Dict(WebDIct):
    SUGGEST = 'http://dict.cn/apis/suggestion.php?'

    def suggestword(self, word):
        query = {'callback': 'jQuery%s_%s' % (util.randint(20), util.timems()),
                 'q': word,
                 'dict': 'dict',
                 's': 'dict'}
        __data = util.get_url_html_string(self.SUGGEST, query)
        print __data
        return [i['g'] for i in util.jsonstrtodict(util.getjson(__data).replace("&nbsp;", " "))['s']]


if __name__ == '__main__':
    u = Dict()
    print u.suggestword('angel')
