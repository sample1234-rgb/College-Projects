# Loading Modules
from tkinter import *
import Qualify,Acheivement

class WorkExp:
    '''A class for your Experience'''
    def __init__(self,fr):
        self.ui = fr
        # Class Variables(lines 10 - 14) to store information
        self.job_title = StringVar()
        self.company_name = StringVar()
        self.start_year = IntVar()
        self.end_year = IntVar()
        self.Others = StringVar()
    def start(self):
        frame = Frame(self.ui,bg="white",width=450,height=300)
        frame.place(relx=0.2,rely=0.1)

        basics = Label(self.ui,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Basic Information:")
        basics.place(relx=0.05,rely=0.12)
        education = Label(self.ui,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Education Qualifications:")
        education.place(relx=0.01,rely=0.18)
        workexp = Label(self.ui,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Work Experience:")
        workexp.place(relx=0.05,rely=0.24)

        jobtitle = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.job_title,highlightbackground="Blue",highlightthickness=2)
        jobtitle.place(relx= 0.12,rely=0.08)
        jobtitle.insert(0,"Job Title:")
        companyname = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.company_name,highlightbackground="Blue",highlightthickness=2)
        companyname.place(relx= 0.56,rely=0.08)
        companyname.insert(0,"Company Name:")

        startyear = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.start_year,highlightbackground="Blue",highlightthickness=2)
        startyear.place(relx= 0.12,rely=0.25)
        startyear.insert(0,"Start Year:")
        endyear = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.end_year,highlightbackground="Blue",highlightthickness=2)
        endyear.place(relx= 0.56,rely=0.25)
        endyear.insert(0,"End Year:")

        othersl = Label(frame,text="Other Information:",bg = "white",font = ("Times New Roman",10,"bold"),fg = "black")
        othersl.place(relx= 0.12,rely=0.40)
        others = Text(frame,width=50,height=5 ,font = ("Times New Roman",12),highlightbackground="Blue",highlightthickness=2)
        others.place(relx= 0.06,rely=0.5)

        w = 150*2.2
        c1 = Canvas(self.ui,bg = "green",width = w,height = 5)
        c1.place(relx = 0,rely =0.85)
        c2 = Canvas(self.ui,bg = "green",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.ui,bg = "red",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.ui,bg = "lime",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.ui,bg = "lime",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)

        saveadd =Button(self.ui,text="Save & Add",font = ("Times New Roman",12,"bold"),relief=RIDGE,bg="#30f2f2")
        saveadd.place(x= 425,rely= 0.75)
        done =Button(self.ui,text="Done",font = ("Times New Roman",12,"bold"),relief=RIDGE,bg="#30f2f2")
        done.place(x= 525,rely= 0.75)
        next =Button(self.ui,text="Next =>",font = ("Times New Roman",12,"bold"),bg="#30c2f2",padx=5,relief=RIDGE,command = self.Next)
        next.place(relx= 0.85,rely= 0.90)
        prev =Button(self.ui,text="<= Back",font = ("Times New Roman",12,"bold"),bg="#30c2f2",padx=5,relief=RIDGE,command =self.Prev)
        prev.place(relx= 0.72,rely= 0.90)
        self.ui.mainloop()
    def Prev(self):
        q = Qualify.Qualify(self.ui)
        q.start()
    def Next(self):
        i = Acheivement.Achievement(self.ui)
        i.start()