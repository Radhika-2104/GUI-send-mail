from tkinter import *
from validate_email import validate_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mymail(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
         
    def initUI(self):
        
        self.parent.title("MAIL SERVICE")
        self.pack(fill=BOTH, expand=True)
        
        frame2 = Frame(self)
        frame2.pack(fill=X)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        frame4 = Frame(self)
        frame4.place(x=5,y=100)
        
        frame5 = Frame(self)
        frame5.place(x=240,y=430)   
        
        def callback(event,fr):
            
            labele1=Label(fr,text="Enter valid email")
            to=event.widget.get()
            is_valid = validate_email(to)
            
            if not is_valid and to:
            
                labele1.place(x=89,y=44,anchor=W)
            if is_valid :
             
                labele1.place(x=89,y=44,anchor=W)
                labele1.config(text='',width=20)
                    
        label = Label(frame2, text="To :", width=9,font = "Verdana 10 bold")
        label.pack(side=LEFT)

        lsmail2=StringVar()
     
        lsmailDir2=label
        lsmailDir2.pack(side="left")

        string2=StringVar(None)
        smail2=Entry(frame2,textvariable=string2,width=65)
        
        smail2.bind("<Return>", lambda event: callback(event,frame2))
              
        smail2.pack(side="left",fill=X,padx=5,pady=15)
     
        label = Label(frame3, text="Subject :", width=9,font = "Verdana 10 bold")
        label.pack(side=LEFT)

        lsmail3=StringVar()
     
        lsmailDir3=label
        lsmailDir3.pack(side="left")

        string=StringVar(None)
        smail3=Entry(frame3,textvariable=string,width=65)
        smail3.pack(side="left",fill=X,padx=5,pady=10)
      
        label = Label(frame4, text="Message :", width=9,font = "Verdana 10 bold")
        label.pack(side=LEFT)
        
        def sendmail():
            html=False
            to_addr=string2.get()
            if not validate_email(to_addr):
                labele1=Label(frame2,text="Enter valid email")
                labele1.place(x=89,y=44,anchor=W)
                return
            
            subject=string.get()
            body=smail4.get("1.0","end-1c")
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            #create header part of mail
            msg = MIMEMultipart()
            username='' ################# Add your Gmail email ID ############
            
            password='' ################## Add password ####################
          
            msg['From'] = username
            msg['To'] = to_addr
            msg['Subject'] = subject
            if html:
              msg.attach(MIMEText(body, 'html'))
            else:
              msg.attach(MIMEText(body, 'plain'))

            #Next, log in to the server
            server.starttls()
            server.login(username,password)
            #Send the mail
            mail = msg.as_string() # The /n separates the message from the headers
            server.sendmail(username, to_addr, mail)
       
        smail4=Text(frame4,width=49,height=20)
        
        smail4.pack(side="left",fill=X)
        
        button=Button(frame5,height=1,width=10,text="send",command=lambda:sendmail())
        button.pack()
       
        
def main():
  
    root = Tk()
    root.geometry("550x500")
    root.resizable(width=False, height=False)
    app = mymail(root)
    root.mainloop()  

    
if __name__ == '__main__':
    main()
