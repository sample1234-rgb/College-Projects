from tkinter import *
import Interests
import WorkExp


class Achievement:
    """ A file for your achievements"""
    def __init__(self, frame, mydata={}):
        self.fr = frame
        self.data = mydata
        self.list1 = []
        self.Achinfo, self.list_box = None, None

    def start(self):
        frame = Frame(self.fr, bg="white", width=450, height=300)
        frame.place(relx=0.2, rely=0.1)

        basics = Label(self.fr, fg='white', font=("Times New Roman", 12, "bold"), bg="green", text="Basic Information:")
        basics.place(relx=0.05, rely=0.12)
        education = Label(self.fr, fg='white', font=("Times New Roman", 12, "bold"), bg="green",
                          text="Education Qualifications:")
        education.place(relx=0.01, rely=0.18)
        workexp = Label(self.fr, fg='white', font=("Times New Roman", 12, "bold"), bg="green", text="Work Experience:")
        workexp.place(relx=0.05, rely=0.24)
        Achivd = Label(self.fr, font=("Times New Roman", 12, "bold"), bg="lime", text="Your Achievements:")
        Achivd.place(relx=0.03, rely=0.30)

        Achname = Label(frame, text="Achievements:", bg="white", font=("Times New Roman", 12, "bold"), fg="black")
        Achname.place(relx=0.45, rely=0.08)
        self.Achinfo = Text(frame, width=50, height=10, bg="white", bd=0, font=("Times New Roman", 12),
                            highlightbackground="Blue", highlightthickness=2)
        self.Achinfo.place(relx=0.08, rely=0.15)

        new_frame = Frame(self.fr, bg="black", width=30, height=250)
        new_frame.place(relx=0.7, rely=0.1)

        self.list_box = Listbox(new_frame, width=20, height=15, bg="SystemButtonFace", bd=0, highlightthickness=2,
                                font=("Airel", 12), activestyle="none", selectbackground='#ededed')
        self.list_box.pack(side=LEFT, fill=BOTH)

        scroll_bar = Scrollbar(new_frame)
        scroll_bar.pack(side=RIGHT, fill=BOTH)

        self.list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.list_box.yview)

        w = 150*2.2
        c1 = Canvas(self.fr, bg="green", width=w, height=5)
        c1.place(relx=0, rely=0.85)
        c2 = Canvas(self.fr, bg="green", width=w, height=5)
        c2.place(relx=0.20, rely=0.85)
        c3 = Canvas(self.fr, bg="green", width=w, height=5)
        c3.place(relx=0.40, rely=0.85)
        c4 = Canvas(self.fr, bg="red", width=w, height=5)
        c4.place(relx=0.60, rely=0.85)
        c5 = Canvas(self.fr, bg="lime", width=w, height=5)
        c5.place(relx=0.80, rely=0.85)

        saveadd = Button(self.fr, text="Save & Add", font=("Times New Roman", 12, "bold"), relief=RIDGE, bg="#30f2f2",
                         command=self.saveAndAdd)
        saveadd.place(x=425, rely=0.75)
        # done = Button(self.fr, text="Save", font=("Times New Roman", 12, "bold"), relief=RIDGE, bg="#30f2f2",
        #               command=self.save)
        # done.place(x=525, rely=0.75)
        next_b = Button(self.fr, text="Next =>", font=("Times New Roman", 12, "bold"), command=self.next_win,
                        relief=RIDGE, bg="#30c2f2", padx=5)
        next_b.place(relx=0.85, rely=0.90)
        prev = Button(self.fr, text="<= Back", font=("Times New Roman", 12, "bold"), command=self.prev_win, relief=RIDGE
                      , bg="#30c2f2", padx=5)
        prev.place(relx=0.72, rely=0.90)

        if self.data.__contains__('Achievements'):
            d = self.data['Achievements']
            print(d)
            for i in d:
                self.list1.append(i)
                self.list_box.insert(END, i)

        self.fr.mainloop()

    def prev_win(self):
        self.submit()
        q = WorkExp.WorkExp(self.fr, self.data)
        q.start()

    def next_win(self):
        self.submit()
        i = Interests.Interests(self.fr, self.data)
        i.start()

    def saveAndAdd(self):
        text = self.Achinfo.get(1.0, END)
        if len(text) > 5:
            self.list1.append(text)
            self.list_box.insert(END, text)
        self.Achinfo.delete(1.0, END)

    def submit(self):
        self.data['Achievements'] = self.list1
        print(self.data['Achievements'])


if __name__ == "__main__":
    wn = Tk()
    c = Achievement(wn)
    c.start()
