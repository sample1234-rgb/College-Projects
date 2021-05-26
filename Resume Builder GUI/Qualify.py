# Including Modules
from tkinter import *
import Basics
import WorkExp


class Qualify:
    """A Qualify class to input Educational Qualifications"""
    def __init__(self, frame, mydata={}):    # Class Constructor
        self.win = frame    # Window
        # Class Variables(lines 10 - 14) to store information
        self.course_name = StringVar()
        self.institute_name = StringVar()
        self.graduation_year = IntVar()
        self.Scores = IntVar()
        self.Others = StringVar()
        self.others, self.list_box = None, None
        self.list1 = []
        self.data = mydata

    def start(self):
        frame = Frame(self.win, bg="white", width=450, height=300)
        # frame widget let u put items together as in container, benefit if you want to adjust this is that placement of
        # objects are not required to be change every time on the window
        frame.place(relx=0.2, rely=0.1)     # (x=150,y=30)

        basic = Label(self.win, fg='white', font=("Times New Roman", 12, "bold"), bg="green", text="Basic Information:")
        basic.place(relx=0.05, rely=0.12)     # Label- to write text on UI
        education = Label(self.win, font=("Times New Roman", 12, "bold"), bg="lime", text="Education Qualifications:")
        education.place(relx=0.01, rely=0.18)
        # Entry boxes ->
        crsname = Entry(frame, fg="gray", font=("Times New Roman", 12, "bold"), highlightbackground="Blue",
                        highlightthickness=2, textvariable=self.course_name)
        crsname.place(relx=0.12, rely=0.08)     # (x= 200,y=50)
        instname = Entry(frame, fg="gray", font=("Times New Roman", 12, "bold"), highlightbackground="Blue",
                         highlightthickness=2, textvariable=self.institute_name)
        instname.place(relx=0.56, rely=0.08)    # (x= 400,y=50)

        passyear = Entry(frame, fg="gray", font=("Times New Roman", 12, "bold"), highlightbackground="Blue",
                         highlightthickness=2, textvariable=self.graduation_year)
        passyear.place(relx=0.12, rely=0.25)    # (x= 200,y=100)
        score = Entry(frame, fg="gray", font=("Times New Roman", 12, "bold"), highlightbackground="Blue",
                      highlightthickness=2, textvariable=self.Scores)
        score.place(relx=0.56, rely=0.25)   # (x= 400,y=100)

        othersl = Label(frame, text="Other Information:", bg="white", font=("Times New Roman", 10, "bold"),
                        fg="black")
        othersl.place(relx=0.12, rely=0.40)  # (x= 180,y=150)
        self.others = Text(frame, width=50, height=5, highlightbackground="Blue", highlightthickness=2,
                           font=("Times New Roman", 12), padx=2, pady=5)
        self.others.place(relx=0.06, rely=0.5)   # (x= 180,y=180)
        # Unoptimized progress bar -->
        w = 150*2.2
        c1 = Canvas(self.win, bg="green", width=w, height=5)
        c1.place(relx=0.0, rely=0.85)
        c2 = Canvas(self.win, bg="red", width=w, height=5)
        c2.place(relx=0.20, rely=0.85)
        c3 = Canvas(self.win, bg="lime", width=w, height=5)
        c3.place(relx=0.40, rely=0.85)
        c4 = Canvas(self.win, bg="lime", width=w, height=5)
        c4.place(relx=0.60, rely=0.85)
        c5 = Canvas(self.win, bg="lime", width=w, height=5)
        c5.place(relx=0.80, rely=0.85)
        # Buttons -->
        self.saveadd = Button(self.win, text="Save & Add", font=("Times New Roman", 12, "bold"), relief=RIDGE,
                              bg="#30f2f2", command=self.saveAndAdd)
        self.saveadd.place(x=425, rely=0.75)

        next_b = Button(self.win, text="Next =>", bg="#30c2f2", font=("Times New Roman", 12, "bold"), relief=RIDGE,
                        command=self.next_window, padx=5)
        next_b.place(relx=0.85, rely=0.90)
        prev = Button(self.win, text="<= Back", bg="#30c2f2", font=("Times New Roman", 12, "bold"), relief=RIDGE,
                      command=self.prev_window, padx=5)
        prev.place(relx=0.72, rely=0.90)

        new_frame = Frame(self.win, bg="black", width=30, height=250)
        new_frame.place(relx=0.7, rely=0.1)

        self.list_box = Listbox(new_frame, width=20, height=15, bg="SystemButtonFace", bd=0, highlightthickness=2,
                                font=("Airel", 12), activestyle="none", selectbackground='#ededed')
        self.list_box.pack(side=LEFT, fill=BOTH)

        scroll_bar = Scrollbar(new_frame)
        scroll_bar.pack(side=RIGHT, fill=BOTH)

        self.list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.list_box.yview)

        self.course_name.set("Course Title:")
        self.institute_name.set("Institution Name:")
        self.graduation_year.set("Passing Year:")
        score.insert(0, "Scores:")
        if self.data.__contains__("Education"):
            d = self.data['Education']
            for i in d:
                self.list1.append(i)
                self.list_box.insert(END, i)
        self.win.mainloop()

    def prev_window(self):     # Previous Window
        self.submit()
        b = Basics.Basics(self.win, self.data)
        b.start()

    def next_window(self):     # Next Window
        self.submit()
        w = WorkExp.WorkExp(self.win, self.data)
        w.start()

    def saveAndAdd(self):
        if self.course_name.get() != "Course Title":
            text = (self.course_name.get(), self.institute_name.get(), self.graduation_year.get(), self.Scores.get(),
                    self.others.get(1.0, END))
            self.list1.append(text)
            self.list_box.insert(END, text)
            self.course_name.set("Course Title:")
            self.institute_name.set("Institution Name:")
            self.graduation_year.set("Passing Year:")
            self.Scores.set("Scores:")
            self.saveadd.config(bg='#30f2f2', fg='black')
        else:
            self.saveadd.config(bg="red", fg="white")

    def submit(self):
        if self.data.__contains__('Education'):
            self.data['Education'] =[self.list1]
        else:
            if self.course_name.get() != 'Course Title:':
                self.data['Education'] = [self.list1]
        print(self.data['Education'])
