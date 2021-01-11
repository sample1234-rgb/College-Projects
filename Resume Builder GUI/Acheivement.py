from tkinter import *

import Interests
import WorkExp


class Achievement:
    def __init__(self,frame,mydata):
        self.fr = frame
        self.data = mydata
    def start(self):
        frame = Frame(self.fr,bg="white",width=450,height=300)
        frame.place(relx=0.2,rely=0.1)

        basics = Label(self.fr,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Basic Information:")
        basics.place(relx=0.05,rely=0.12)
        education = Label(self.fr,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Education Qualifications:")
        education.place(relx=0.01,rely=0.18)
        workexp = Label(self.fr,fg= 'white',font = ("Times New Roman",12,"bold"),bg= "green",text = "Work Experience:")
        workexp.place(relx=0.05,rely=0.24)
        Achivd = Label(self.fr,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Your Achievements:")
        Achivd.place(relx=0.03,rely=0.30)

        Achname = Label(frame,text="Achievements:",bg = "white",font = ("Times New Roman",12,"bold"),fg = "black")
        Achname.place(relx= 0.45,rely=0.08)
        Achinfo = Text(frame,width=50,height=10 ,bg = "white",bd=0,font = ("Times New Roman",12),highlightbackground="Blue",highlightthickness=2)
        Achinfo.place(relx= 0.08,rely=0.15)

        w = 150*2.2
        c1 = Canvas(self.fr,bg = "green",width = w,height = 5)
        c1.place(relx = 0,rely =0.85)
        c2 = Canvas(self.fr,bg = "green",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.fr,bg = "green",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.fr,bg = "red",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.fr,bg = "lime",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)

        saveadd =Button(self.fr,text="Save & Add",font = ("Times New Roman",12,"bold"),relief=RIDGE,bg="#30f2f2")
        saveadd.place(x= 425,rely= 0.75)
        done =Button(self.fr,text="Done",font = ("Times New Roman",12,"bold"),relief=RIDGE,bg="#30f2f2")
        done.place(x= 525,rely= 0.75)
        next =Button(self.fr,text="Next =>",font = ("Times New Roman",12,"bold"),command =self.Next,relief=RIDGE,bg="#30c2f2",padx=5)
        next.place(relx= 0.85,rely= 0.90)
        prev =Button(self.fr,text="<= Back",font = ("Times New Roman",12,"bold"),command = self.Prev,relief=RIDGE,bg="#30c2f2",padx=5)
        prev.place(relx= 0.72,rely= 0.90)

        self.fr.mainloop()
    def Prev(self):
        # self.submit()
        q = WorkExp.WorkExp(self.fr,self.data)
        q.start()
    def Next(self):
        # self.submit()
        i = Interests.Interests(self.fr,self.data)
        i.start()

    def SaveAndAdd(self):
        list1 = []
        list1.append()
        print(list1)
        self.data.delete(1.0, END)

    def Done(self):
        new_frame = Frame(self.fr, bg="black", width=40, height=250)
        self.fr.geometry("900x400")
        new_frame.place(relx=0.7, rely=0.1)

        list_box = Listbox(new_frame, width=40, height=15, bg="SystemButtonFace", bd=0, highlightthickness=0,
                           font=("Airel", 12), activestyle="none")
        list_box.pack(side=LEFT, fill=BOTH)

        scroll_bar = Scrollbar(new_frame)
        scroll_bar.pack(side=RIGHT, fill=BOTH)

        list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=list_box.yview)
    # def submit(self):
    #     self.data.append((self.course_name.get(), self.institute_name.get(), self.graduation_year.get(),self.Scores.get(), self.others.get(1.0, END)))
        # print(self.data)