from tkinter import *
from tkinter import filedialog,font,colorchooser,messagebox,dnd
import os,sys,sqlite3
from docx import Document
from fpdf import FPDF
import Designs
'''
class NewCanvas(Canvas):
    def __init__(self,*args,**kargs):
        super(Canvas).__init__(*args,**kargs)

    def create_table(self,x1, y1, x2, y2, r=25, reverse=False, **Options):
        # x1=425, y1=150, x2= 675, y2= 350
        colour_1 = "#ffc466"
        colour_2 = "#ffd485"
        colour_3 = "#ff5656"
        Page.create_rectangle(x1, y1 + r, x2, y2 - r, fill=colour_2, outline="")  # (425,175,675,325) I
        Page.create_rectangle(x1 + r, y2 - r, x2 - r, y2, fill=colour_2, outline="")  # (450,325,650,350) II
        Page.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour_2, outline="")  # (425,300,475,350) 3
        Page.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour_2, outline="")  # (625,300,675,350) 2

        Page.create_rectangle(x1 + r, y1, x2 - r, y1 + 2 * r, fill=colour_1, outline="")  # III (450, 200, 650, 150)
        if (reverse):
            Page.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_3, outline="")  # 1 (425, 150, 475, 200)
            Page.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_1, outline="")  # 4 (625, 150, 675, 200)
        else:
            Page.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_1, outline="")  # 1 (425, 150, 475, 200)
            Page.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_3, outline="")  # 4 (625, 150, 675, 200)

    def create_rounded_rectangle(self,x1, y1, x2, y2, r=25, color="#ca94ff"):
        Points = [x1, y1 + r, x1 + r, y1 + r, x1 + r, y1, x2 - r, y1, x2 - r, y1 + r, x2, y1 + r, x2, y2 - r, x2 - r,
                  y2 - r, x2 - r, y2, x1 + r, y2, x1 + r, y2 - r, x1, y2 - r]
        colour = color
        Page.create_polygon(Points, fill=colour, outline="")
        Page.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour, outline="")  # 1 (425, 150, 475, 200)
        Page.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour, outline="")  # (625,300,675,350) 2
        Page.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour, outline="")  # (425,300,475,350) 3
        Page.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour, outline="")  # 4 (625, 150, 675, 200)
'''
class Template_Editor:

    def __init__(self):
        # self.root =frame
        self.root = Tk()
        self.root.title("Template Editor")
        self.root.iconbitmap("curriculum-vitae.ico")
        self.Mark = True
        self.wm = None
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.root.minsize(int(0.8 * self.root.winfo_screenwidth()), int(0.9 * self.root.winfo_screenheight()))
        # Panels
        self.panned_window = PanedWindow(bd=5, bg="red", relief=RAISED)
        self.panned_window.pack(fill=BOTH, expand=1)

        self.pan_1 = PanedWindow(bd=0, relief=RAISED, orient=VERTICAL)
        self.panned_window.add(self.pan_1, width=125, minsize=50)
        self.frame_1 = Frame(self.pan_1, bg="white")
        self.pan_1.add(self.frame_1)

        pan_11 = PanedWindow(bd=0, relief=RAISED)
        self.pan_1.add(pan_11)
        self.frame_11 = Frame(pan_11, bg="white")
        pan_11.add(self.frame_11)

        self.pan_2 = PanedWindow(bd=0, relief=RAISED)
        self.panned_window.add(self.pan_2, width=900, minsize=900)
        self.frame_2 = Frame(self.pan_2, bg="white")
        self.pan_2.add(self.frame_2)

        self.pan_3 = PanedWindow(bd=0, relief=RAISED)
        self.panned_window.add(self.pan_3, minsize=50)
        self.frame_3 = Frame(self.pan_3, bg="white")
        self.pan_3.add(self.frame_3)

        self.prev_btn = Button(self.frame_2, text="<=", bd=0, command=self.Prev)
        # pan_2.add(prev_btn,minsize=10)
        self.prev_btn.place(relx=0.02, rely=0.95)
        self.Scroll_Bar = Scrollbar(self.frame_2)
        self.Scroll_Bar.pack(side=RIGHT, fill=Y)
        self.Page = Canvas(self.frame_2, bg="white", width=800, height=1000, bd=2)  # ,xscrollcommand=Horizontal_scroll.set,)bd=2)
        self.Page.config(scrollregion=(0, 0, 800, 1000), yscrollcommand=self.Scroll_Bar.set)
        self.Scroll_Bar.config(command=self.Page.yview)
        # Page.config(width=800,height=1200,yscrollcommand=Scroll_Bar.set,scrollregion=Page.bbox(0,0,1000,1000))
        self.Page.pack()
        # photo_btn = Button(frame_2, text="| O=|' ", bg="white", relief=RIDGE)
        # ds = Designs.Design(Page)
        self.Text_Label_Frame = LabelFrame(self.frame_1, text="Text", bg="gray", fg="white", font=("Arial", 12, "bold"))
        self.Text_Label_Frame.pack(fill=BOTH, expand=1)  # .place(relx=0.1,rely=0.01)
        self.Remove_Text_btn = Button(self.Text_Label_Frame, text=" X ", bg="#9c3030", fg="white", bd=0, font=("Arial", 12, "bold"), command=self.remove_text)
        self.Remove_Text_btn.place(x=0, y=20)
        self.config_Text_btn = Button(self.Text_Label_Frame, text=" ->", bg="gray", fg="white", bd=0, font=("Arial", 12, "bold"), command=self.config_text)
        self.config_Text_btn.place(x=0, y=50)
        self.Add_Text_btn = Button(self.Text_Label_Frame, text=" + ", bg="#309c30", fg="white", bd=0, font=("Arial", 12, "bold"), command=self.Add_Text)
        self.Add_Text_btn.place(x=0, y=70)

        Object_Label_Frame = LabelFrame(self.frame_11, text="Object", bg="gray", fg="white", font=("Ariel", 10, "bold"))
        Object_Label_Frame.pack(fill=BOTH, expand=1)  # .place(relx=0.1,rely=0.1)

        Text_Box_btn = Button(Object_Label_Frame, text="T", font=("Times New Roman", 10), relief=RIDGE)
        Text_Box_btn.grid(row=0, column=0)
        self.draw_rect_btn = Button(Object_Label_Frame, text="[]", font=("Times New Roman", 10), relief=RIDGE, command=lambda :self.Object(0))
        self.draw_rect_btn.grid(row=0, column=1)
        # i=1
        self.draw_line_btn = Button(Object_Label_Frame, text="/", font=("Times New Roman", 10), relief=RIDGE, command=lambda :self.Object(1))
        self.draw_line_btn.grid(row=0, column=2)
        # i=2
        self.draw_circle_btn = Button(Object_Label_Frame, text="O", font=("Times New Roman", 10), relief=RIDGE, command=lambda :self.Object(2))
        self.draw_circle_btn.grid(row=0, column=3)

        # Panel 3
        File_Lable_Frame = LabelFrame(self.frame_3, text="File", bg="gray", fg="white", font=("Ariel", 12, "bold"))
        File_Lable_Frame.pack(fill=X, expand=1)  # place(relx=0.1,rely=0.01)
        new_btn = Button(File_Lable_Frame, text="New", font=("Times New Roman", 10), relief=RIDGE, command=self.New_File)
        new_btn.pack(fill=X, expand=1)  # padx=5,pady=5)
        open_btn = Button(File_Lable_Frame, text="Open", font=("Times New Roman", 10), relief=RIDGE, command=self.Open_File)
        open_btn.pack(fill=X, expand=1)  # padx=5,pady=5)
        save_btn = Button(File_Lable_Frame, text="Save", font=("Times New Roman", 10), relief=RIDGE, command=self.Save_File)
        save_btn.pack(fill=X, expand=1)  # padx=10,pady=5)
        save_as_btn = Button(File_Lable_Frame, text="Save As", font=("Times New Roman", 10), relief=RIDGE,command=self.Save_As_File)
        save_as_btn.pack(fill=X, expand=1)  # padx=10, pady=5)

        View_Label_Frame = LabelFrame(self.frame_3, text="View", bg="gray", fg="white", font=('Ariel', 12, "bold"))
        View_Label_Frame.pack(fill=X, expand=1)  # place(relx=0.1,rely=0.25)
        self.Apperance_btn = Button(View_Label_Frame, text="Theme", font=("Times New Roman", 10), relief=RIDGE, command=self.dark)
        self.Apperance_btn.pack(fill=X, expand=1)
        self.watermark_btn= Button(View_Label_Frame, text="Watermark", font=("Times New Roman", 10), relief=RIDGE, command=self.mark)
        self.watermark_btn.pack(fill=X, expand=1)

        self.nxt_btn = Button(self.frame_2, text="=>", width=0, bd=0, command=self.Next)
        self.nxt_btn.place(relx=0.95, rely=0.95)
        self.ds = Designs.Design(self.Page)

        self.mark()
        self.binder() # For making all tokens bind to Events
        self.root.mainloop()

    def mark(self):
        """For the sake of Publicity: added WaterMark text"""
        if self.Mark:
            self.Mark = False
            self.watermark_btn.config(relief=RIDGE)
            self.Page.delete(self.wm)
        else:
            self.Mark = True
            self.watermark_btn.config(relief=GROOVE)
            self.wm =self.Page.create_text(700, 980, text="Made by Resume Builder", font=("Arial Black", 6))

    def Next(self):
        '''Move to Next Template of the range'''
        self.nxt_btn.config(command=self.ds.next_Design)
        self.binder()

    def binder(self):
        """Bind the tags to the canvas every time new template is created."""
        for i in range(0, self.ds.iterator):
            strng = "token_"+str(i)
            self.Page.tag_bind(strng, "<ButtonPress-1>", self.drag_start)
            self.Page.tag_bind(strng, "<ButtonRelease-1>", self.drag_stop)
            self.Page.tag_bind(strng, "<B1-Motion>", self.drag)
            self.Page.tag_bind(strng, "<Button-3>", self.resize)

    def remove_text(self):
        """Remove the Text from the canvas"""
        self.Page.delete(self.tag)
        for i, key in enumerate(self.text_fields):
            self.text_fields[i].place_forget()
            self.texts[i].place_forget()

    def config_text(self):
        """Change the Text of the Canvas"""
        all =[]
        for i, key in enumerate(self.text_fields):
            a = self.text_fields[i].get()
            all.append(a)
        if self.tag:
            self.Page.itemconfigure(self.tag, activefill=all[0], activestipple=all[1], anchor=all[2],
                                    angle=all[3], disabledfill=all[4], disabledstipple=all[5], fill=all[6],
                                    font=all[7], justify=all[8], offset=all[9], state=all[10],
                                    stipple=all[11], tags=all[12], text=all[13], underline=all[14], width=all[15])
        else:
            num = self.ds.iterator + 1
            self.ds.iterator = num
            token = "token_"+str(num)
            self.Page.create_text(activefill=all[0], activestipple=all[1], anchor=all[2],
                                    angle=all[3], disabledfill=all[4], disabledstipple=all[5], fill=all[6],
                                    font=all[7], justify=all[8], offset=all[9], state=all[10],
                                    stipple=all[11], tags=all[12], text=token, width=all[14])
            self.Page.tag_bind(token, "<ButtonPress-1>", self.drag_start)
            self.Page.tag_bind(token, "<ButtonRelease-1>", self.drag_stop)
            self.Page.tag_bind(token, "<B1-Motion>", self.drag)
            self.Page.tag_bind(token, "<Button-3>", self.resize)

    def Config_Object(self):
        all = []
        for i, key in enumerate(self.text_fields):
            a = self.text_fields[i].get()
            all.append(a)
        self.Page.itemconfig(self.tag, activefill=all[0], activestipple=all[1], anchor=all[2],
                                angle=all[3], disabledfill=all[4], disabledstipple=all[5], fill=all[6],
                                font=all[7], justify=all[8], offset=all[9], state=all[10],
                                stipple=all[11], tags=all[12], text=all[13], width=all[14])
    def Add_Text(self):
        all = []
        idk = self.Page.itemconfig(self.tag)
        texts,text_fields=[],[]
        y = 0
        for i, key in enumerate(idk.keys()):
            item = Label(self.Text_Label_Frame, text=key, bg="gray", fg="white", font=("Airal", 10))
            item.place(x=0, y=y)
            y += 20
            texts.append(item)
        y = 0
        for i, key in enumerate(idk.keys()):
            item_entry = Entry(self.Text_Label_Frame, width=20)
            item_entry.place(x=100, y=y)
            y += 20
            text_fields.append(item_entry)

    def resize(self, event):
        """To update the widgets"""
        # self.Text_Label_Frame.place_forget()
        # self.Remove_Text_btn = Button(self.Text_Label_Frame, text=" X ", bg="#9c3030", fg="white",bd=0,font=("Arial", 12, "bold"), command=self.Remove_Text)
        self.Remove_Text_btn.place(x=230, y=0)
        # self.config_Text_btn = Button(self.Text_Label_Frame, text=" ->", bg="gray", fg="white",bd=0,font=("Arial", 12, "bold"), command=self.Config_Text)
        self.config_Text_btn.place(x=230, y=40)
        # self.Add_Text_btn = Button(self.Text_Label_Frame, text=" + ", bg="#309c30", fg="white", bd=0,font=("Arial", 12, "bold"), command=self.Add_Text)
        self.Add_Text_btn.place(x=230, y=80)

        item = self.Page.find_closest(event.x, event.y)[0]
        self.tag = self.Page.gettags(item)[0]
        print(self.tag)
        idk = self.Page.itemconfigure(self.tag)
        self.texts, self.text_fields = [], []
        y = 0
        for i, key in enumerate(idk.keys()):
            item = Label(self.Text_Label_Frame, text=key, bg="gray", fg="white", font=("Airal", 10))
            item.place(x=0, y=y)
            y += 20
            self.texts.append(item)
        item = Label(self.Text_Label_Frame, text=" X ", bg="gray", fg="white", font=("Airal", 10))
        item.place(x=0, y=y)
        y += 20
        self.texts.append(item)
        item = Label(self.Text_Label_Frame, text=" y ", bg="gray", fg="white", font=("Airal", 10))
        item.place(x=0, y=y)
        self.texts.append(item)
        y = 0
        for i, key in enumerate(idk.keys()):
            config = self.Page.itemcget(self.tag, key)
            item_entry = Entry(self.Text_Label_Frame, width=20, bd=0)
            item_entry.place(x=100, y=y)
            item_entry.insert(0, config)
            y += 20
            self.text_fields.append(item_entry)
        coors = self.Page.coords(self.tag)
        item = Entry(self.Text_Label_Frame, width=20, bd=0)
        item.place(x=100, y=y)
        y += 20
        item.insert(0, coors[0])
        self.text_fields.append(item)
        item = Entry(self.Text_Label_Frame, width=20, bd=0)
        item.place(x=100, y=y)
        item.insert(0, coors[1])
        self.text_fields.append(item)

        print(coors,len(self.text_fields))
    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        item = self.Page.find_closest(event.x, event.y)[0]
        tag = self.Page.gettags(item)[0]
        print(tag)
        # print(tag)
        self._drag_data["item"] = tag
        self.Page.focus(tag)
        if 'outline' in self.Page.itemconfigure(tag):
            self.Page.itemconfigure(self._drag_data["item"], outline="black")
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        if 'outline' in self.Page.itemconfigure(self._drag_data["item"]):
            self.Page.itemconfigure(self._drag_data["item"], outline="")
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.Page.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        self.Obj.x1_entry.delete(0, 'end')
        self.Obj.x1_entry.insert(0, str(event.x))
        self.Obj.y1_entry.delete(0, 'end')
        self.Obj.y1_entry.insert(0, str(event.y))

    def Prev(self):
        '''To move to Previous templates.'''
        self.prev_btn.config(command=self.ds.prev_Design)
        self.binder()
        # prev_btn.config(command=Prev)

    def To_Ps(self,file_name,color="color"):
        '''Saves the template as .ps (PostScript) file'''
        self.Page.postscript(file=file_name, colormode=color, height=1000)

    def To_Pdf(self,file_name):
        '''Saves the template as .pdf (Portable Digital Format) file'''
        self.To_Ps(file_name)
        pdf = FPDF()
        pdf.add_page()
        pdf.output(file_name, "F")

    # New File option
    def New_File(self):
        global opened
        opened = False

        self.Page.delete("all")
        self.root.title("New File")

    def Open_File(self):
        # Delete previous data
        self.Page.delete("all")
        # Geting the file
        file = filedialog.askopenfile(initialdir="C:/Users/ADMIN/Desktop", title="Open",
                                      filetypes=(("Document Files", "*.DOCX"), ("All Files", "*.*"), ("Post Script File", "*.ps")))
        if file:
            global opened
            opened = file
        # updating the status
        file_name = file
        file_name = file_name.replace("C:/", "")
        self.root.title(file_name)
        # Status_bar.config(text=f"{file_name}       ")
        # open the file
        file = open(file, 'r')
        file_data = file.read()
        self.Page.insert(0, file_data)
        # closing the file
        file.close()

    def Save_File(self):
        global opened
        if opened:
            file = open(opened, "w")
            # file.write(Page.get(0, END))
            file.close()
        else:
            self.Save_As_File()

    def Save_As_File(self):
        file = filedialog.asksaveasfile(defaultextension=".*", initialdir="C:", title="Save File", filetypes=(
        ("Text Files", "*.txt"), ("Document Files", "*.DOCX"), ("All Files", "*.*"), ("Post Script Files", "*.ps")))
        if file:
            # Update the status
            name = file
            name = name.name
            file= name
            name = name.replace("C:/Users/hp/PycharmProjects/Resumr2/", "")
            # self.Page.update()
            self.root.title(f'{name}')
            # Save the file
            self.To_Ps(name)
            # file = open(file, "w")
            # file.write(Page.get(0,END))
            # file.close()
    def light(self):
        '''Light Theme'''
        back = "white"
        self.frame_1.config(bg=back)
        self.frame_2.config(bg=back)
        self.frame_3.config(bg=back)
        self.panned_window.config(bg="#cccccc")
        self.Page.config(bg="white")
        self.Apperance_btn.config(relief=RIDGE,command=self.dark)
    def dark(self):
        '''Dark Theme'''
        back = "#2e2e2e"
        self.frame_1.config(bg=back)
        self.frame_2.config(bg=back)
        self.frame_3.config(bg=back)
        self.panned_window.config(bg="#cccccc")
        self.Page.config(bg="#616161")
        self.Apperance_btn.config(relief=GROOVE,command=self.light)

    def Object(self,i):
        self.Rect_label = LabelFrame(self.frame_1, text="[_]")
        self.Rect_label.pack(fill=BOTH, expand=1)  # place(relx=0.1,rely=0.25)
        self.Obj = Objects(self.Rect_label,self.Page,i)
        if i == 0:
            self.draw_rect_btn.config(command=lambda :self.unpack(i))
            self.Obj.add_rect()
        elif i == 1:
            self.Obj.add_line()
            self.draw_line_btn.config(command=lambda :self.unpack(i))
        else:
            self.Obj.add_oval()
            self.draw_circle_btn.config(command=lambda :self.unpack(i))

    def unpack(self,i):
        self.Rect_label.pack_forget()
        if i == 0:
            self.draw_rect_btn.config(command=lambda :self.Object(i))
        elif i == 1:
            self.draw_line_btn.config(command=lambda :self.Object(i))
        elif i == 2:
            self.draw_circle_btn.config(command=lambda :self.Object(i))

class Objects:
    i=0
    def __init__(self,frame,canvas,i):
        self.label_frame = frame
        self.canvas= canvas

        # Row 1
        x1_label = Label(self.label_frame, text="X1:")
        x1_label.grid(row=0, column=0)
        self.x1_entry = Entry(self.label_frame, width=5)
        self.x1_entry.grid(row=0, column=1)
        self.x1_entry.insert(0,0)
        x2_label = Label(self.label_frame, text="X2:")
        x2_label.grid(row=0, column=2)
        self.x2_entry = Entry(self.label_frame, width=5)
        self.x2_entry.grid(row=0, column=3)
        self.x2_entry.insert(0,0)
        # Row 2
        y1_label = Label(self.label_frame, text="Y1:")
        y1_label.grid(row=1, column=0)
        self.y1_entry = Entry(self.label_frame, width=5)
        self.y1_entry.grid(row=1, column=1)
        self.y1_entry.insert(0,0)
        y2_label = Label(self.label_frame, text="Y2:")
        y2_label.grid(row=1, column=2)
        self.y2_entry = Entry(self.label_frame, width=5)
        self.y2_entry.grid(row=1, column=3)
        self.y2_entry.insert(0,0)
        # Row 3
        fill_label = Label(self.label_frame, text="Fill:")
        fill_label.grid(row=2, column=0)
        fill_col = self.choose_color()
        self.fill_entry = Entry(self.label_frame, width=5)
        # if fill_col != '':
        self.fill_entry.insert(0, fill_col)
        # fill_entry = Entry(label_frame, text="White", width=5)
        self.fill_entry.grid(row=2, column=1)
        outline_label = Label(self.label_frame, text="Outline:")
        outline_label.grid(row=2, column=2)
        self.outline_entry = Entry(self.label_frame, text="Black", width=5)
        self.outline_entry.grid(row=2, column=3)
        # Row 4
        self.minMAX_btn = Button(self.label_frame, text=" - ")
        self.minMAX_btn.grid(row=3, column=2)
        self.obJects = []
        add_obj_btn = Button(self.label_frame, text=" > ")
        # list1 = [int(x1_entry.get()),int(y1_entry.get()),int(x2_entry.get()),int(y2_entry.get()),fill_entry.get(),outline_entry.get()]
        add_obj_btn.grid(row=3, column=3)
        if i == 0:
            add_obj_btn.config(command= self.add_rect)
        elif i == 1:
            add_obj_btn.config(command= self.add_line)
        elif i == 2 :
            add_obj_btn.config(command=self.add_oval)

    def add_rect(self):
        co_ords= [int(self.x1_entry.get()),int(self.y1_entry.get()),int(self.x2_entry.get()),int(self.y2_entry.get())]
        fill_color = self.fill_entry.get()
        outline_color= self.outline_entry.get()
        obj = self.canvas.create_rectangle(co_ords,fill=fill_color,outline=outline_color)
        # add obj reference in list
        Objects.i += 1
        self.obJects.append(obj)
        obj_btn = Button(self.label_frame,text ="obj ",command=lambda :self.update_object(Objects.i-1))
        obj_btn.grid(row=4,column=0,columnspan=3,ipadx=40)
        obj_del_btn = Button(self.label_frame, text="\||/", command=lambda: self.delete_object)
        obj_del_btn.grid(row=4, column=3, columnspan=3)

    def add_line(self):
        co_ords= [int(self.x1_entry.get()),int(self.y1_entry.get()),int(self.x2_entry.get()),int(self.y2_entry.get())]
        fill_color = self.fill_entry.get()
        outline_color= self.outline_entry.get()
        obj = self.canvas.create_line(co_ords,fill=fill_color,outline=outline_color)
        # add obj reference in list
        Objects.i += 1
        self.obJects.append(obj)
        obj_btn = Button(self.label_frame,text ="obj ", command=lambda :self.update_object(Objects.i-1))
        obj_btn.grid(row=4, column=0, columnspan=3)
        obj_del_btn = Button(self.label_frame, text="\||/", command=lambda: self.delete_object)
        obj_del_btn.grid(row=4, column=3, columnspan=3)

    def add_oval(self):
        co_ords= [int(self.x1_entry.get()), int(self.y1_entry.get()), int(self.x2_entry.get()), int(self.y2_entry.get())]
        fill_color = self.fill_entry.get()
        outline_color= self.outline_entry.get()
        obj = self.canvas.create_oval(co_ords, fill=fill_color, outline=outline_color)
        # add obj reference in list
        Objects.i += 1
        self.obJects.append(obj)
        obj_btn = Button(self.label_frame, text ="obj ", command=lambda :self.update_object(Objects.i-1))
        obj_btn.grid(row=4, column=0, columnspan=3)
        obj_del_btn = Button(self.label_frame, text="\||/", command=lambda i: self.delete_object)
        obj_del_btn.grid(row=4, column=3, columnspan=3)

    def delete_object(self, i):
        #remove from canvas
        # item = self.canvas.find_closest(event.x, event.y)[0]
        # self.Page.itemconfigure(self._drag_data["item"],outline="black")
        self.canvas.delete(self.obJects[i])
        #remove from list
        temp = self.obJects[i]
        self.obJects.remove(temp)

    def update_object(self, i):
        # put the data back to form
        self.x1_entry.config(text="")
        self.y1_entry.config(text="")
        self.x2_entry.config(text="")
        self.y2_entry.config(text="")
        self.fill_entry.config(text="")
        self.outline_entry.config(text="")
        # Pass new co-ords
        coords = []#int(self.x1_entry.get()),int(self.y1_entry.get()),int(self.x2_entry.get()),int(self.y2_entry.get())]
        # update to canvas
        self.canvas.coords(self.obJects[i], coords)
        self.canvas.itemconfig(self.obJects[i],fill="", outline="")
    def choose_color(self):
        col = colorchooser.askcolor()
        return col[1]
    def Minimize(self):
        self.label_frame.grid_forget()
        self.minMAX_btn.config(text=" + ")
'''
# retrieving from database
conn = sqlite3.connect("basic.db")
cursor= conn.cursor()
x=cursor.execute(''''SELECT * FROM information WHERE first_name = "Gaurav"'''').fetchall()
Z= [y for y in x]
# Variables
fname,lname,email,lindin,no1,no2,add1,add2= Z[0]
x = cursor.execute(''''SELECT * FROM education''''').fetchall()
z = [y for y in x]
edu = z
x = cursor.execute(''''SELECT * FROM work_info'''').fetchall()
skills = cursor.execute(''''SELECT * FROM interests''''').fetchall()
ach = cursor.execute(''''SELECT * FROM achievements'''').fetchall()
conn.close()
global opened,rect,line,oval
opened=False
rect=line=oval=None
# Main Frame
Main_Frame =Frame(root)
Main_Frame.pack(pady=5)
# Scroll Bar
scroll_bar = Scrollbar(Main_Frame)
scroll_bar.pack(side=RIGHT,fill=Y)
# Horizontal scrollbar
Horizontal_scroll=Scrollbar(Main_Frame,orient='horizontal')
Horizontal_scroll.pack(side=BOTTOM,fill=X)
# Canvas
Page=Canvas(Main_Frame,bg="white",width=600,height=600,scrollregion=(0,0,500,400),yscrollcommand=scroll_bar.set,xscrollcommand=Horizontal_scroll.set,bd=2)
# Text box
# Page = Text(Main_Frame,width=80,height=40,undo=True,selectbackground="#fff280",selectforeground="gray",wrap="none",yscrollcommand=scroll_bar.set,xscrollcommand=Horizontal_scroll.set,bd=2)
Page.pack()
# Configuring scroll bar
scroll_bar.config(command=Page.yview)
Horizontal_scroll.config(command=Page.xview)
# Status bar
Status_bar = Label(root,text=" Ready      ",anchor="e")
Status_bar.pack(fill=X,side=BOTTOM,ipady = 2)
# in_frame= Frame(Page,bg="gray",width=300,height=600)
# in_frame.pack(padx=20,pady=20)
'''
'''
def Save_as_Docx_File():
    doc = Document()
    doc.add_heading("Name",1)
    doc.add_heading("Email", 3)
    doc.add_heading("Contact", 3)
    doc.add_heading("Linkedin", 3)
    doc.add_paragraph("Describe yourself")
    doc.add_heading("Education",4)
    doc.add_heading("Achievements",4)
    doc.add_heading("Technical Experience",4)
    doc.add_heading("KEY SKILLS",4)
def colourchoice():
    color = colorchooser.askcolor()[1]
    return color

def Bold():
    B_font=font.Font(Page,Page.cget("font"))
    B_font.config(weight="Bold")

    Page.tag_config("bold",font=B_font)
    current_tags=Page.tag_names("sel.first")
    if "bold" in current_tags:
        Page.tag_remove("bold","sel.first","sel.last")
    else:
        Page.tag_add("bold","sel.first","sel.last")
def Italics():
    I_font = font.Font(Page, Page.cget("font"))
    I_font.config(slant="italic")

    Page.tag_config("italics", font=I_font)
    current_tags = Page.tag_names("sel.first")
    if "italics" in current_tags:
        Page.tag_remove("italics", "sel.first", "sel.last")
    else:
        Page.tag_add("italics", "sel.first", "sel.last")
def Print():
    file = None
    if file:
        # win32ctypes.pywin32.win32api.ShellExecute(0,"print",file,None,".",0)
        pass
'''

if __name__ == "__main__":
    t = Template_Editor()

