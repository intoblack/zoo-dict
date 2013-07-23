#coding=utf-8




import gtk
import time
import threading



class WordSelect(object):
    
    __word = None
    __type = ""
    __change = False
    __lock = threading.Lock
    
    
    @staticmethod
    def getInstance():
        if not WordSelect.__instance:
            WordSelect.__lock.acquire()
            if not WordSelect.__instance:
                WordSelect.__instance = object.__new__(WordSelect)
                object.__init__(WordSelect.__instance)
            WordSelect.__lock.release()
        return WordSelect.__instance
    
    def get_select_Word(self):
        return self.__word
    
    def set_select_word(self,word):
        WordSelect.__lock.acquire()
        if not word and not word.strip() == '' and not self.__word == word:
            self.__word = word
            self.__change = True
        else:
            self.__change = False
        WordSelect.__lock.release()
        
        
        
clipboard = gtk.clipboard_get()

while True:
    t = clipboard.wait_for_text()
    time.sleep(1)
    print t   