# import TextEditor
class Design():
    def __init__(self,canvas):
        self.canvas= canvas
        self.design_1()
    # Design 1
    def design_1(self):
        self.canvas.delete("all")
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(300, 50, text=name, font=('Airel', 20, "bold"))
        self.canvas.create_text(120, 75, text=email, font=('Helvetica', 10))  # "Email@email.email"
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_text(275, 75, text="(+91)" + no, font=('Helvetica', 10))  # "XXX-XXX-XXXX"
        self.canvas.create_text(420, 75, text=lindin, font=('Helvetica', 10))  # "Linkedin@Username"
        self.canvas.create_line(100, 100, 500, 100)  # Heading line
        self.canvas.create_text(150, 120, text="Describe yourself", font=("Times New Roman", 8))
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(300, 200, text="Your Education", font=('Airel', 8), anchor='w')
        #     y += 20
        self.canvas.create_line(300, 170, 500, 170)  # Education qualification list
        self.canvas.create_text(500, 160, text="Education", font=('Helvetica', 10, "bold"))

        self.canvas.create_line(70, 170, 200, 170)  # Achievement line
        self.canvas.create_text(70, 160, text="Achievements", font=('Airel', 10, "bold"))
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(70, 180, text="Achievements", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(300, 330, 500, 330)  # Work experience line
        self.canvas.create_text(500, 320, text="Technical Experience", font=('Times New Romans', 10, "bold"))
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(300, 350, text="No Experience till Now", font=('Helvetica', 8), anchor="w")
        self.canvas.create_line(50, 440, 200, 440)  # interests/hobbbies line
        self.canvas.create_text(50, 430, text="KEY SKILLS", font=('Helvetica', 10, "bold"))
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(50, 460, text="tt", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(100, 550, 500, 550)  # About you line
        self.canvas.update()
        self.nxt = self.design_2
    # Design 2
    def design_2(self):
        self.canvas.delete("all")
        rect_colour = "#ffc466"
        self.canvas.create_rectangle(10, 0, 160, 1000, fill=rect_colour, outline="")
        self.canvas.create_rectangle(0, 10, 170, 160, fill=rect_colour, outline="")
        self.canvas.create_rectangle(15, 15, 155, 155, fill="#b0afac")
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(80, 175, text=name, font=('Airel', 10, "bold"), justify="center")
        self.canvas.create_text(80, 300, text=email, font=('Helvetica', 10))  # "Email@email.email"
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_line(20, 275, 150, 275)  # Heading line(Contacts)
        self.canvas.create_text(80, 325, text="(+91)" + no, font=('Helvetica', 10))  # "XXX-XXX-XXXX"
        self.canvas.create_text(80, 350, text=lindin, font=('Helvetica', 10))  # "Linkedin@Username"
        self.canvas.create_line(20, 185, 150, 185)  # Heading line
        # text= #"Hi, there this is the template of design 2"
        text = "Describe yourself"  # , this is the texting text for the wraping effect of canvas create text widget"
        self.canvas.create_text(80, 220, text=text, font=("Times New Roman", 8), width=150)

        self.canvas.create_text(400, 60, text="Education", font=('Helvetica', 12, "bold"))
        self.canvas.create_line(300, 70, 500, 70)  # Education qualification list
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(400, 90, text="Your Education", font=('Airel', 8), anchor='w')
        #     y += 20
        self.canvas.create_text(400, 200, text="Achievements", font=('Airel', 12, "bold"))
        self.canvas.create_line(300, 210, 500, 210)  # Achievement line
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(400, 230, text="--Achievements--", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(300, 380, 500, 380)  # Work experience line
        self.canvas.create_text(400, 370, text="Technical Experience", font=('Times New Romans', 12, "bold"))
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 400, text="No Experience till Now", font=('Helvetica', 8), anchor="w")
        self.canvas.create_line(20, 440, 150, 440)  # interests/hobbbies line
        self.canvas.create_text(80, 430, text="KEY SKILLS", font=('Helvetica', 10, "bold"))
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(50, 460, text="tt", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(160, 550, 800, 550)  # About you line
        self.canvas.update()
        self.nxt = self.design_3
        self.prev = self.design_1
    # Design 3
    def design_3(self):
        self.canvas.delete("all")
        rect_colour = "#ffc466"
        points_1 = [100, 0, 0, 100, 0, 120, 120, 0]
        points_2 = [500, 600, 600, 500, 600, 480, 480, 600]
        self.canvas.create_polygon(points_1, fill=rect_colour)
        self.canvas.create_polygon(points_2, fill="red")
        # self.canvas.create_rectangle(100, 100, 260, 150, fill=rect_colour, outline="")
        # self.canvas.create_rectangle(0, 10, 170, 160, fill=rect_colour, outline="")
        self.canvas.create_oval(50, 50, 170, 170, outline=rect_colour, width=5)
        self.canvas.create_oval(550, 550, 450, 450, outline="red", width=5)
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(250, 40, text=name, font=('Airel', 10, "bold"), justify="center")
        self.canvas.create_text(250, 60, text=email, font=('Helvetica', 10))  # "Email@email.email"
        no = "xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.canvas.create_line(200, 140, 500, 140)  # Heading line
        self.canvas.create_text(250, 80, text="(+91)" + no, font=('Helvetica', 10))  # "XXX-XXX-XXXX"
        self.canvas.create_text(250, 100, text=lindin, font=('Helvetica', 10))  # "Linkedin@Username"
        self.canvas.create_line(325, 45, 325, 125)  # Divider line
        # text= #"Hi, there this is the template of design 2"
        text = "Describe yourself"
        self.canvas.create_text(400, 40, text=text, font=("Times New Roman", 8))

        self.canvas.create_text(500, 190, text="Education", font=('Helvetica', 12, "bold"))
        self.canvas.create_line(250, 200, 500, 200)  # Education qualification list
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        self.canvas.create_text(300, 230, text="Your Education", font=('Airel', 8), anchor='w')
        #     y += 20
        self.canvas.create_text(80, 200, text="Achievements", font=('Airel', 12, "bold"))
        self.canvas.create_line(40, 210, 250, 210)  # Achievement line
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(80, 230, text="--Achievements--", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(40, 380, 250, 380)  # Work experience line
        self.canvas.create_text(80, 370, text="Technical Experience", font=('Times New Romans', 12, "bold"))
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(40, 400, text="No Experience till Now", font=('Helvetica', 8), anchor="w")
        self.canvas.create_line(250, 400, 500, 400)  # interests/hobbbies line
        self.canvas.create_text(500, 390, text="KEY SKILLS", font=('Helvetica', 10, "bold"))
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(300, 420, text="tt", font=('Airel', 8), anchor="w")
        # y += 20
        self.canvas.create_line(100, 550, 400, 550, fill="red")  # About you line
        self.canvas.update()
        self.nxt = self.design_4
        self.prev = self.design_2

    def create_table(self,x1, y1, x2, y2, r=25, reverse=False, **Options):
        # x1=425, y1=150, x2= 675, y2= 350
        colour_1 = "#ffc466"
        colour_2 = "#ffd485"
        colour_3 = "#ff5656"
        self.canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=colour_2, outline="")  # (425,175,675,325) I
        self.canvas.create_rectangle(x1 + r, y2 - r, x2 - r, y2, fill=colour_2, outline="")  # (450,325,650,350) II
        self.canvas.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour_2, outline="")  # (425,300,475,350) 3
        self.canvas.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour_2, outline="")  # (625,300,675,350) 2

        self.canvas.create_rectangle(x1 + r, y1, x2 - r, y1 + 2 * r, fill=colour_1, outline="")  # III (450, 200, 650, 150)
        if (reverse):
            self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_3, outline="")  # 1 (425, 150, 475, 200)
            self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_1, outline="")  # 4 (625, 150, 675, 200)
        else:
            self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour_1, outline="")  # 1 (425, 150, 475, 200)
            self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour_3, outline="")  # 4 (625, 150, 675, 200)

    def create_rounded_rectangle(self,x1, y1, x2, y2, r=25, color="#ca94ff"):
        Points = [x1, y1 + r, x1 + r, y1 + r, x1 + r, y1, x2 - r, y1, x2 - r, y1 + r, x2, y1 + r, x2, y2 - r, x2 - r,
                  y2 - r, x2 - r, y2, x1 + r, y2, x1 + r, y2 - r, x1, y2 - r]
        colour = color
        self.canvas.create_polygon(Points, fill=colour, outline="")
        self.canvas.create_oval(x1, y1, x1 + 2 * r, y1 + 2 * r, fill=colour, outline="")  # 1 (425, 150, 475, 200)
        self.canvas.create_oval(x2 - 2 * r, y2 - 2 * r, x2, y2, fill=colour, outline="")  # (625,300,675,350) 2
        self.canvas.create_oval(x1, y2 - 2 * r, x1 + 2 * r, y2, fill=colour, outline="")  # (425,300,475,350) 3
        self.canvas.create_oval(x2 - 2 * r, y1, x2, y1 + 2 * r, fill=colour, outline="")  # 4 (625, 150, 675, 200)

    # Design 4
    def design_4(self):
        self.canvas.delete("all")
        self.create_rounded_rectangle(20, 20, 220, 800, r=15)
        self.create_rounded_rectangle(30, 30, 210, 180, r=20, color="#e1c2ff")
        self.create_rounded_rectangle(30, 200, 210, 350, r=10, color="#cf9eff")
        name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
        email = "email@email.com"
        lindin = "linkedin/username"
        self.canvas.create_text(120, 220, text=name, font=('Airel', 10, "bold"))
        no = "xxx-xxx-xxxx,xxx-xxx-xxxx"  # str(no1)
        # if no2 != 0:
        #     no = str(no1)+",\n"+str(no2)
        self.create_rounded_rectangle(30, 400, 210, 550, r=15, color="#cf9eff")
        # self.canvas.create_line(200, 140, 500, 140)  # Heading line
        self.canvas.create_text(120, 420, text=email, font=('Helvetica', 10))  # "Email@email.email"
        self.canvas.create_text(120, 460, text="(+91)" + no, font=('Helvetica', 10), width=110)  # "XXX-XXX-XXXX"
        self.canvas.create_text(120, 500, text=lindin, font=('Helvetica', 10))  # "Linkedin@Username"
        self.canvas.create_line(40, 230, 200, 230)  # Divider line
        text = "Decribe yourself Hi, there this is the template of design 2 Describe yourself"
        self.canvas.create_text(120, 260, text=text, font=("Times New Roman", 8), width=150)

        self.reate_table(250, 20, 770, 220)
        self.canvas.create_text(500, 40, text="Education", font=('Helvetica', 12, "bold"))
        # Collecting data in list
        # y = 200
        # for i,info in enumerate(edu):
        #     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
        txt = "Hi, there this is the template of design 4 Describe yourself,qwertyuioplkjhgfdsazxcv bnmmmmkiijnhyygvrdzwwwa"
        self.canvas.create_text(400, 80, text=txt, font=('Airel', 8), anchor='w', width=400)
        #     y += 20

        self.create_table(250, 220, 770, 420, reverse=True)
        self.canvas.create_text(500, 240, text="Achievements", font=('Airel', 12, "bold"))
        # self.canvas.create_line(40, 210, 250, 210)  # Achievement line
        # y = 180
        # for i,info in enumerate(ach):
        #     achs = "~ "+info[0]
        self.canvas.create_text(400, 280, text=txt, font=('Airel', 8), anchor="w", width=400)
        # y += 20

        self.create_table(250, 420, 770, 620)
        # self.canvas.create_line(40, 380, 250, 380)  # Work experience line
        self.canvas.create_text(500, 440, text="Technical Experience", font=('Times New Romans', 12, "bold"))
        # if list.length=0 => print("No data")
        # if(len(x) == 0):
        self.canvas.create_text(400, 480, text="No Experience till Now", font=('Helvetica', 8), anchor="w", width=400)

        self.create_table(250, 620, 770, 800, reverse=True)
        # self.canvas.create_line(250, 400, 500, 400)  # interests/hobbbies line
        self.canvas.create_text(500, 640, text="KEY SKILLS", font=('Helvetica', 10, "bold"))
        # y=460
        # for i,info in enumerate(skills[0]):
        #     tt =''
        #     if (info != '-') or (info != " "):
        #         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
        self.canvas.create_text(400, 680, text="tt", font=('Airel', 8), anchor="w", width=400)
        # y += 20
        self.canvas.create_line(300, 800, 600, 800, fill="red")  # About you line
        self.canvas.update()
        self.prev = self.design_3
