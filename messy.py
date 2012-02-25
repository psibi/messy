#!/usr/bin/python
import gtk
import pygtk

class messy:
    def __init__(self):
        gladefile="messy.xml"
        builder=gtk.Builder()
        builder.add_from_file(gladefile)
        self.window=builder.get_object("mainwindow")
        builder.connect_signals(self)
        
    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()

if __name__=="__main__":
    window=messy()
    gtk.main()
