# Loading Modules/Header files
from tkinter import *
from tkinter.ttk import Scrollbar
import sqlite3

class Developer:
    '''Class Developer : To show Developer's information of this Application.'''
    def __init__(self): # It it the constructor of class(frame is window,self reference is passed automatically)
        self.window = Tk()  # Create window
        self.window.attributes("-alpha",0.85)
        self.window.wm_title("DevelopeR")  # title of window
        # self.window.iconbitmap('curriculum-vitae.ico')
        app_width=400
        app_height=400
        scrn_width=self.window.winfo_screenwidth()/2
        scrn_height=self.window.winfo_screenheight()/2
        self.window.geometry(f'{app_width}x{app_height}+{325+int(scrn_width-(app_width/2))}+{int(scrn_height-(app_height/2))}')
        self.window.wm_minsize(200, 400)  # minimum size of window
        self.window.maxsize(400, 400)
        self.window.bind('<Button-1>',self.show)
        self.start()

    def start(self): # defining a function/method with class reference
        colour_background ="#54f54f"
        colour_1="#55f55f"
        colour_2="#42f578"
        colour_3="#42f59c"
        colour_4="#42f5b6"
        # Create a MainFrame
        Main_Frame = Frame(self.window)
        Main_Frame.pack(fill=BOTH,expand=1)
        # Create a canvas
        canvas =Canvas(Main_Frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        # Add scrollbar to canvas
        scroll_bar = Scrollbar(Main_Frame,orient=VERTICAL)
        scroll_bar.pack(side=RIGHT,fill=Y)
        # configure canvas
        canvas.config(yscrollcommand=scroll_bar.set)
        canvas.bind('<Configure>',lambda e: canvas.config(scrollregion=canvas.bbox('all')))
        scroll_bar.config(command=canvas.yview)
        # create another frame inside canvas
        In_Frame=Frame(canvas,bg=colour_background)
        # add new frame to window
        canvas.create_window((0,0),window=In_Frame,anchor="n")
        back = Button(In_Frame,text="<=",bg=colour_background,bd=0,font=("Airel",12,"bold"),fg="white",command=self.window.destroy)
        back.place(x=0,y=0)
        Dev_Label= Label(In_Frame,text= "App Developers",fg="Green",bg=colour_background,font=("Times New Roman",20,"bold"),anchor="center")
        Dev_Label.pack(pady=20)
        # hl = canvas.create_line(10,10,50,10,width=3)
        line = Label(In_Frame,text="----------------------(  )---------------------",bg="#54f54f",bd=0,font=("Times New Roman",16,"bold"),fg="red")
        line.pack()
        frame1 = Frame(In_Frame,bg=colour_1,width=360,height=300)#frame widget let u put items together as in container,
        frame1.pack(padx=10,pady=20)
        # frame1.place(relx=0.05,rely=0.1)#(x=150,y=30)

        frame2 = Frame(In_Frame, bg=colour_2, width=360,height=300)  # frame widget let u put items together as in container,
        # frame2.place(relx=0.25, rely=0.1)  # (x=150,y=30)
        frame2.pack(padx=10,pady=20)
        frame3 = Frame(In_Frame, bg=colour_3, width=360,height=300)  # frame widget let u put items together as in container
        # frame3.place(relx=0.5, rely=0.1)  # (x=150,y=30)
        frame3.pack(padx=10,pady=20)
        frame4 = Frame(In_Frame,bg=colour_4,width=360,height=300)
        frame4.pack(padx=10,pady=20)

        # Name: Gaurav Bhardwaj    Email: bhardwajg2411@gmail.com   call @:6283913449
        name1 = Label(frame1,text="Gaurav Bhardwaj",bg=colour_1,font = ("Times New Roman",12,"bold"))
        Call1 = Label(frame1, text="Call @: 6283913449",bg=colour_1, font=("Times New Roman", 12, "bold"))
        name1.place(relx= 0.12,rely=0.08) # X: along length of screen(200),Y: along width of screen(50)
        email1 = Label(frame1, text="Email: bhardwajg2411@gmail.com",bg=colour_1,font = ("Times New Roman",12,"bold"))
        email1.place(relx=0.12,rely=0.24)#x=200,y=100
        Call1.place(relx=0.12,rely=0.4)

        name2 = Label(frame2, text="Girish Kumar",bg=colour_2, font=("Times New Roman", 12, "bold"))
        Call2 = Label(frame2, text="Call @: 6283913449",bg=colour_2, font=("Times New Roman", 12, "bold"))
        name2.place(relx=0.12, rely=0.08)  # X: along length of screen(200),Y: along width of screen(50)
        email2 = Label(frame2, text="Email: bhardwajg2411@gmail.com",bg=colour_2, font=("Times New Roman", 12, "bold"))
        email2.place(relx=0.12, rely=0.24)  # x=200,y=100
        Call2.place(relx=0.12, rely=0.4)

        name3 = Label(frame3, text="Hardik Punj",bg=colour_3, font=("Times New Roman", 12, "bold"))
        Call3 = Label(frame3, text="Call @: 6283913449",bg=colour_3, font=("Times New Roman", 12, "bold"))
        # Name: Gaurav Bhardwaj    Email: bhardwajg2411@gmail.com   call @:6283913449
        name3.place(relx=0.12, rely=0.08)  # X: along length of screen(200),Y: along width of screen(50)
        email3 = Label(frame3, text="Email: bhardwajg2411@gmail.com",bg=colour_3, font=("Times New Roman", 12, "bold"))
        email3.place(relx=0.12, rely=0.24)  # x=200,y=100
        Call3.place(relx=0.12, rely=0.4)

        Version = Label(frame4, font=("Times New Roman", 10, "bold"),bg=colour_4, text="Version:\nBeta(i)")
        Version.place(relx=0.05,rely=0.9)

        # button widget for linking various events
        self.window.mainloop()#required for showing the window
    def show(self,e):
        self.window.attributes("-alpha",1.0)

if __name__ == "__main__":#Python representation of main function
    # window = Tk()#Create window
    # window.wm_title("ResumeR")#title of window
    # window.wm_minsize(200, 400)#minimum size of window
    # window.maxsize(400, 400)
    dev = Developer()#object of class Basics(frame)

    # dev.start()