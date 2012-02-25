#!/usr/bin/python
import mechanize
import cookielib
from time import sleep

br=mechanize.Browser()

class sms_client:
    """Basic class accessingg features of 160by2.com"""
    def __init__(self):
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        
    def authenticate_site(self,user,pword):
        br.open("http://www.160by2.com")
        br.select_form(nr=0)
        br.form['username']=user
        br.form['password']=pword
        br.submit()
        s = br.geturl()
        link = s.split("?")
        self.id = link[1]
        
    def open_sendpage(self):
        action="SendSMS"
        s = self.get_weburl(action)
        br.open(s)
        br.select_form(nr=0)

    def send_sms(self,mobile_no,msg):
        self.open_sendpage()
        action="SendSMSAction"
        s = self.get_weburl(action)
        br.form['mobile1']=mobile_no
        br.form['msg1']=msg
        br.form.action = s
        try:
            br.submit()
        except Exception:
            pass #ignore the response exception

    def logout(self):
        self.open_sendpage()
        action="Logout"
        s = self.get_weburl(action)
        br.form.action = s
        br.submit()
        print br.response().read()
  
    def get_weburl(self,action):
        weburl = "http://www.160by2.com/" + action + ".action?" + self.id
        return weburl
 
if __name__=="__main__":
    pass
    #client = sms_client()
    #client.authenticate_site('7200120343','xxx')
    #client.send_sms('9487847594',"Hello World)
    #client.logout()


