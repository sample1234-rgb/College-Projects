from tkinter import *
pencere = Tk()
pencere.geometry("{0}x{1}".format(400, 400))

labelFrame = LabelFrame(pencere, width = 400, height = 400)
labelFrame.pack(side="left",fill=BOTH)
canvas = Canvas(labelFrame,relief=SUNKEN)
canvas.config(scrollregion=(0,0,1000,1000))    # halloldu =)

scrollbar = Scrollbar(labelFrame)
scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right",fill=Y)
canvas.pack(side="left",expand=YES,fill=BOTH)

# frame = Frame(canvas,width=100,height=100,bg="white")
# frame.pack(side="top",fill=BOTH)
# canvas.create_window(0,0,window=frame, anchor="nw")
name = "FIRST LAST NAME"  # fname+' '+lname#"FIRST - LAST NAME"
email = "email@email.com"
lindin = "linkedin/username"
canvas.create_text(300, 50, text=name, font=('Airel', 20, "bold"))
canvas.create_text(120, 75, text=email, font=('Helvetica', 10))  # "Email@email.email"
no = "xxx-xxx-xxxx"  # str(no1)
# if no2 != 0:
#     no = str(no1)+",\n"+str(no2)
canvas.create_text(275, 75, text="(+91)" + no, font=('Helvetica', 10))  # "XXX-XXX-XXXX"
canvas.create_text(420, 75, text=lindin, font=('Helvetica', 10))  # "Linkedin@Username"
canvas.create_line(100, 100, 500, 100)  # Heading line
canvas.create_text(150, 120, text="Describe yourself", font=("Times New Roman", 8))
# Collecting data in list
# y = 200
# for i,info in enumerate(edu):
#     n_info = "> "+info[0]+" "+info[1]+"    "+info[2]#+"     "+str(info[3])
canvas.create_text(300, 200, text="Your Education", font=('Airel', 8), anchor='w')
#     y += 20
canvas.create_line(300, 170, 500, 170)  # Education qualification list
canvas.create_text(500, 160, text="Education", font=('Helvetica', 10, "bold"))

canvas.create_line(70, 170, 200, 170)  # Achievement line
canvas.create_text(70, 160, text="Achievements", font=('Airel', 10, "bold"))
# y = 180
# for i,info in enumerate(ach):
#     achs = "~ "+info[0]
canvas.create_text(70, 180, text="Achievements", font=('Airel', 8), anchor="w")
# y += 20
canvas.create_line(300, 330, 500, 330)  # Work experience line
canvas.create_text(500, 320, text="Technical Experience", font=('Times New Romans', 10, "bold"))
# if list.length=0 => print("No data")
# if(len(x) == 0):
canvas.create_text(300, 350, text="No Experience till Now", font=('Helvetica', 8), anchor="w")
canvas.create_line(50, 440, 200, 440)  # interests/hobbbies line
canvas.create_text(50, 430, text="KEY SKILLS", font=('Helvetica', 10, "bold"))
# y=460
# for i,info in enumerate(skills[0]):
#     tt =''
#     if (info != '-') or (info != " "):
#         tt = "> "+info#[0]+" "+info[1]+" "+info[2]+" "+info[3]
canvas.create_text(50, 460, text="tt", font=('Airel', 8), anchor="w")
# y += 20
canvas.create_line(100, 550, 500, 550)  # About you line
canvas.update()
pencere.mainloop()