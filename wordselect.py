#coding=utf-8




import threading
from multiprocessing import Pool
import time


class WordSelect(object):
    
    __instance = None
    __word = None
    __type = ""
    __change = False
    __lock = threading.Lock()
    
    
    @staticmethod
    def getInstance():
        if not WordSelect.__instance:
            WordSelect.__lock.acquire()
            if not WordSelect.__instance:
                WordSelect.__instance = object.__new__(WordSelect)
                object.__init__(WordSelect.__instance)
            WordSelect.__lock.release()
        return WordSelect.__instance
    
    def get_select_word(self):
        return self.__word
    
    def get_select_change(self):
        return self.__change
    
    def set_select_word(self,word):
        WordSelect.__lock.acquire()
        if word and  not word.strip() == '' and not self.__word == word:
            self.__word = word
            self.__change = True
        else:
            self.__change = False
        WordSelect.__lock.release()


class T(object):
    x = 9

    def  s(self):
        self.x = 10

    def p(self):
        print self.x
        print self.x
        print self.x
pool = Pool(1)

t = T()
pool.apply_async(t.s , callback = t.p )

while True:
    time.sleep(1)
    print t.p()
