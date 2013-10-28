#!/usr/bin/env  python
# coding=utf-8


import util
import json


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

    def query(self, word):
        pass

    def audio(self, word):
        pass

    def suggestword(self, word):
        pass


class YouDao(WebDIct):

    """docstring for YouDao"""

    QUERY = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&q='

    def query(self, word):
        QUERY_URL = self.QUERY + word
        return self.__parser(word, util.get_response_with_useragent(QUERY_URL).read())

    def __parser(self, word, data):
        print data
        _dict_json = json.loads(data)

        return WordMean(word, _dict_json['translation'][0], _dict_json['basic']['explains'], ['%s:%s' % (value['key'], ','.join([word for word in value['value']])) for value in _dict_json['web']])


class Baidu(WebDIct):

    QUERY = 'http://fanyi.baidu.com/transapi/'


if __name__ == '__main__':
    u = YouDao()
    print u.query('help')
