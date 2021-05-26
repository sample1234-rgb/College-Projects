# Loading Modules
from tkinter import *
import Qualify, Acheivement

class WorkExp:
    '''A class for your Experience'''
    def __init__(self,  fr,  mydata={}):
        self.ui = fr
        # Class Variables(lines 10 - 14) to store information
        self.job_title = StringVar()
        self.company_name = StringVar()
        self.start_year = IntVar()
        self.end_year = IntVar()
        self.Others = StringVar()
        self.data = mydata
        self.list1 = []
        self.list_box = None

    def start(self):
        frame = Frame(self.ui, bg="white", width=450, height=300)
        frame.place(relx=0.2, rely=0.1)

        basics = Label(self.ui, fg='white', font=("Times New Roman", 12, "bold"), bg="green", text="Basic Information:")
        basics.place(relx=0.05, rely=0.12)
        education = Label(self.ui, fg='white', font=("Times New Roman", 12, "bold"), bg="green", text="Education Qualifications:")
        education.place(relx=0.01, rely=0.18)
        workexp = Label(self.ui, font=("Times New Roman", 12, "bold"), bg="lime", text="Work Experience:")
        workexp.place(relx=0.05, rely=0.24)

        jobtitle = Entry(frame, fg="gray", font = ("Times New Roman", 12, "bold"), textvariable=self.job_title, highlightbackground="Blue", highlightthickness=2)
        jobtitle.place(relx= 0.12, rely=0.08)
        companyname = Entry(frame, fg="gray", font = ("Times New Roman", 12, "bold"), textvariable=self.company_name, highlightbackground="Blue", highlightthickness=2)
        companyname.place(relx= 0.56, rely=0.08)

        startyear = Entry(frame, fg="gray", font = ("Times New Roman", 12, "bold"), textvariable=self.start_year, highlightbackground="Blue", highlightthickness=2)
        startyear.place(relx= 0.12, rely=0.25)
        endyear = Entry(frame, fg="gray", font = ("Times New Roman", 12, "bold"), textvariable=self.end_year, highlightbackground="Blue", highlightthickness=2)
        endyear.place(relx= 0.56, rely=0.25)

        othersl = Label(frame, text="Other Information:", bg = "white", font = ("Times New Roman", 10, "bold"), fg = "black")
        othersl.place(relx= 0.12, rely=0.40)
        self.others = Text(frame, width=50, height=5 , font = ("Times New Roman", 12), highlightbackground="Blue", highlightthickness=2)
        self.others.place(relx= 0.06, rely=0.5)

        # if(len(self.data) == 2):
        self.job_title.set("Job Title:")
        self.company_name.set("Company Name:")
        self.start_year.set("Start Year:")
        self.end_year.set("End Year:")

        w = 150*2.2
        c1 = Canvas(self.ui, bg="green", width=w, height=5)
        c1.place(relx=0, rely=0.85)
        c2 = Canvas(self.ui, bg="green", width=w, height=5)
        c2.place(relx=0.20, rely=0.85)
        c3 = Canvas(self.ui, bg="red", width=w, height=5)
        c3.place(relx=0.40, rely=0.85)
        c4 = Canvas(self.ui, bg="lime", width=w, height=5)
        c4.place(relx=0.60, rely=0.85)
        c5 = Canvas(self.ui, bg="lime", width=w, height=5)
        c5.place(relx=0.80, rely=0.85)

        self.saveadd = Button(self.ui, text="Save & Add", font=("Times New Roman", 12, "bold"), relief=RIDGE,
                              bg="#30f2f2", command=self.SaveAndAdd)
        self.saveadd.place(x=425, rely=0.75)
        next = Button(self.ui, text="Next =>", font = ("Times New Roman", 12, "bold"), bg="#30c2f2", padx=5, relief=RIDGE, command = self.Next)
        next.place(relx=0.85, rely=0.90)
        prev = Button(self.ui, text="<= Back", font = ("Times New Roman", 12, "bold"), bg="#30c2f2", padx=5, relief=RIDGE, command =self.Prev)
        prev.place(relx=0.72, rely=0.90)

        new_frame = Frame(self.ui, bg="black", width=40, height=250)
        self.ui.geometry("900x400")
        new_frame.place(relx=0.7, rely=0.1)

        self.list_box = Listbox(new_frame, width=40, height=15, bg="SystemButtonFace", bd=0, highlightthickness=0, font=("Airel", 12), activestyle="none")
        self.list_box.pack(side=LEFT, fill=BOTH)
        for i in range(len(self.list1)):
            self.list_box.insert(END, self.list1[0][i])

        scroll_bar = Scrollbar(new_frame)
        scroll_bar.pack(side=RIGHT, fill = BOTH)

        self.list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.list_box.yview)

        self.ui.mainloop()

    def Prev(self):
        self.submit()
        q = Qualify.Qualify(self.ui, self.data)
        q.start()

    def Next(self):
        self.submit()
        i = Acheivement.Achievement(self.ui, self.data)
        i.start()

    def submit(self):
        if self.data.__contains__('Technical'):
            self.data['Technical'] = [self.list1]
        else:
            self.data['Technical'] = [self.list1]
        print(self.data['Technical'])

    def check_item(self):
        self.list_box.itemconfig(self.list_box.curselection(), fg="#4e4e4e")
        self.list_box.selection_clear(0, END)

    def uncheck_item(self):
        self.list_box.itemconfig(self.list_box.curselection(), fg="black")
        self.list_box.selection_clear(0, END)

    def SaveAndAdd(self):
        if self.job_title.get() != "Job Title":
            text = (self.job_title.get(), self.company_name.get(), self.start_year.get(), self.end_year.get(),
                    self.others.get(1.0, END))
            self.list1.append(text)
            self.list_box.insert(END, text)
            self.job_title.set("Job Title:")
            self.company_name.set("Company Name:")
            self.start_year.set("Start Year:")
            self.end_year.set("End Year:")
            self.others.delete(1.0, END)

            self.saveadd.config(bg='#30f2f2', fg='black')
        else:
            self.saveadd.config(bg="red", fg="white")


if __name__ == "__main__":
    window = Tk()
    window.wm_title("ResumeR")  # title of window
    window.iconbitmap("curriculum-vitae.ico")
    app_width = 650
    app_height = 400
    screen_width = window.winfo_screenwidth() / 2
    screen_height = window.winfo_screenheight() / 2
    window.geometry(
        f'{app_width}x{app_height}+{int(screen_width - (app_width) / 2) - 200}+{int(screen_height - (app_height) / 2)}')
    window.wm_minsize(650,  400)  # minimum size of window
    obj = WorkExp(window, [])
    obj.start()
