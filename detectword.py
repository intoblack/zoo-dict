#coding=utf-8


import threading
import gtk
import time
import utils
from suggestword import get_suggest_word

class DetectClboard(threading.Thread):
    
    __clipboard = None 
    __alive = True
    __timedelay = 1
    def __init__(self ,timedelay = 1):
        threading.Thread.__init__(self)
        self.__clipboard = gtk.clipboard_get()
        self.__timedelay = timedelay
    
    def setAlive(self,alive=True):
        self.__alive = alive
    
    def killDetect(self):
        self.setAlive(False)
    
    
    def run(self):
        
        while self.__alive:
            time.sleep(self.__timedelay)
            _word = self.__clipboard.wait_for_text()
            print _word


class MonitorClip(object):
    _old = ''
    
    def __init__(self):
        #self.clip = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
        self.clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
        self.clip.connect("owner-change", self._clipboard_changed)


    def _clipboard_changed(self,clipboard, event):
        text = clipboard.wait_for_text()
        text = text.encode("utf-8")
        if not text == self._old:
            self._old = text
            utils.cls()
            for word in get_suggest_word(text):
                print word.toString()
            
        
    
    
if __name__ == "__main__":
    m = DetectClboard()
    m.start()
    
        