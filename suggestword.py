#coding=utf-8


import utils
from  Moudle import wordlabel
suggest_url = 'http://dict.cn/apis/suggestion.php?'

def query_suggest_word(word):
    query = {'callback':'jQuery%s_%s' % (utils.randint(20),utils.timems()),
             'q':word,
             'dict':'dict',
             's':'dict'}
    _url = utils.queryurl(suggest_url, query)
    return utils.get_url_data(_url)


def get_suggest_word(word):
    wordlist = []
    for i in utils.jsonstrtodict(utils.clear_data(query_suggest_word(word)).replace("&nbsp;", " "))['s']:
        w = wordlabel()
        w.initWithDict(i)
        wordlist.append(w)
    return wordlist


for i in get_suggest_word("angel"):
    print i.toString()
