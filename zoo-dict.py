#!/usr/bin/env python
# coding=utf-8

from Tkinter import Tk
from Tkinter import Entry
from Tkinter import Label
from Tkinter import Button
# from Tkinter import StringVar
from Tkinter import Text
from webdict import YouDao
from Tkinter import END
# from threading import Thread
from Tkinter import NORMAL


class DictWindow(Tk):

    """词典主窗口 基于tk
    pack


    ipadx = width
    ipady = height
    padx = the distance which x to top
    pady = the distance which y to top
    anchor = widget locate in the window
    side =  simple anchor

    """

    __locate_dict = {
        'TOP': "n", 'BOTTOM': "s", 'LEFT': "w", 'RIGHT': "e", 'LEFT_TOP': "nw",
        'LEFT_BOTTOM': "sw", 'RIGHT_BOTTOM': "se", 'RIGHT_TOP': "ne", 'CENTER': "center"}

    def __init__(self):
        Tk.__init__(self)
        self.title('Zoo-Dict')
        self.geometry('600x400')
        self.__input = TextWord(main_window=self)
        self.__input.grid(
            padx=10, pady=10, sticky=self.get_anchor_str('LEFT_TOP'), ipadx=100, ipady=10)

        self.__querybutton = QueryButton(
            master=self, command=self.key_word_search)
        self.__querybutton.grid(
            ipadx=20, ipady=7, padx=10, pady=10, sticky=self.get_anchor_str('RIGHT_TOP'), row=0)
        # self.__show_box_text = StringVar()
        self.__show_text = ShowText(self )
        self.__show_text.grid(ipadx=1, ipady=1, row=1)
        self.__show_text.tag_config('keyword', foreground='red')
        self.__show_text.tag_config('translation', foreground='green')
        self.__show_text.tag_config('meaning', foreground='blue')
        self.__web_dict = YouDao()

        
        # self.__show_box = ShowWordLabel(
        #     master=self,  textvar=self.__show_box_text)
        # self.__show_box.grid(ipadx=100, ipady=100, padx=20,
        #                      pady=30)

    def key_word_search(self):
        
        __word = self.__input.get()
        self.__show_text.clear_all()
        if not __word or __word.strip() == '':
            return
        _ws = self.__web_dict.query(self.__input.get())
        self.__show_text.insert(1.0, _ws.word + '\n\n', 'keyword')
        self.__show_text.insert(3.0, _ws.translation + '\n\n', 'translation')
        __meaning_point = float(3.0 + len(_ws.meaning.split('\n')))
        self.__show_text.insert(__meaning_point, _ws.meaning + '\n\n', 'meaning')
        self.__show_text.insert(__meaning_point + 5.0, _ws.example, 'meaning')
        

    def get_anchor_str(self, locate_string):
        return self.__locate_dict[locate_string]


class TextWord(Entry):

    """docstring for TextWord"""
    __mask = None

    def __init__(self, main_window=None, command=None):
        Entry.__init__(self, master=main_window, validatecommand=command)

    def set_pass_word(self, mask):
        if not isinstance(mask, str):
            return
        self.__mask = mask
        self['show'] = mask

    def set_read_only(self):
        self['state'] = 'readonly'


class QueryButton(Button):

    def __init__(self, master=None, command=None):
        Button.__init__(
            self, master=master, command=command)


class ShowWordLabel(Label):

    def __init__(self, master=None, command=None, labeltext='example', textvar=None):
        Label.__init__(
            self, master=master, command=command, text=labeltext, textvariable=textvar)

    def get(self):
        return self.__text

    def set(self, text):
        if isinstance(text, str) or isinstance(text, unicode):
            self.__text = text


class ShowText(Text):

    """docstring for ShowText"""

    def __init__(self, master=None):
        Text.__init__(self, master=master , state = NORMAL)

    def clear_all(self):
        self.delete(1.0 , END)

    

if __name__ == '__main__':
    d = DictWindow()
    d.mainloop()
