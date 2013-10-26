#!/usr/bin/env python
# coding=utf-8

from Tkinter import Tk
from Tkinter import Entry
from Tkinter import LEFT, TOP
from Tkinter import RIGHT
from Tkinter import Button


class DictWindow(Tk):

    """词典主窗口 基于tk"""

    __locate_dict = {
        'TOP': "n", 'BOTTOM': "s", 'LEFT': "w", 'RIGHT': "e", 'LEFT_TOP': "nw",
        'LEFT_BOTTOM': "sw", 'RIGHT_BOTTOM': "se", 'RIGHT_TOP': "ne", 'CENTER': "center"}



    def __init__(self):
        Tk.__init__(self)
        self.title('Zoo-Dict')
        self.geometry('600x400')
        self.__input = TextWord(main_window=self)
        self.__input.pack(
            padx=10, pady=10, anchor=self.get_anchor_str('RIGHT_TOP'), ipadx=100, ipady=10)
        self.__querybutton = QueryButton(master=self, command=self.p)
        self.__querybutton.pack(
            expand=False, ipadx=10, ipady=30, padx=60, pady=60)

    def p(self):
        print self.__input.get()


    def get_anchor_str(self,locate_string):
        return self.__locate_dict[locate_string]



class TextWord(Entry):

    """docstring for TextWord"""

    def __init__(self, main_window=None, command=None):
        Entry.__init__(self, master=main_window, validatecommand=command)


class QueryButton(Button):

    def __init(self, master=None, command=None, width=30, height=60):
        Button.__init__(
            self, master=master, command=command, width=width, height=height)


if __name__ == '__main__':
    d = DictWindow()
    d.mainloop()
