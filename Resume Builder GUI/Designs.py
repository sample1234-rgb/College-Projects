# import TextEditor
class Design():
    def __init__(self,canvas):
        self.canvas= canvas
        self.designs = ["self.design_1()","self.design_2()","self.design_3()","self.design_4()","self.design_5()","self.design_6()"]
        self.nxtptr = 0
        self.prevptr = 5
        self.iterator= 0
        self.design_5()
    # Design 1
    def design_1(self):
        self.canvas.delete("all")
        i=0
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(300, 50, text=name, font=('Airel', 20, "bold"),tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(120, 75, text=email, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Email@email.email"
        i += 1
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_text(275, 75, text="(+91)" + no, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "XXX-XXX-XXXX"
        i += 1
        self.canvas.create_text(420, 75, text=lindin, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Linkedin@Username"
        i += 1
        self.canvas.create_line(100, 100, 500, 100,tags= ("token_"+str(i)))  # Heading line
        i += 1
        self.canvas.create_text(150, 120, text="Describe yourself", font=("Times New Roman", 8),tags= ("token_"+str(i)))
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(300, 200, text="Your Education", font=('Airel', 8), anchor='w',tags= ("token_"+str(i)))
        i += 1
        #     y += 20
        self.canvas.create_line(300, 170, 500, 170,tags= ("token_"+str(i)))  # Education qualification list
        i += 1
        self.canvas.create_text(500, 160, text="Education", font=('Helvetica', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(70, 170, 200, 170,tags= ("token_"+str(i)))  # Achievement line
        i += 1
        self.canvas.create_text(70, 160, text="Achievements", font=('Airel', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(70, 180, text="Achievements", font=('Airel', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(300, 330, 500, 330,tags= ("token_"+str(i)))  # Work experience line
        i += 1
        self.canvas.create_text(500, 320, text="Technical Experience", font=('Times New Romans', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(300, 350, text="No Experience till Now", font=('Helvetica', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(50, 440, 200, 440,tags= ("token_"+str(i)))  # interests/hobbbies line
        i += 1
        self.canvas.create_text(50, 430, text="KEY SKILLS", font=('Helvetica', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(50, 460, text="tt", font=('Airel', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(100, 550, 500, 550,tags= ("token_"+str(i)))  # About you line
        i += 1
        self.iterator = i
        self.canvas.update()
        self.nxtptr += 1
        self.prevptr = 5
    # Design 2
    def design_2(self):
        self.canvas.delete("all")
        rect_colour = "#ffc466"
        x1 = 120
        y1 = 225
        i=0
        tag = "token_"
        self.canvas.create_rectangle(10, 0, 225, 1000, fill=rect_colour, outline="",tags= (tag+str(i),))#(10,0,y1,Y)
        i += 1
        self.canvas.create_rectangle(0, 10, 235, 210, fill=rect_colour, outline="",tags= (tag+str(i),))#(0,10,y1+10,y1-10)
        i += 1
        self.canvas.create_rectangle(20, 20, 215, 190, fill="#b0afac",tags= (tag+str(i),))#()
        i += 1
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(120, 225, text=name, font=('Airel', 10, "bold"), justify="center",tags= (tag+str(i),))#(x1,y1)
        i += 1
        self.canvas.create_text(120, 350, text=email, font=('Helvetica', 10),tags= (tag+str(i)))  # "Email@email.email" (x1,125+y1)
        i += 1
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_text(120, 375, text="(+91)" + no, font=('Helvetica', 10),tags= (tag+str(i)))  # "XXX-XXX-XXXX" (x1,150+y1)
        i += 1
        self.canvas.create_text(120, 400, text=lindin, font=('Helvetica', 10),tags= (tag+str(i)))  # "Linkedin@Username" (x1,y1+175)
        i += 1
        self.canvas.create_line(20, 235, 210, 235,tags= (tag+str(i)))  # Heading line (20,y1+10,210,y1+10)
        i += 1
        # text= #"Hi, there this is the template of design 2"
        text = "Describe yourself , this is the texting text for the wraping effect of canvas create text widget"
        self.canvas.create_text(120, 270, text=text, font=("Times New Roman", 10), width=200,tags= (tag+str(i)))
        i += 1

        self.canvas.create_text(400, 60, text="Education", font=('Helvetica', 12, "bold"),tags= (tag+str(i)))
        i += 1
        self.canvas.create_line(300, 70, 500, 70,tags= (tag+str(i)))  # Education qualification list
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(400, 90, text="Your Education", font=('Airel', 8), anchor='w',tags= (tag+str(i)))
        i += 1
        #     y += 20
        self.canvas.create_text(400, 200, text="Achievements", font=('Airel', 12, "bold"),tags= (tag+str(i)))
        i += 1
        self.canvas.create_line(300, 210, 500, 210,tags= (tag+str(i)))  # Achievement line
        i += 1
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(400, 230, text="--Achievements--", font=('Airel', 8), anchor="w",tags= (tag+str(i)))
        # y += 20
        i += 1

        self.canvas.create_line(300, 380, 500, 380,tags= (tag+str(i)))  # Projects line
        i += 1
        self.canvas.create_text(400, 370, text="My Projects", font=('Times New Romans', 12, "bold"),tags= (tag+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 400, text="---Projects---", font=('Helvetica', 8), anchor="w",tags= (tag+str(i)))
        i += 1
        self.canvas.create_line(300, 580, 500, 580,tags= (tag+str(i)))  # Work experience line
        i += 1
        self.canvas.create_text(400, 570, text="Technical Experience", font=('Times New Romans', 12, "bold"),tags= (tag+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 600, text="No Experience till Now", font=('Helvetica', 8), anchor="w",tags= (tag+str(i)))
        i += 1

        self.canvas.create_line(20, 690, 210, 690,tags= (tag+str(i)))  # interests/hobbbies line
        i += 1
        self.canvas.create_text(120, 680, text="KEY SKILLS", font=('Helvetica', 10, "bold"),tags= (tag+str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(80, 720, text="tt", font=('Airel', 8), anchor="w",tags= (tag+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(20, 400, 210, 400,tags= (tag+str(i)))  # About you line
        i += 1
        self.iterator = i
        self.canvas.update()

        self.nxtptr = 2
        self.prevptr = 0

        # self.nxt = self.design_3
        # self.prev = self.design_1
    # Design 3
    def design_3(self):
        self.canvas.delete("all")
        rect_colour = "#ffc466"
        points_1 = [100, 0, 0, 100, 0, 120, 120, 0]
        points_2 = [500, 600, 600, 500, 600, 480, 480, 600]
        i=0
        self.canvas.create_polygon(points_1, fill=rect_colour,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_polygon(points_2, fill="red",tags= ("token_"+str(i)))
        i += 1
        # self.canvas.create_rectangle(100, 100, 260, 150, fill=rect_colour, outline="")
        # self.canvas.create_rectangle(0, 10, 170, 160, fill=rect_colour, outline="")
        self.canvas.create_oval(50, 50, 170, 170, outline=rect_colour, width=5,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_oval(550, 550, 450, 450, outline="red", width=5,tags= ("token_"+str(i)))
        i += 1
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(250, 40, text=name, font=('Airel', 10, "bold"), justify="center",tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(250, 60, text=email, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Email@email.email"
        i += 1
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_line(200, 140, 500, 140,tags= ("token_"+str(i)))  # Heading line
        i += 1
        self.canvas.create_text(250, 80, text="(+91)" + no, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "XXX-XXX-XXXX"
        i += 1
        self.canvas.create_text(250, 100, text=lindin, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Linkedin@Username"
        i += 1
        self.canvas.create_line(325, 45, 325, 125,tags= ("token_"+str(i)))  # Divider line
        i += 1
        # text= #"Hi, there this is the template of design 2"
        text = "Describe yourself"
        self.canvas.create_text(400, 40, text=text, font=("Times New Roman", 8),tags= ("token_"+str(i)))
        i += 1

        self.canvas.create_text(500, 190, text="Education", font=('Helvetica', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(250, 200, 500, 200,tags= ("token_"+str(i)))  # Education qualification list
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(300, 230, text="Your Education", font=('Airel', 8), anchor='w',tags= ("token_"+str(i)))
        i += 1
        #     y += 20
        self.canvas.create_text(80, 200, text="Achievements", font=('Airel', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(40, 210, 250, 210,tags= ("token_"+str(i)))  # Achievement line
        i += 1
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(80, 230, text="--Achievements--", font=('Airel', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(40, 380, 250, 380,tags= ("token_"+str(i)))  # Work experience line
        i += 1
        self.canvas.create_text(80, 370, text="Technical Experience", font=('Times New Romans', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(40, 400, text="No Experience till Now", font=('Helvetica', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(250, 400, 500, 400,tags= ("token_"+str(i)))  # interests/hobbbies line
        i += 1
        self.canvas.create_text(500, 390, text="KEY SKILLS", font=('Helvetica', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(300, 420, text="tt", font=('Airel', 8), anchor="w",tags= ("token_"+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(100, 550, 400, 550, fill="red",tags= ("token_"+str(i)))  # About you line
        i += 1
        self.iterator = i
        self.canvas.update()

        self.nxtptr += 1
        self.prevptr = 1
        # self.nxt = self.design_4
        # self.prev = self.design_2

    def create_table(self,x1, y1, x2, y2, r=25, reverse=False, tags=None,**Options):
        # x1=425, y1=150, x2= 675, y2= 350
        colour_1 = "#ffc466"
        colour_2 = "#ffd485"
        colour_3 = "#ff5656"
        self.canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=colour_2, outline="",tags=tags)  # (425,175,675,325) I
        self.canvas.create_rectangle(x1 + r, y2 - r, x2 - r, y2, fill=colour_2, outline="",tags=tags)  # (450,325,650,350) II
        self.canvas.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour_2, outline="",tags=tags)  # (425,300,475,350) 3
        self.canvas.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour_2, outline="",tags=tags)  # (625,300,675,350) 2

        self.canvas.create_rectangle(x1 + r, y1, x2 - r, y1 + 2 * r, fill=colour_1, outline="",tags=tags)  # III (450, 200, 650, 150)
        if (reverse):
            self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_3, outline="",tags= tags)  # 1 (425, 150, 475, 200)
            self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_1, outline="",tags= tags)  # 4 (625, 150, 675, 200)
        else:
            self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_1, outline="",tags= tags)  # 1 (425, 150, 475, 200)
            self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_3, outline="",tags= tags)  # 4 (625, 150, 675, 200)

    def create_rounded_rectangle(self,x1, y1, x2, y2, r=25, color="#ca94ff",tags=None):
        Points = [x1, y1 + r, x1 + r, y1 + r, x1 + r, y1, x2 - r, y1, x2 - r, y1 + r, x2, y1 + r, x2, y2 - r, x2 - r,
                  y2 - r, x2 - r, y2, x1 + r, y2, x1 + r, y2 - r, x1, y2 - r]
        colour = color
        self.canvas.create_polygon(Points, fill=colour, outline="",tags=tags)
        self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour, outline="",tags=tags)  # 1 (425, 150, 475, 200)
        self.canvas.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour, outline="",tags=tags)  # (625,300,675,350) 2
        self.canvas.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour, outline="",tags=tags)  # (425,300,475,350) 3
        self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour, outline="",tags=tags)  # 4 (625, 150, 675, 200)
    def create_blade(self,x1,y1,x2,y2,m,n,rev=False,color="blue",tags=None):
        x= (m*x2 + n*x1)/(m+n)
        if(rev):
            y = y1 - 0.3*abs(y2-y1)
            Points = [x1, y1, x1, y2, x + 10, y2, x - 10, y, x2, y, x2, y1]
        else:
            y = y1 + 0.3*abs(y2-y1)
            Points = [x1,y1,x1,y2,x-10,y2,x+10,y,x2,y,x2,y1]
        self.canvas.create_polygon(Points,fill=color,outline="",tags=tags)
    # Design 4
    def create_pin_line(self,x1,y1,x2,y2,pin_color="blue",pin_outline="",line_color="black",line_width=2,tags=None):
        self.canvas.create_line(x1,y1,x2,y2, fill=line_color, width=line_width, tags=tags)
        self.canvas.create_oval(x1-5,y1-5,x1+5,y1+5, fill=pin_color,outline=pin_outline, tags=tags)
    def create_skillset_scale(self,x1,y1,x2,y2,value=50,fg="#ccdd00",bg="white",width=4,tags=None):
        self.canvas.create_oval(x1 - 20 - 5, y1 - 5, x1 - 20 + 5, y1 + 5, fill=fg, outline="", tags=tags)

        self.canvas.create_line(x1, y1, x2, y2, fill=bg, width=width, tags=tags)
        self.canvas.create_line(x1, y1, x2+value, y1, fill=fg, width=width+2, tags=tags)
    def design_4(self):
        self.canvas.delete("all")
        i=0
        self.create_rounded_rectangle(20, 20, 220, 800, r=15,tags=("token_"+str(i),))
        i += 1
        self.create_rounded_rectangle(30, 30, 210, 180, r=20, color="#e1c2ff",tags=("token_"+str(i),))
        i += 1
        self.create_rounded_rectangle(30, 200, 210, 350, r=10, color="#cf9eff",tags=("token_"+str(i),))
        i += 1
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(120, 220, text=name, font=('Airel', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        no = "xxx-xxx-xxxx,xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.create_rounded_rectangle(30, 400, 210, 550, r=15, color="#cf9eff",tags= ("token_"+str(i)))
        i += 1
        # self.canvas.create_line(200, 140, 500, 140)  # Heading line
        self.canvas.create_text(120, 420, text=email, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Email@email.email"
        i += 1
        self.canvas.create_text(120, 460, text="(+91)" + no, font=('Helvetica', 10), width=110,tags= ("token_"+str(i)))  # "XXX-XXX-XXXX"
        i += 1
        self.canvas.create_text(120, 500, text=lindin, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Linkedin@Username"
        i += 1
        self.canvas.create_line(40, 230, 200, 230,tags= ("token_"+str(i)))  # Divider line
        i += 1
        text = "Decribe yourself Hi, there this is the template of design 2 Describe yourself"
        self.canvas.create_text(120, 260, text=text, font=("Times New Roman", 8), width=150,tags= ("token_"+str(i)))
        i += 1

        self.create_table(250, 20, 770, 220,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(500, 40, text="Education", font=('Helvetica', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        txt = "Hi, there this is the template of design 4 Describe yourself,qwertyuioplkjhgfdsazxcv bnmmmmkiijnhyygvrdzwwwa"
        self.canvas.create_text(400, 80, text=txt, font=('Airel', 8), anchor='w', width=400,tags= ("token_"+str(i)))
        i += 1
        #     y += 20

        self.create_table(250, 220, 770, 420, reverse=True,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(500, 240, text="Achievements", font=('Airel', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # self.canvas.create_line(40, 210, 250, 210)  # Achievement line
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(400, 280, text=txt, font=('Airel', 8), anchor="w", width=400,tags= ("token_"+str(i)))
        i += 1
        # y += 20

        self.create_table(250, 420, 770, 620,tags= ("token_"+str(i)))
        i += 1
        # self.canvas.create_line(40, 380, 250, 380)  # Work experience line
        self.canvas.create_text(500, 440, text="Technical Experience", font=('Times New Romans', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 480, text="No Experience till Now", font=('Helvetica', 8), anchor="w", width=400,tags= ("token_"+str(i)))
        i += 1

        self.create_table(250, 620, 770, 800, reverse=True,tags= ("token_"+str(i)))
        i += 1
        # self.canvas.create_line(250, 400, 500, 400)  # interests/hobbbies line
        self.canvas.create_text(500, 640, text="KEY SKILLS", font=('Helvetica', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(400, 680, text="tt", font=('Airel', 8), anchor="w", width=400,tags= ("token_"+str(i)))
        i += 1
        # y += 20
        self.canvas.create_line(300, 800, 600, 800, fill="red",tags= ("token_"+str(i)))  # About you line
        i += 1
        self.iterator = i
        self.canvas.update()

        self.nxtptr = 4
        self.prevptr = 2
        # self.prev = self.design_3
    def next_Design(self):
        exec(self.designs[self.nxtptr])
        print(self.designs[self.nxtptr])

    def prev_Design(self):
        exec(self.designs[self.prevptr])
        print(self.designs[self.prevptr])
    def design_5(self):
        self.canvas.delete("all")
        i=0
        self.canvas.create_rectangle(0, 0, 800, 350,fill="#dffffd",outline="",tags=("token_"+str(i),))
        i += 1
        self.canvas.create_rectangle(40, 100, 200, 370, fill="#cccccc",outline="",tags=("token_"+str(i),))
        i += 1
        name = "Hey,\nI'm FIRST LAST NAME!"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(120, 400, text=name, font=('Airel', 10, "bold"),width= 200,tags= ("token_"+str(i)))
        i += 1
        text = "Decribe yourself Hi, there this is the template of design 2 Describe yourself"
        self.canvas.create_text(120, 440, text=text, font=("Times New Roman", 8), width=200,tags= ("token_"+str(i)))
        i += 1
        no = "xxx-xxx-xxxx,      xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_text(120, 800, text=email, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Email@email.email"
        i += 1
        self.canvas.create_text(120, 770, text="(+91)" + no, font=('Helvetica', 10), width=110,tags= ("token_"+str(i)))  # "XXX-XXX-XXXX"
        i += 1
        self.canvas.create_text(120, 820, text=lindin, font=('Helvetica', 10),tags= ("token_"+str(i)))  # "Linkedin@Username"
        i += 1
        self.canvas.create_line(40, 850, 760, 850,fill="#dffffd",width=5,tags= ("token_"+str(i)))  # Divider line 1
        i += 1
        self.canvas.create_line(450, 850, 450, 950,fill="#dffffd",width=5,tags= ("token_"+str(i)))  # Divider line 2
        i += 1
        self.canvas.create_line(340, 725, 760, 725, fill="#dffffd",width=2,tags= ("token_"+str(i)))  # E cross lines
        i += 1
        self.canvas.create_line(340, 775, 760, 775, fill="#dffffd",width=2,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(340, 825, 760, 825, fill="#dffffd",width=2,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_line(550, 725, 550, 825, fill="#dffffd",width=2,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(400, 100, text="Education", font=('Helvetica', 12, "bold"),anchor="e",tags= ("token_"+str(i)))
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        txt = "Hi, there this is the template of design 5 Describe yourself,qwertyuioplkjhgfdsazxcv bnmmmmkiijnhyygvrdzwwwa"
        self.canvas.create_text(500, 140, text=txt, font=('Airel', 8),width=400,tags= ("token_"+str(i)))
        i += 1
        #     y += 20
        self.canvas.create_text(400, 240, text="Achievements",anchor="e",font=('Airel', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(500, 280, text=txt, font=('Airel', 8), anchor="center", width=400,tags= ("token_"+str(i)))
        i += 1
        # y += 20

        self.canvas.create_text(400, 360, text="Technical Experience", font=('Times New Romans', 12, "bold"),tags= ("token_"+str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 380, text="No Experience till Now", font=('Helvetica', 8), width=400,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_oval(300, 425, 360, 485, outline="#dffffd",width=4,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_oval(550, 425, 610, 485, outline="#dffffd", width=4,tags=("token_" + str(i)))
        i += 1
        self.canvas.create_oval(300, 525, 360, 585, outline="#dffffd",width=4,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_oval(550, 525, 610, 585, outline="#dffffd",width=4,tags= ("token_"+str(i)))
        i += 1

        self.canvas.create_text(400, 630, text="KEY SKILLS", font=('Helvetica', 10, "bold"),tags= ("token_"+str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(400, 680, text="tt", font=('Airel', 8), anchor="w", width=400,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(40, 870, text="My References", font=('Airel', 12,"bold"), anchor="w",tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(40, 900, text="Reference 1", font=('Airel', 8), anchor="w", width=200,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(40, 930, text="the dataiu boiud qiuwy fiuoqw uftv uqweiu wpeu qfvy quw", font=('Airel', 8), anchor="w", width=200,tags= ("token_"+str(i)))
        i += 1
        self.canvas.create_text(240, 900, text="Reference 2", font=('Airel', 8), anchor="w", width=200,
                                tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(240, 930, text="the dataiu boiud qiuwyfiuoqwuftvuqweiuwpeuqfvyquw", font=('Airel', 8),
                                anchor="w", width=200, tags=("token_" + str(i)))
        i += 1
        # y += 20
        self.iterator = i
        self.canvas.update()

        self.nxtptr = 5
        self.prevptr = 3
    def design_6(self):
        self.canvas.delete("all")
        i = 0
        self.canvas.create_rectangle(0, 0, 300, 1000, fill="#dcdcdc", outline="", tags=("token_" + str(i),))
        i += 1
        self.create_blade(0, 0, 800, 150, 1,1, color="#54c9ff", tags=("token_" + str(i)))
        i += 1
        self.create_blade(800, 1000, 0, 940, 1, 4, rev=True, color="#54c9ff", tags=("token_" + str(i)))
        i += 1
        # self.canvas.create_rectangle(40, 100, 200, 370, fill="#cccccc", outline="", tags=("token_" + str(i),))
        # i += 1
        name = "Hey,\nI'm FIRST LAST NAME!"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(120, 50, text=name, font=('Airel', 20, "bold"),fill="white", width=200, tags=("token_" + str(i)))
        i += 1
        text = "Decribe yourself Hi, there this is the template of design 2 Describe yourself"
        self.canvas.create_text(120, 220, text=text, font=("Times New Roman", 8), width=200, tags=("token_" + str(i)))
        i += 1
        no = "xxx-xxx-xxxx,xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_text(480, 100, text=email, font=('Helvetica', 10),
                                tags=("token_" + str(i)))  # "Email@email.email"
        i += 1
        self.canvas.create_text(600, 100, text="(+91)" + no, font=('Helvetica', 10), width=110,
                                tags=("token_" + str(i)))  # "XXX-XXX-XXXX"
        i += 1
        self.canvas.create_text(720, 100, text=lindin, font=('Helvetica', 10),
                                tags=("token_" + str(i)))  # "Linkedin@Username"
        i += 1
        self.create_pin_line(350,200,350,400, pin_color="#54c9ff",pin_outline="",line_color="#ccddee", line_width=2, tags=("token_" + str(i)))  # Divider line
        i += 1
        self.canvas.create_text(400, 600, text="Education", font=('Helvetica', 12, "bold"), anchor="e",
                                tags=("token_" + str(i)))
        i += 1
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        txt = "Hi, there this is the template of design 5 Describe yourself,qwertyuioplkjhgfdsazxcv bnmmmmkiijnhyygvrdzwwwa"
        self.canvas.create_text(500, 630, text=txt, font=('Airel', 8), width=400, tags=("token_" + str(i)))
        i += 1
        #     y += 20
        self.canvas.create_text(400, 240, text="Achievements", anchor="e", font=('Airel', 12, "bold"),
                                tags=("token_" + str(i)))
        i += 1
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(500, 280, text=txt, font=('Airel', 8), anchor="center", width=400,tags=("token_" + str(i)))
        i += 1
        # y += 20
        self.canvas.create_text(400, 180, text="Technical Experience", font=('Times New Romans', 12, "bold"),
                                tags=("token_" + str(i)))
        i += 1
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(420, 200, text="No Experience till Now", font=('Helvetica', 8), width=400,
                                tags=("token_" + str(i)))
        i += 1

        self.canvas.create_text(80, 600, text="KEY SKILLS", font=('Helvetica', 10, "bold"), tags=("token_" + str(i)))
        i += 1
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(40, 630, text="tt", font=('Airel', 8), anchor="w", width=400, tags=("token_" + str(i)))
        i += 1
        self.create_skillset_scale(80,630,200,630,value=60,fg="#54c9ff", bg="white", width=4, tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(40, 850, text="My References", font=('Airel', 12, "bold"), anchor="w",
                                tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(40, 890, text="Reference 1", font=('Airel', 8), anchor="w", width=200,
                                tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(40, 910, text="the dataiu boiud qiuwy fiuoqw uftv uqweiu wpeu qfvy quw",
                                font=('Airel', 8), anchor="w", width=100, tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(180, 890, text="Reference 2", font=('Airel', 8), anchor="w", width=200,
                                tags=("token_" + str(i)))
        i += 1
        self.canvas.create_text(180, 910, text="the dataiu boiud qiuwy fiuoqw uftv uqweiu wpeu qfvy quw", font=('Airel', 8),
                                anchor="w", width=100, tags=("token_" + str(i)))
        i += 1
        # y += 20
        self.iterator = i
        self.canvas.update()

        self.nxtptr = 0
        self.prevptr = 4