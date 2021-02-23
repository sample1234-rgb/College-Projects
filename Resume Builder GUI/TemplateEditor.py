from tkinter import *
from tkinter import filedialog, font, colorchooser, messagebox, ttk
import os, sys, sqlite3
from docx import Document
from fpdf import FPDF
import Designs

class TemplateEditor:
    def __init__(self):
        # self.root =frame
        self.root = Tk()
        self.root.title("Template Editor")
        self.root.iconbitmap("curriculum-vitae.ico")
        self.root.geometry(f"{self.root.winfo_screenwidth()-3}x{self.root.winfo_screenheight()-3}+0+0")
        self.Mark = True
        self.wm,self.tag = None, None
        self.texts, self.text_fields = [], []
        self.var = IntVar()
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.text_idk = ["activefill", "activestipple", "anchor", "angle", "disabledfill", "disabledstipple", "fill",
                        "font", "justify", "offset", "state", "stipple", "tags", "text", "underline", "width"]
        self.text_or_object = True
        self.object_idk = ['activedash', 'activefill', 'activeoutline', 'activeoutlinestipple', 'activestipple',
                           'activewidth', 'dash', 'dashoffset', 'disableddash', 'disabledfill', 'disabledoutline',
                           'disabledoutlinestipple', 'disabledstipple', 'disabledwidth', 'fill', 'offset', 'outline',
                           'outlineoffset', 'outlinestipple', 'state', 'stipple', 'tags', 'width']

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

        self.prev_btn = Button(self.frame_2, text="<=", bd=0, command=self.prev)
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

        self.Text_Label_Frame = LabelFrame(self.frame_1, text="Text", bg="gray", fg="white", font=("Arial", 12, "bold"))
        self.Text_Label_Frame.pack(fill=BOTH, expand=1)  # .place(relx=0.1,rely=0.01)
        self.Remove_Text_btn = Button(self.Text_Label_Frame, text=" X ", bg="#9c3030", fg="white", bd=0, font=("Arial", 12, "bold"), command=self.remove_text)
        # self.Remove_Text_btn.place(x=0, y=20)
        self.config_Text_btn = Button(self.Text_Label_Frame, text=" ->", bg="gray", fg="white", bd=0, font=("Arial", 12, "bold"), command=self.config_text)
        # self.config_Text_btn.place(x=0, y=50)
        self.Add_Text_btn = Button(self.Text_Label_Frame, text=" + ", bg="#c0c0c0", fg="white", bd=0, font=("Arial", 12, "bold"), height=10, width=15, command=self.add_text)
        self.Add_Text_btn.place(x=50, y=70)

        self.object_label_frame = LabelFrame(self.frame_11, text="Object", bg="gray", fg="white", font=("Ariel", 10, "bold"))
        self.object_label_frame.pack(fill=BOTH, expand=1)  # .place(relx=0.1,rely=0.1)
        self.Remove_object_btn = Button(self.object_label_frame, text=" X ", bg="#9c3030", fg="white", bd=0,
                                      font=("Arial", 12, "bold"), command=self.remove_text)
        # self.Remove_object_btn.place(x=0, y=20)
        self.config_object_btn = Button(self.object_label_frame, text=" ->", bg="gray", fg="white", bd=0,
                                      font=("Arial", 12, "bold"), command=self.config_object)
        # self.config_object_btn.place(x=0, y=50)
        self.Add_object_btn = Button(self.object_label_frame, text=" + ", bg="#c0c0c0", fg="white", bd=0,
                                   font=("Arial", 12, "bold"), height=10, width=15, command=self.add_object)
        self.Add_object_btn.place(x=50, y=70)
        '''self.draw_rect_btn = Button(self.object_label_frame, text="[]", font=("Times New Roman", 10), relief=RIDGE)#
        self.draw_rect_btn.config(command=self.add_object)#lambda: self.Object(0))
        self.draw_rect_btn.place(x=0, y=0)
        # i=1
        self.draw_line_btn = Button(self.object_label_frame, text=" /", font=("Times New Roman", 10), relief=RIDGE, command=lambda: self.Object(1))
        self.draw_line_btn.place(x=20, y=0)
        # i=2
        self.draw_circle_btn = Button(self.object_label_frame, text="O", font=("Times New Roman", 10), relief=RIDGE, command=lambda: self.Object(2))
        self.draw_circle_btn.place(x=40, y=0)
        '''
        # Panel 3
        file_label_frame = LabelFrame(self.frame_3, text="File", bg="gray", fg="white", font=("Ariel", 12, "bold"))
        file_label_frame.pack(fill=X, expand=1)  # place(relx=0.1,rely=0.01)
        new_btn = Button(file_label_frame, text="New", font=("Times New Roman", 10), relief=RIDGE, command=self.new_file)
        new_btn.pack(fill=X, expand=1)  # padx=5,pady=5)
        open_btn = Button(file_label_frame, text="Open", font=("Times New Roman", 10), relief=RIDGE, command=self.open_file)
        open_btn.pack(fill=X, expand=1)  # padx=5,pady=5)
        save_btn = Button(file_label_frame, text="Save", font=("Times New Roman", 10), relief=RIDGE, command=self.save_file)
        save_btn.pack(fill=X, expand=1)  # padx=10,pady=5)
        save_as_btn = Button(file_label_frame, text="Save As", font=("Times New Roman", 10), relief=RIDGE,command=self.save_as_file)
        save_as_btn.pack(fill=X, expand=1)  # padx=10, pady=5)

        view_label_frame = LabelFrame(self.frame_3, text="View", bg="gray", fg="white", font=('Ariel', 12, "bold"))
        view_label_frame.pack(fill=X, expand=1)  # place(relx=0.1,rely=0.25)
        self.Apperance_btn = Button(view_label_frame, text="Theme", font=("Times New Roman", 10), relief=RIDGE, command=self.dark)
        self.Apperance_btn.pack(fill=X, expand=1)
        self.watermark_btn= Button(view_label_frame, text="Watermark", font=("Times New Roman", 10), relief=RIDGE, command=self.mark)
        self.watermark_btn.pack(fill=X, expand=1)

        self.nxt_btn = Button(self.frame_2, text="=>", width=0, bd=0, command=self.next)
        self.nxt_btn.place(relx=0.95, rely=0.95)
        self.ds = Designs.Design(self.Page)

        self.mark()
        self.binder()  # For making all tokens bind to Events
        self.root.mainloop()

    def mark(self):
        """For the sake of Publicity: added WaterMark text"""
        if self.Mark:
            self.Mark = False
            self.watermark_btn.config(bg="#fedcba",relief=RIDGE)
            self.Page.delete(self.wm)
        else:
            self.Mark = True
            self.watermark_btn.config(bg="#abcdef",relief=GROOVE)
            self.wm = self.Page.create_text(700, 980, text="Made by Resume Builder", font=("Arial Black", 6))

    def next(self):
        """Move to next Template of the range"""
        self.nxt_btn.config(command=self.ds.next_Design)
        self.mark()

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
        # print(tag)
        self.Page.delete(self.tag)
        for i, key in enumerate(self.text_fields):
            self.text_fields[i].place_forget()
            self.texts[i].place_forget()

    def config_text(self):
        """Change the Text of the Canvas"""
        opts = []
        for i, key in enumerate(self.text_fields):
            a = self.text_fields[i].get()
            opts.append(a)
        if self.tag is not None:
            self.Page.itemconfigure(self.tag, activefill=opts[0], activestipple=opts[1], anchor=opts[2],
                                    angle=opts[3], disabledfill=opts[4], disabledstipple=opts[5], fill=opts[6],
                                    font=opts[7], justify=opts[8], offset=opts[9], state=opts[10],
                                    stipple=opts[11], tags=opts[12], text=opts[13], underline=opts[14], width=opts[15])
        else:
            num = self.ds.iterator + 1
            self.ds.iterator = num
            token = "token_"+str(num)
            if(opts[16] == ""):
                x = 100
            else:
                x = float(opts[16])
            if(opts[17] == ""):
                y = 100
            else:
                y = float(opts[17])
            self.Page.create_text(x, y, activefill=opts[0], activestipple=opts[1], anchor=opts[2],
                                    angle=float(opts[3]), disabledfill=opts[4], disabledstipple=opts[5], fill=opts[6],
                                    font=opts[7], justify=opts[8], offset=opts[9], state=opts[10], stipple=opts[11],
                                  tags=token, text=opts[13], underline=int(opts[14]), width=float(opts[15]))
            # self.Page.coords(token,float(opts[16]),float(opts[17]))
            self.Page.tag_bind(token, "<ButtonPress-1>", self.drag_start)
            self.Page.tag_bind(token, "<ButtonRelease-1>", self.drag_stop)
            self.Page.tag_bind(token, "<B1-Motion>", self.drag)
            self.Page.tag_bind(token, "<Button-3>", self.resize)
            self.tag = token

    def config_object(self):
        """Update canvas objects"""
        opts = []
        for i, key in enumerate(self.text_fields):
            a = self.text_fields[i].get()
            opts.append(a)

        if self.tag is not None:
            self.Page.itemconfigure(self.tag, activedash=opts[0], activefill=opts[1], activeoutline=opts[2],
                                    activeoutlinestipple=opts[3], activestipple=opts[4], activewidth=opts[5], dash=opts[6], dashoffset=opts[7],
                                    disableddash=opts[8], disabledfill=opts[9], disabledoutline=opts[10],
                                    disabledoutlinestipple=opts[11], disabledstipple=opts[12], disabledwidth=opts[13],
                                    fill=opts[14], offset=opts[15], outline=opts[16], outlineoffset=opts[17],
                                    outlinestipple=opts[18], state=opts[19], stipple=opts[20], tags=opts[21], width=opts[22])
        else:
            num = self.ds.iterator + 1
            self.ds.iterator = num
            token = "token_" + str(num)

            if (self.var.get() == 1):
                self.Page.create_line(float(opts[23]), float(opts[24]), 100, 100, activedash=opts[0],
                                           activefill=opts[1], activeoutline=opts[2],
                                           activeoutlinestipple=opts[3], activestipple=opts[4], activewidth=opts[5],
                                           dash=opts[6], dashoffset=opts[7],
                                           disableddash=opts[8], disabledfill=opts[9], disabledoutline=opts[10],
                                           disabledoutlinestipple=opts[11], disabledstipple=opts[12],
                                           disabledwidth=opts[13],
                                           fill=opts[14], offset=opts[15], outline=opts[16], outlineoffset=opts[17],
                                           outlinestipple=opts[18], state=opts[19], stipple=opts[20], tags=token,
                                           width=opts[22])
            elif (self.var.get() == 2):
                self.Page.create_rectangle(float(opts[23]), float(opts[24]), 100, 100, activedash=opts[0], activefill=opts[1], activeoutline=opts[2],
                                        activeoutlinestipple=opts[3], activestipple=opts[4], activewidth=opts[5], dash=opts[6], dashoffset=opts[7],
                                        disableddash=opts[8], disabledfill=opts[9], disabledoutline=opts[10],
                                        disabledoutlinestipple=opts[11], disabledstipple=opts[12], disabledwidth=opts[13],
                                        fill=opts[14], offset=opts[15], outline=opts[16], outlineoffset=opts[17],
                                        outlinestipple=opts[18], state=opts[19], stipple=opts[20], tags=token, width=opts[22])
            elif (self.var.get() == 3):
                self.Page.create_polygon(float(opts[23]), float(opts[24]), 100, 100, activedash=opts[0],
                                           activefill=opts[1], activeoutline=opts[2],
                                           activeoutlinestipple=opts[3], activestipple=opts[4], activewidth=opts[5],
                                           dash=opts[6], dashoffset=opts[7],
                                           disableddash=opts[8], disabledfill=opts[9], disabledoutline=opts[10],
                                           disabledoutlinestipple=opts[11], disabledstipple=opts[12],
                                           disabledwidth=opts[13],
                                           fill=opts[14], offset=opts[15], outline=opts[16], outlineoffset=opts[17],
                                           outlinestipple=opts[18], state=opts[19], stipple=opts[20], tags=token,
                                           width=opts[22])
            elif (self.var.get() == 4):
                self.Page.create_oval(float(opts[23]), float(opts[24]), 100, 100, activedash=opts[0],
                                           activefill=opts[1], activeoutline=opts[2],
                                           activeoutlinestipple=opts[3], activestipple=opts[4], activewidth=opts[5],
                                           dash=opts[6], dashoffset=opts[7],
                                           disableddash=opts[8], disabledfill=opts[9], disabledoutline=opts[10],
                                           disabledoutlinestipple=opts[11], disabledstipple=opts[12],
                                           disabledwidth=opts[13],
                                           fill=opts[14], offset=opts[15], outline=opts[16], outlineoffset=opts[17],
                                           outlinestipple=opts[18], state=opts[19], stipple=opts[20], tags=token,
                                           width=opts[22])

            # self.Page.coords(token,float(opts[16]),float(opts[17]))
            self.Page.tag_bind(token, "<ButtonPress-1>", self.drag_start)
            self.Page.tag_bind(token, "<ButtonRelease-1>", self.drag_stop)
            self.Page.tag_bind(token, "<B1-Motion>", self.drag)
            self.Page.tag_bind(token, "<Button-3>", self.resize)

    def add_text(self):
        """Add Text item to canvas"""
        y = 0
        self.Remove_Text_btn.place(x=0, y=400)
        self.config_Text_btn.place(x=30, y=400)
        self.Add_Text_btn.place(x=60, y=400)
        self.Add_Text_btn.config(height=0, width=0, bg="#309c30")

        self.texts, self.text_fields = [], []
        for key in self.text_idk:
            item = Label(self.Text_Label_Frame, text=key, bg="gray", fg="white", font=("Airal", 10))
            item.place(x=0, y=y)
            item_entry = Entry(self.Text_Label_Frame, width=20, bd=0)
            item_entry.place(x=100, y=y)
            y += 20
            self.text_fields.append(item_entry)
            self.texts.append(item)

        item = Label(self.Text_Label_Frame, text=" X ", bg="gray", fg="white", font=("Airal", 10))
        item.place(x=0, y=y)
        item_entry = Entry(self.Text_Label_Frame, width=20, bd=0)
        item_entry.place(x=100, y=y)
        y += 20
        self.text_fields.append(item_entry)
        self.texts.append(item)

        item = Label(self.Text_Label_Frame, text=" y ", bg="gray", fg="white", font=("Airal", 10))
        item.place(x=0, y=y)
        item_entry = Entry(self.Text_Label_Frame, width=20, bd=0)
        item_entry.place(x=100, y=y)
        y += 20
        self.text_fields.append(item_entry)
        self.texts.append(item)
        print(y)
        if self.tag is None:
            self.text_fields[2].insert(0, "center")
            self.text_fields[3].insert(0, "0.0")
            self.text_fields[6].insert(0, "black")
            self.text_fields[7].insert(0, ("Arial", 10))
            self.text_fields[8].insert(0, "left")
            self.text_fields[9].insert(0, "0,0")

            self.text_fields[13].insert(0, "hello world")
            self.text_fields[14].insert(0, -1)
            self.text_fields[15].insert(0, 100)
            self.text_fields[16].insert(0, 200)
            self.text_fields[17].insert(0, 100)

    def add_object(self):
        """Add shape object to canvas"""
        y = 0

        self.Remove_object_btn.place(x=0, y=550)
        self.config_object_btn.place(x=30, y=550)
        self.Add_object_btn.place(x=60, y=550)
        self.Add_object_btn.config(height=0, width=0, bg="#309c30")


        t = Tabs(self.object_label_frame)
        frame_temp = t.frame1
        print(t.notebook.tab(1))
        # new_slider = Scale(self.object_label_frame, bg="gray", fg="white", showvalue=5, width=6, length=150,
        #                    sliderlength=4, highlightthickness=0, troughcolor="black", bd=0, from_=0, to=5,
        #                    orient=HORIZONTAL, variable=self.var)
        # new_slider.place(x=0, y=y)
        y += 0
        for key in self.object_idk:
            item = Label(frame_temp, text=key, bg="gray", fg="white", font=("Arial", 10))
            item.place(x=0, y=y)
            item_entry = Entry(frame_temp, width=20, bd=0)
            item_entry.place(x=150, y=y)
            y += 20
            self.text_fields.append(item_entry)
            self.texts.append(item)

        item = Label(frame_temp, text=" X ", bg="gray", fg="white", font=("Arial", 10))
        item.place(x=0, y=y)
        item_entry = Entry(frame_temp, width=20, bd=0)
        item_entry.place(x=25, y=y)
        y += 20
        self.text_fields.append(item_entry)
        self.texts.append(item)

        item = Label(frame_temp, text=" y ", bg="gray", fg="white", font=("Arial", 10))
        item.place(x=0, y=y)
        item_entry = Entry(frame_temp, width=20, bd=0)
        item_entry.place(x=25, y=y)
        y += 20
        self.text_fields.append(item_entry)

        item = Label(frame_temp, text=" X2 ", bg="gray", fg="white", font=("Arial", 10))
        item.place(x=125, y=y-40)
        item_entry = Entry(frame_temp, width=20, bd=0)
        item_entry.place(x=150, y=y-40)
        y += 20
        self.text_fields.append(item_entry)
        self.texts.append(item)

        item = Label(frame_temp, text=" Y2 ", bg="gray", fg="white", font=("Arial", 10))
        item.place(x=125, y=y-40)
        item_entry = Entry(frame_temp, width=20, bd=0)
        item_entry.place(x=150, y=y-40)
        y += 20
        self.text_fields.append(item_entry)
        self.texts.append(item)
        if self.tag is None:
            self.text_fields[2].insert(0, "black")
            self.text_fields[3].insert(0, "0.0")
            self.text_fields[6].insert(0, "black")
            self.text_fields[7].insert(0, "")
            self.text_fields[8].insert(0, "left")
            self.text_fields[9].insert(0, "0,0")

            self.text_fields[13].insert(0, "")
            self.text_fields[14].insert(0, "black")
            self.text_fields[15].insert(0, 100)
            self.text_fields[16].insert(0, "black")
            self.text_fields[17].insert(0, "0,0")

    def resize(self, event):
        """To update the widgets"""
        self.texts, self.text_fields = [], []

        item = self.Page.find_closest(event.x, event.y)[0]
        self.tag = self.Page.gettags(item)[0]
        # print(self.tag)
        if 'outline' in self.Page.itemconfig(self.tag).keys():
            self.add_object()
            for i, key in enumerate(self.object_idk):
                config = self.Page.itemcget(self.tag, key)
                self.text_fields[i].insert(0, config)
            coors = self.Page.coords(self.tag)
            self.text_fields[23].insert(0, str(coors[0]))
            self.text_fields[24].insert(0, str(coors[1]))
        else:
            self.add_text()
            edit_btn = Button(self.Text_Label_Frame, text="~",command=self.notebook)
            edit_btn.place(x=225,y=260)
            for i, key in enumerate(self.text_idk):
                config = self.Page.itemcget(self.tag, key)
                self.text_fields[i].insert(0, config)
            coors = self.Page.coords(self.tag)
            self.text_fields[16].insert(0, str(coors[0]))
            self.text_fields[17].insert(0, str(coors[1]))

    def notebook(self):
        """Notebook for instant edits"""
        root = Tk()
        root.wm_title("Notebook Editor")
        root.geometry("500x450")
        root.wm_iconbitmap("curriculum-vitae.ico")
        # Create a MainFrame
        Main_Frame = Frame(root)
        Main_Frame.pack(fill=BOTH, expand=1)
        # create a text area
        text_area = Text(Main_Frame, bg="white", width=60, wrap=WORD)
        text_area.place(x=0, y=0)
        text_area.insert('1.0', self.text_fields[13].get())

        def save():
            self.text_fields[13].delete(0, END)
            self.text_fields[13].insert(0, text_area.get("1.0", END))
            exitwindow()

        def select():
            text_area.selection_get()

        def exitwindow():
            msg = messagebox.askquestion("Exiting", "Are you sure to exit the the Notebook")
            if msg:
                root.destroy()

        # Save button
        save_btn = Button(Main_Frame, text=" SAVE ", font=("Times New Roman", 10, "bold"), bg="#6cff6c", bd=0, relief=FLAT, command=save)
        save_btn.place(x=320, y=400)
        # Select all button
        select_all_btn = Button(Main_Frame, text="SELECT", font=("Times New Roman", 10, "bold"), bg="#30c2f2", bd=0, relief=FLAT, command=select)
        select_all_btn.place(x=200, y=400)

        # cancel button
        cancel_btn = Button(Main_Frame, text="CANCEL", font=("Times New Roman", 10, "bold"), bg="#ff3c30", bd=0, relief=FLAT, command=exitwindow)
        cancel_btn.place(x=250, y=400)

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        item = self.Page.find_closest(event.x, event.y)[0]
        tag = self.Page.gettags(item)[0]

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
        '''
        self.Obj.x1_entry.delete(0, 'end')
        self.Obj.x1_entry.insert(0, str(event.x))
        self.Obj.y1_entry.delete(0, 'end')
        self.Obj.y1_entry.insert(0, str(event.y))'''

    def prev(self):
        """To move to Previous templates."""
        self.prev_btn.config(command=self.ds.prev_Design)
        # self.binder()
        # prev_btn.config(command=Prev)

    def to_ps(self, file_name, color="color"):
        """Saves the template as .ps (PostScript) file"""
        self.Page.postscript(file=file_name, colormode=color, height=1000)

    def to_pdf(self, file_name):
        """Saves the template as .pdf (Portable Digital Format) file"""
        self.to_ps(file_name)
        pdf = FPDF()
        pdf.add_page()
        pdf.output(file_name, "F")

    # New File option
    def new_file(self):
        global opened
        opened = False

        self.Page.delete("opts")
        self.root.title("New File")

    def open_file(self):
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

    def save_file(self):
        global opened
        if opened:
            file = open(opened, "w")
            # file.write(Page.get(0, END))
            file.close()
        else:
            self.save_as_file()

    def save_as_file(self):
        file = filedialog.asksaveasfile(defaultextension=".*", initialdir="C:", title="Save File", filetypes=(
        ("Text Files", "*.txt"), ("Document Files", "*.DOCX"), ("All Files", "*.*"), ("Post Script Files", "*.ps")))
        if file:
            # Update the status
            name = file
            name = name.name
            # file = name
            name = name.replace("C:/Users/hp/PycharmProjects/Resumr2/", "")
            # self.Page.update()
            self.root.title(f'{name}')
            # Save the file
            self.to_ps(name)
            # file = open(file, "w")
            # file.write(Page.get(0,END))
            # file.close()

    def light(self):
        """Light Theme"""
        back = "white"
        self.frame_1.config(bg=back)
        self.frame_2.config(bg=back)
        self.frame_3.config(bg=back)
        self.panned_window.config(bg="#cccccc")
        self.Page.config(bg="white")
        self.Apperance_btn.config(relief=RIDGE,command=self.dark)

    def dark(self):
        """Dark Theme"""
        back = "#2e2e2e"
        self.frame_1.config(bg=back)
        self.frame_2.config(bg=back)
        self.frame_3.config(bg=back)
        self.panned_window.config(bg="#cccccc")
        self.Page.config(bg="#616161")
        self.Apperance_btn.config(relief=GROOVE, command=self.light)

    def Object(self, i):
        self.Rect_label = LabelFrame(self.frame_1, text="[_]")
        self.Rect_label.pack(fill=BOTH, expand=1)  # place(relx=0.1,rely=0.25)
        self.Obj = Objects(self.Rect_label, self.Page, i)
        if i == 0:
            self.draw_rect_btn.config(command=lambda: self.unpack(i))
            self.Obj.add_rect()
        elif i == 1:
            self.Obj.add_line()
            self.draw_line_btn.config(command=lambda: self.unpack(i))
        else:
            self.Obj.add_oval()
            self.draw_circle_btn.config(command=lambda: self.unpack(i))

    def unpack(self, i):
        self.Rect_label.pack_forget()
        if i == 0:
            self.draw_rect_btn.config(command=lambda: self.Object(i))
        elif i == 1:
            self.draw_line_btn.config(command=lambda: self.Object(i))
        elif i == 2:
            self.draw_circle_btn.config(command=lambda: self.Object(i))


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

class Tabs:
    def __init__(self, root):
        self.notebook = ttk.Notebook(root)

        self.frame1 = Frame(self.notebook, width=300, height=500, bg="gray")
        frame2 = Frame(self.notebook, width=300, height=520, bg="red")
        frame3 = Frame(self.notebook, width=300, height=520, bg="lime")
        frame4 = Frame(self.notebook, width=300, height=520, bg="yellow")
        frame5 = Frame(self.notebook, width=300, height=520, bg="yellow")

        self.frame1.pack(fill=BOTH, expand=1)
        frame2.pack(fill=BOTH, expand=1)
        frame3.pack(fill=BOTH, expand=1)
        frame4.pack(fill=BOTH, expand=1)
        frame5.pack(fill=BOTH, expand=1)

        self.notebook.add(self.frame1, text="    --    ")
        self.notebook.add(frame2, text="   [_]   ")
        self.notebook.add(frame3, text="   \u2302   ")
        self.notebook.add(frame4, text="   O    ")
        self.notebook.add(frame5, text="   O    ")

        self.notebook.place(x=0, y=0)

if __name__ == "__main__":
    t = TemplateEditor()

