#coding=utf-8




import gtk
 
import gtk
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("ZooDict")
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        button = gtk.Button("搜索")
        button.connect("clicked", self.button_action)
        button.set_visible(True)
        button.set_size_request(10,10)
        self.add(button)
    
   
 
        self.connect("destroy", gtk.main_quit)
 
        self.show()
    def button_action(self, widget, data=None):
        print 'hi%s' % data
 
    def main(self):
        gtk.main()
if __name__ == "__main__":
    p = PyApp()
    p.main()