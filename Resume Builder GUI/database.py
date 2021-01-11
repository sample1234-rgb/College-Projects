import sqlite3
connection = sqlite3.connect("Database.db")#'Improved_Version.db')
cur = connection.cursor()
# Tables --> writen in SQL format
#
# # Information Table:
# cur.execute('''CREATE TABLE Information(first_name text,last_name text,email text,linkedin text,cont_id integer NOT NULL ,address_id integer NOT NULL,FOREIGN KEY(cont) RFERENCES Contacts(id),FOREIGN KEY(address_id) RFERENCES Addresses(id),)''')
# # Education Table:
# cur.execute('''CREATE TABLE education(course_name text,institute_name text,passing_year text,score real,others text)''')
# # Work Information:
# cur.execute('''CREATE TABLE work_info(job_title text,company_name text,start_year text,end_year text,others text)''')
# # Interest Table:
# cur.execute('''CREATE TABLE interests(int_1 text,int_2 text,int_3 text,int_4 text,others text)''')
# # Achievement Table:
# cur.execute('''CREATE TABLE achievements(achieve text)''')
#
# cur.execute("INSERT INTO achievements VALUES ('Python level 3')")
# cur.execute("INSERT INTO achievements VALUES ('C/C++ level 2')")
# cur.execute("INSERT INTO achievements VALUES ('Java level 1')")
# cur.execute("INSERT INTO achievements VALUES ('HTML/CSS/JS level 2')")
# cur.execute("INSERT INTO achievements VALUES ('Django level 1')")
# cur.execute("ALTER TABLE information SET phone_no_2=8427932049 WHERE first_name='Gaurav'")
# cur.execute("drop table info")
# connection.commit()
# for i,x in enumerate(cur.execute('''SELECT * FROM information''')):
#     print(i,x,"\n")
# print([x for x in cur.execute('''SELECT first_name FROM info''')])
# print(len(cur.execute('''SELECT * FROM info''')))

# cur.execute('''CREATE TABLE Contact(number integer(10) NOT NULL UNIQUE)''')
# cur.execute('''CREATE TABLE Addresses(address text NOT NULL UNIQUE)''')
# cur.execute('''CREATE TABLE Information(first_name text,last_name text,email text,linkedin text,cont_id integer NOT NULL ,cont_id_2 integer,address_id integer NOT NULL,address_id_2 integer)''')
# cur.execute('''CREATE TABLE Organisation(Name text,Type text)''')
# cur.execute('''CREATE TABLE Education(id NOT NULL PRIMARY KEY AUTOINCREMENT,Course text,org_id integer NOT NULL,Score integer,Passed integer(4) NOT NULL,FOREIGN KEY(org_id) REFERENCES Organisation(id))''')

#cur.execute('''CREATE TABLE Projects(id integer NOT NULL PRIMARY KEY,Name text,duration integer,Current_Version real)''')
# cur.execute('''CREATE TABLE Achievements(id integer NOT NULL PRIMARY KEY,Information text)''')
# cur.execute('''CREATE TABLE Key_Skills(id integer NOT NULL,Name text,Type text)''')
# cur.execute('''CREATE TABLE Experiences(id integer NOT NULL PRIMARY KEY,Job text Not NULL,Company_id integer NOT NULL,Start_year integer(4),Present_designation text,Additional text,Project_id integer NOT NULL,FOREIGN KEY(Company_id) REFERENCES Organisation(id),FOREIGN KEY(Project_id) REFERENCES Projects(id))''')
# number = 6283913449
# cur.execute("INSERT INTO Contact VALUES({})".format(number))
# id = cur.execute("Select oid from Contact where number=6283913449").fetchone()
Add = 'kelliey'
# cur.execute('''INSERT INTO Addresses(address) VALUES("e")''')
a_id_1 = cur.execute("SELECT oid,address FROM Addresses").fetchall()
# a_id_1 = a_id_1
for id in a_id_1:
    if (id[1] == Add):
        a_id_1=id[0]
print(a_id_1)
# for i in id:
#     print(i[0])
# cur.execute("DROP TABLE Contact")
connection.commit()
# for i,n in enumerate(cur.execute('''Select * from Contact''')):
#     print(n)
connection.close()