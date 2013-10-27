#!/usr/bin/env python
# coding=utf-8

from Tkinter import Tk
from Tkinter import Entry
from Tkinter import Label
from Tkinter import Button
from Tkinter import StringVar


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

        self.__querybutton = QueryButton(master=self, command=self.p)
        self.__querybutton.grid(
            ipadx=20, ipady=7, padx=10, pady=10, sticky=self.get_anchor_str('RIGHT_TOP'), row=0)
        self.__show_box_text = StringVar()
        self.__show_box = ShowWordLabel(
            master=self,  textvar=self.__show_box_text)
        self.__show_box.grid(ipadx=100, ipady=100, padx=20,
                             pady=30)

    def p(self):
        self.__show_box_text.set(self.__input.get())

    def get_anchor_str(self, locate_string):
        return self.__locate_dict[locate_string]


class TextWord(Entry):

    """docstring for TextWord"""
    __mask = None

    def __init__(self, main_window=None, command=None):
        Entry.__init__(self, master=main_window, validatecommand=command)

    def set_pass_word(self, mask):
        if not isinstance(mask , str):
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


if __name__ == '__main__':
    d = DictWindow()
    d.mainloop()
