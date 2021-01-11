# Loading Modules/Header files
from tkinter import *
import Qualify,sqlite3,Developer
from tkinter import messagebox
from googletrans import Translator
def length(num):
    cnt=0
    while(num > 0):
        num = num/10
        cnt += 1
    return cnt
class Basics:
    '''Class Basic Information : To collect your reference''' # '''-''' is called a doc-string->used to tell information
    def __init__(self,frame,mydata): # It it the constructor of class(frame is window,self reference is passed automatically)
        self.window = frame # Self is the class reference ~This statement in C/C++/Java
        # Class Variables(lines 10 - 17) to store information
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.Email = StringVar()
        self.LinkedIn = StringVar()
        self.cont1 = IntVar()
        self.cont2 = IntVar()
        self.Address1 = StringVar()
        self.Address2 = StringVar()
        self.data = mydata
    # def __init__(self,frame,pk):
    #     pass
    def start(self): # defining a function/method with class reference
        # c = Canvas(self.window,bg="white",width=450)# widget for drawing purposes(frame,bgcolour,width)
        # c.place(x=150,y=30)#adjustment
        tranlate_btn = Button(self.window,font=("Times New Roman",12,"bold"),bd=0,text="Translate")
        # tranlate_btn.place(relx=0.15,rely=0.9)
        frame1 = Frame(self.window,bg="white",width=450,height=300)#frame widget let u put items together as in container,
        # benefit if you want to adjust this is that placement of objects are not required to be change every time on the window
        frame1.place(relx=0.2,rely=0.1)#(x=150,y=30)
        Version = Button(self.window, font=("Times New Roman", 10, "bold"),bd=0, text="Version:\nChocolate",command = self.Dev)
        Version.place(relx=0.05,rely=0.9)

        basics = Label(self.window,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Basic Information:")
        # Label is used to print text in window
        basics.place(relx=0.05,rely=0.12)

        self.fname = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable = self.first_name)
        # Entry widget for taking input,fname = First Name
        self.fname.place(relx= 0.12,rely=0.08) # X: along length of screen(200),Y: along width of screen(50)
        self.lname = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable = self.last_name)
        self.lname.place(relx=0.56,rely=0.08)#x=400,y=50

        self.email = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable=self.Email)
        self.email.place(relx=0.12,rely=0.25)#x=200,y=100
        self.link = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable =self.LinkedIn)
        self.link.place(relx= 0.56,rely=0.25)#x=400,y=100

        self.contact1 = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable= self.cont1)
        self.contact1.place(relx=0.12,rely=0.42)#(x= 200,y=150)
        self.contact2 = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,textvariable= self.cont2)
        self.contact2.place(relx=0.56,rely=0.42)#(x= 400,y=150)

        self.address1 = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,width = 50,textvariable=self.Address1)
        self.address1.place(relx=0.07,rely=0.6)#(x= 180,y=200)
        self.address2 = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,width=50,textvariable= self.Address2)
        self.address2.place(relx=0.07,rely=0.78)#(x= 180,y=250)
        # Ignore this doc_string
        '''
        self.c= []
        x=0
        for _ in range(5):
            a = Canvas(self.window,bg = "red",width = 150*2.2,height = 5)
            a.place(relx = 0+x,rely=0.85)
            self.c.append(a)
            x += 0.2
        for i in range(1,5):
            self.c[i].config(bg = "lime")'''
        if(len(self.data) == 0):
            self.first_name.set('First Name:')
            self.last_name.set("Last Name:")
            self.Email.set("E-mail:")
            self.LinkedIn.set("LinkedIn:")
            self.cont1.set(1234567890)
            self.cont2.set(9876543210)
            self.Address1.set("Address 1:")
            self.Address2.set("Address 2:")
        else:
            self.first_name.set(self.data[0][0])
            self.last_name.set(self.data[0][1])
            self.Email.set(self.data[0][2])
            self.LinkedIn.set(self.data[0][3])
            self.cont1.set(self.data[0][4])
            self.cont2.set(self.data[0][5])
            self.Address1.set(self.data[0][6])
            self.Address2.set(self.data[0][7])

        # Unoptimized Progress Bar:
        w=150*2.2# showing current level status
        c1 = Canvas(self.window,bg = "red",width = w,height = 5)
        c1.place(relx = 0.0,rely =0.85)
        c2 = Canvas(self.window,bg = "lime",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.window,bg = "lime",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.window,bg = "lime",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.window,bg = "lime",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)

        next =Button(self.window,text="Next =>",font = ("Times New Roman",12,"bold"),bg="#30c2f2",command = self.Next,relief = RIDGE,padx =5)
        next.place(relx= 0.85,rely= 0.90)   #relx,rely: relative positions acc.to the window size (in %)
        # button widget for linking various events
        self.window.mainloop()#required for showing the window
    def Next(self):#method
        if self.first_name.get()=='' or self.first_name.get()=="First Name:":
            self.fname.config(highlightbackground="red",highlightthickness=2)
            messagebox.showwarning("No first name","Please enter your first name")
        elif self.last_name.get() == '' or self.last_name.get() == "Last Name:":
            self.lname.config(highlightbackground="red", highlightthickness=2)
            messagebox.showwarning("No last name", "Please enter your last name")
        elif self.Email.get() == '' or self.Email.get() == "E-mail:":
            self.email.config(highlightbackground="red", highlightthickness=2)
            messagebox.showwarning("No email", "Please enter your Email Address")
        elif self.cont1.get() == 1234567890:
            self.contact1.config(highlightbackground="red", highlightthickness=2)
            messagebox.showwarning("No Contact number", "Please enter your contact details")
        elif self.Address1.get() == '' or self.Address1.get() == "Address 1:":
            self.address1.config(highlightbackground="red", highlightthickness=2)
            messagebox.showwarning("No Address given", "Please enter your Address details")
        # if length(self.cont1.get()) != 10:
        #     messagebox.showerror("Contact Detail Error", "Contact Number not having 10 digits")
        # Temporary Checking/Assignmment:
        if self.cont2.get() == 9876543210:
            self.cont2.set(0)
        # if length(self.cont2.get()) != 10:
        #     messagebox.showerror("Contact Detail Error", "Contact Number not having 10 digits")

        if self.Address2.get() == '' or self.Address2.get() == "Address 2:":
            self.Address2.set("-")

        if(len(self.data) == 0):
            self.data.append((self.fname.get(),self.lname.get(),self.Email.get(),self.LinkedIn.get(),self.cont1.get(),self.cont2.get(),self.Address1.get(),self.Address2.get()))
        else:
            self.data[0] = (self.fname.get(), self.lname.get(), self.Email.get(), self.LinkedIn.get(),
                              self.cont1.get(), self.cont2.get(), self.Address1.get(), self.Address2.get())
        print(self.data)
        # Database Connectivity
        '''
        with sqlite3.connect('Database.db') as connection:
            # with clause works similar to try-catch block exception if file execution is interrupted, it automatically closes the file
            cur = connection.cursor()
            # cur.execute(''INSERT INTO Contact VALUES(:number)'',{'number': self.cont1.get()})
            c_id_1 = cur.execute("SELECT oid from Contact where number={}".format(self.cont1.get())).fetchone()
            c_id_1 = c_id_1[0]
            c_id_2 = 0
            # cur.execute(''INSERT INTO Addresses(address) VALUES(:address)'',{'address':self.Address1.get()})#.format(self.Address1.get()))
            a_id_1 = cur.execute("SELECT oid,address FROM Addresses where address={}".format(self.Address1.get())).fetchall()
            # for id in a_id_1:
            #     if (id[1] == self.Address1.get()):
            #         a_id_1 = id[0]
            print(a_id_1)
            a_id_2 = 0
            if int(self.contact2.get()) != 0:
                # cur.execute(''INSERT INTO Contact VALUES(:a)'',{"a":self.cont2.get()})
                c_id_2 = cur.execute("SELECT oid from Contact where number={}".format(self.contact2.get())).fetchone()
                print(c_id_2)
                # c_id_2 = c_id_2
            if self.Address2.get() != "-":
                # cur.execute(''INSERT INTO Addresses(address) VALUES(:address)'',{'address':self.Address2.get()})
                a_id_2 = cur.execute("SELECT oid,address from Addresses").fetchone()
                for id in a_id_2:
                    if (id[1] == self.Address2.get()):
                        a_id_2 = id[0]
            # cur.execute(''INSERT INTO information VALUES(:a,:b,:c,:d,:e,:f,:g,:h)'',{"a":self.first_name.get(),"b":self.last_name.get(),"c":self.Email.get(),"d":self.LinkedIn.get(),"e":c_id_1,"f":c_id_2,"g":a_id_1,"h":a_id_2})
            connection.commit()
            connection.close()'''
        messagebox.showinfo("Done","Data is Saved")
        q = Qualify.Qualify(self.window,self.data)  # from module Qualify create object of class Qualify
        q.start()

    def Dev(self):
        dev= Developer.Developer()

if __name__ == "__main__":#Python representation of main function, actually it is a function that checks for cuurent file name
    window = Tk()#Create window
    window.wm_title("ResumeR")#title of window
    window.iconbitmap("curriculum-vitae.ico")
    app_width=650
    app_height=400
    screen_width= window.winfo_screenwidth()/2
    screen_height= window.winfo_screenheight()/2
    window.geometry( f'{app_width}x{app_height}+{int(screen_width-(app_width)/2)-200}+{int(screen_height-(app_height)/2)}' )
    window.wm_minsize(650, 400)#minimum size of window
    mydata= []
    basics = Basics(window,mydata)#object of class Basics(frame)
    basics.start()