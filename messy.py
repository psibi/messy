#!/usr/bin/python
import gtk
import pygtk
from client import sms_client
class messy:
    def __init__(self):
        gladefile="messy.xml"
        builder=gtk.Builder()
        self.sms = sms_client()
        builder.add_from_file(gladefile)
        self.window=builder.get_object("mainwindow")
        self.send_window=builder.get_object("send_window")
        self.mobno=builder.get_object("mobno_send")
        self.message=builder.get_object("message")
        self.username=builder.get_object("username")
        self.password=builder.get_object("password")
        builder.connect_signals(self)
        
    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_login_button_clicked(self,widget,data=None):
        self.user=self.username.get_text()
        self.pword=self.password.get_text()
        self.sms.authenticate_site(self.user,self.pword)
        self.window.hide()
        self.send_window.show()

    def on_send_button_clicked(self,widget,data=None):
        self.mob = self.mobno.get_text()
        
    

if __name__=="__main__":
    window=messy()
    gtk.main()
