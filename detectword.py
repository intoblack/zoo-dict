# coding=utf-8


import threading
import gtk
import time
import util
from webdict import Dict


class DetectClboard(threading.Thread):

    __clipboard = None
    __alive = True
    __timedelay = 1

    def __init__(self, timedelay=1):
        threading.Thread.__init__(self)
        self.__clipboard = gtk.clipboard_get()
        self.__timedelay = timedelay

    def setAlive(self, alive=True):
        self.__alive = alive

    def killDetect(self):
        self.setAlive(False)

    def run(self):

        while self.__alive:
            time.sleep(self.__timedelay)
            _word = self.__clipboard.wait_for_text()
            print _word


class MonitorClip(object):
    __old = ''
    __suggestwords = []
    def __init__(self):
        self.clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
        self.clip.connect("owner-change", self._clipboard_changed)
        self.suggest = Dict()

    def _clipboard_changed(self, clipboard, event):
        text = clipboard.wait_for_text()
        text = text.encode("utf-8")
        print text
        if not text == self.__old:
            self.__old = text
            util.cls()
            del self.__suggestwords
            self.__suggestwords = [ word for word in self.suggest.suggestword(text)]
            print self.__suggestwords
                


if __name__ == "__main__":
    m = MonitorClip()
    gtk.mainloop()
