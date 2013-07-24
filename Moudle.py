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
    
    _tran = {'e' : 'mean',
             'g':'word'}
    
    def __init__(self,word='',meaning=''):
        self.word = word
        self.mean = meaning
    
    def initWithDict(self, datadict):
        for _key, _value in datadict.items():
            setattr(self, self._tran[_key], _value)
    
    
    def toString(self):
        return '%(word)s\t%(mean)s' % self.__dict__ 
        