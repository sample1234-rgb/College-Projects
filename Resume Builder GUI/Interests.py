# Loading Modules
from tkinter import *
import Acheivement,TemplateEditor

class Interests:
    '''A class for your Interests'''
    def __init__(self,fr,mydata):
        self.win = fr
        # Class Variables(lines 10 - 14) to store information
        self.Interest_1 = StringVar()
        self.Interest_2 = StringVar()
        self.Interest_3 = StringVar()
        self.Interest_4 = StringVar()
        self.Others = StringVar()
        self.data = mydata
    def start(self):
        frame=Frame(self.win,bg="white",width=450,height=300)
        frame.place(relx=0.2,rely=0.1)

        basics = Label(self.win,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Basic Information:")
        basics.place(relx=0.05,rely=0.12)
        education = Label(self.win,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Education Qualifications:")
        education.place(relx=0.01,rely=0.18)
        workexp = Label(self.win,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Work Experience:")
        workexp.place(relx=0.05,rely=0.24)
        Achivd = Label(self.win,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Your Achievements:")
        Achivd.place(relx=0.03,rely=0.30)
        urInterest = Label(self.win,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Your Interests:")
        urInterest.place(relx=0.05,rely=0.36)

        In1 = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.Interest_1,highlightbackground="Blue",highlightthickness=2,bd=0)
        In1.place(relx= 0.12,rely=0.08)
        In1.insert(0,"Listening to Music..")
        In2 = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.Interest_2,highlightbackground="Blue",highlightthickness=2,bd=0)
        In2.place(relx= 0.56,rely=0.08)
        In2.insert(0,"Playing Guitar..")

        In3 = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.Interest_3,highlightbackground="Blue",highlightthickness=2,bd=0)
        In3.place(relx=0.12,rely=0.25)
        In3.insert(0,"Like to Drive..")
        In4 = Entry(frame,fg="gray",font = ("Times New Roman",12,"bold"),textvariable=self.Interest_4,highlightbackground="Blue",highlightthickness=2,bd=0)
        In4.place(relx= 0.56,rely=0.25)
        In4.insert(0,"Making New Friends :)")

        othersl = Label(frame,text="Other Information:",bg = "white",font = ("Times New Roman",10,"bold"),fg = "black")
        othersl.place(relx= 0.12,rely=0.4)
        others = Text(frame,width=50,height=5 ,bg = "white",font = ("Times New Roman",12),highlightbackground="Blue",highlightthickness=2,bd=0)
        others.place(relx= 0.06,rely=0.50)

        w = 150*2.2
        c1 = Canvas(self.win,bg = "green",width = w,height = 5)
        c1.place(relx = 0,rely =0.85)
        c2 = Canvas(self.win,bg = "green",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.win,bg = "green",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.win,bg = "green",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.win,bg = "red",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)

        next =Button(self.win,text="Next =>",font = ("Times New Roman",12,"bold"),relief=RIDGE,bg="#30c2f2",padx=5)
        next.place(relx= 0.85,rely= 0.90)
        prev =Button(self.win,text="<= Back",font = ("Times New Roman",12,"bold"),command = self.Prev,relief=RIDGE,bg="#30c2f2",padx=5)
        prev.place(relx= 0.72,rely= 0.90)
        self.win.mainloop()
    def Prev(self):
        w = Acheivement.Achievement(self.win,self.data)
        w.start()
    def Next(self):
        te = TemplateEditor.Template_Editor(self.win)