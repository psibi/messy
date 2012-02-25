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
        self.window=builder.get_object("main_window")
        self.send_window=builder.get_object("send_window")
        self.mobno=builder.get_object("mobno_send")
        self.message=builder.get_object("message")
        self.username=builder.get_object("username")
        self.password=builder.get_object("password")
        self.msgtext=builder.get_object("msg")
        self.counter=0
        builder.connect_signals(self)
        
    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_login_button_clicked(self,widget,data=None):
        user=self.username.get_text()
        pword=self.password.get_text()
        self.sms.authenticate_site(user,pword)
        self.window.hide()
        self.send_window.show()

    def on_send_button_clicked(self,widget,data=None):
        if self.counter!=0:
            user=self.username.get_text()
            pword=self.password.get_text()
            self.sms.authenticate_site(user,pword)
        else:
            self.counter = self.counter + 1
            mobno = self.mobno.get_text()
            startiter, enditer = self.msgtext.get_bounds()
            text=self.msgtext.get_text(startiter,enditer,False)
            self.sms.send_sms(mobno,text)
            self.sms.logout()
            dlg=gtk.MessageDialog(self.window,gtk.DIALOG_DESTROY_WITH_PARENT,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,"Message Sent!")
            dlg.run()
            dlg.destroy()

    def on_send_window_destroy(self,widget,data=None):
        gtk.main_quit()

if __name__=="__main__":
    window=messy()
    gtk.main()
