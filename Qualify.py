# Including Modules
from tkinter import *
import Basics,WorkExp

class Qualify:
    '''A Qualify class to input Educational Qualifications'''
    def __init__(self,frame):#Class Constructor
        self.win = frame #Window
        # Class Variables(lines 10 - 14) to store information
        self.course_name = StringVar()
        self.institute_name = StringVar()
        self.graduation_year = IntVar()
        self.Scores = IntVar()
        self.Others = StringVar()
    def start(self):
        frame = Frame(self.win, bg="white", width=450,height=300)  # frame widget let u put items together as in container,
        # benefit if you want to adjust this is that placement of objects are not required to be change every time on the window
        frame.place(relx=0.2, rely=0.1)# (x=150,y=30)

        basics = Label(self.win,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Basic Information:")
        basics.place(relx=0.05,rely=0.12)     #Label- to write text on UI
        education = Label(self.win,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Education Qualifications:")
        education.place(relx=0.01,rely=0.18)
        # Entry boxes ->
        crsname = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable=self.course_name)
        crsname.place(relx=0.12,rely=0.08)#(x= 200,y=50)
        crsname.insert(0,"Course Title:")
        instname = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable=self.institute_name)
        instname.place(relx=0.56,rely=0.08)#(x= 400,y=50)
        instname.insert(0,"Institution Name:")

        passyear = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable=self.graduation_year)
        passyear.place(relx=0.12,rely=0.25)#(x= 200,y=100)
        passyear.insert(0,"Passing Year:")
        score = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable=self.Scores)
        score.place(relx=0.56,rely=0.25)#(x= 400,y=100)
        score.insert(0,"Scores:")

        othersl = Label(frame,text="Other Information:",bg = "white",font = ("Times New Roman",10,"bold"),fg = "black")
        othersl.place(relx=0.12,rely=0.40)#(x= 180,y=150)
        others = Text(frame,width=50,height=5,highlightbackground="Blue",highlightthickness=2,font = ("Times New Roman",12),padx=2,pady=5)
        others.place(relx=0.06,rely=0.5)#(x= 180,y=180)
        # Unoptimized progess bar -->
        w = 150*2.2
        c1 = Canvas(self.win,bg = "green",width = w,height = 5)
        c1.place(relx = 0.0,rely =0.85)
        c2 = Canvas(self.win,bg = "red",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.win,bg = "lime",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.win,bg = "lime",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.win,bg = "lime",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)
        # Buttons -->
        next =Button(self.win,text="Next =>",bg="#30c2f2",font = ("Times New Roman",12,"bold"),relief=RIDGE,command=self.Next,padx=5)
        next.place(relx= 0.85,rely= 0.90)
        prev =Button(self.win,text="<= Back",bg="#30c2f2",font = ("Times New Roman",12,"bold"),relief=RIDGE,command = self.Prev,padx=5)
        prev.place(relx= 0.72,rely= 0.90)
        self.win.mainloop()
    def Prev(self):#Previous Window
        b = Basics.Basics(self.win)
        b.start()
    def Next(self):#Next Window
        w = WorkExp.WorkExp(self.win)
        w.start()
