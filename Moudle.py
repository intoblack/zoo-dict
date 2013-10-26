#!/usr/bin/env python
# coding=utf-8


class Moudle:
    __dict__ = {}

    def __setattr__(self, attr, val):
        self.__dict__[attr] = val

    def toDict(self):
        return self.__dict__

    def initWithDict(self, datadict):
        for _key, _value in datadict.items():
            setattr(self, _key, _value)

    def toString(self):
        restr = ''
        for _key, _value in self.__dict__.items():
            infostr = '%s,%s\n' % (_key, _value)
            restr = restr + infostr
        return restr


class wordlabel(Moudle):

    __tran = {'e': 'mean',
              'g': 'word'}
    word = None
    mean = None
    def __init__(self, word='', meaning=''):
        self.word = word.encode("utf-8")
        self.mean = meaning.encode("utf-8")

    def initWithDict(self, datadict):
        for _key, _value in datadict.items():
            setattr(self, self.__tran[_key], _value)

    def __str__(self):
        return '%s : %s ' % (self.word, self.mean)
