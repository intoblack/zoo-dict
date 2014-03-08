# coding=utf-8
#!/usr/bin/env python


import urllib2
import json
import urllib
# import os
from optparse import OptionParser
import sys
from subprocess import call  
# import commands
reload(sys)
sys.setdefaultencoding('utf-8')


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

    SUGGEST = 'http://dsuggest.ydstatic.com/suggest/suggest.s?keyfrom=dict.suggest'
    QUERY = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&'

    def query(self, word):
        QUERY_URL = self.QUERY + urllib.urlencode({'q': word})
        return self.__parser(word, urllib2.urlopen(QUERY_URL).read())

    def __parser(self, word, data):
        _dict_json = json.loads(data)
        if _dict_json.has_key('basic'):
            return WordMean(word, _dict_json['translation'][0], _dict_json['basic']['explains'], ['%s:%s' % (value['key'], ','.join([word for word in value['value']])) for value in _dict_json['web']])
        elif _dict_json.has_key('translation'):
            return WordMean(word, _dict_json['translation'][0])
        else:
            return None

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


class ConsleString(object):

    __strbuffer = []
    __fore_color = False
    __append = False

    def append_string(self, value):
        if self.__strbuffer and not self.__fore_color:
        	if self.__strbuffer[len(self.__strbuffer) - 1] != '1m' or  self.__strbuffer[len(self.__strbuffer) - 1] != '0m':
        		self.__strbuffer.append('1m')
        	self.__append = False
        	self.__strbuffer.append(value)
        return self

    def clear(self):
        if self.__strbuffer and len(self.__strbuffer) > 0:
            del self.__strbuffer[:]
            self.__append = False
            self.__fore_color = False

    def __getattr__(self, key):
        if not self.__strbuffer:
            self.__strbuffer = list()
        if len(self.__strbuffer) == 0 or not self.__append:
            self.__strbuffer.append('\e[')
            self.__append = True
        self.__color(key, 'black', 30, 40)
        self.__color(key, 'red', 31, 41)
        self.__color(key, 'green', 32, 42)
        self.__color(key, 'yellow', 33, 43)
        self.__color(key, 'blue', 34, 44)
        self.__color(key, 'purple', 35, 45)
        self.__color(key, 'darkgreen', 36, 46)
        self.__color(key, 'white', 37, 47)
        if key == 'consle':
        	self.__strbuffer.append('\e[0m')
        if key == 'hg':
            self.__strbuffer.append('1m')
        if key == 'low':
            self.__strbuffer.append('0m')
        return self

    def __color(self, key, color, fore_gruod, back_ground):
        if key == color:
            if not self.__fore_color:
                self.__strbuffer.append('%d;' % fore_gruod)
                self.__fore_color = True
            else:
                self.__strbuffer.append('%d;' % back_ground)
                self.__fore_color = False

    def __str__(self):
        if self.__strbuffer and isinstance(self.__strbuffer, list):
            if len(self.__strbuffer) > 0 and self.__strbuffer[len(self.__strbuffer) - 1] != '\e[0m':
                self.__strbuffer.append('\e[0m')
            return ''.join(self.__strbuffer)
        else:
            return ''

def consle_show(word):
	call(['echo' , '-e' , '%s' % word])

def consle_clear():
	call(['clear'])


if __name__ == '__main__':
    opts = OptionParser()
    opts.add_option('-t', '--translte', dest='translate' , action = 'store_false',  help='chose function to find word meaning' , default = True)
    opts.add_option('-s', '--suggest', dest='suggest' , action = 'store_true',  help='chose function to find word suggestion' , default = False)
    opts.add_option('-w' , '--word' , dest = 'word' , help = 'find and suggest word ')
    (options,args) = opts.parse_args(sys.argv)
    if options.word:
    	yd = YouDao()
    	consle_string = ConsleString()
    	if options.suggest:
    		print yd.suggestword(options.word)
    	elif options.translate:
    		consle_clear()
    		word_mean = yd.query(options.word)
    		consle_show(consle_string.red.black.append_string('单词 :').green.black.append_string(word_mean.word))
    		consle_string.clear()
    		consle_show(consle_string.red.black.append_string('翻译 :').green.black.append_string(word_mean.translation))
    		consle_string.clear()
    		consle_show(consle_string.red.black.append_string('单词释义 :').green.black.append_string(word_mean.meaning))
    		consle_string.clear()
    		consle_show(consle_string.red.black.append_string('例子 :').green.black.append_string(word_mean.example))


