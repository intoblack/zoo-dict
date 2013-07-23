#coding=utf-8




import gtk
import time



clipboard = gtk.clipboard_get()

while True:
    t = clipboard.wait_for_text()
    time.sleep(1)
    print t   