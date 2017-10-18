import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# To do this follow this guidline:
# command = ""          --> first do this to put SQL statements / commands in this string
# c.execute(command)    --> then do this to run SQL statement

#These are your SQL commands
createCourses = "CREATE TABLE coursesTable(code TEXT, mark INTEGER, id INTEGER);"
createPeeps = "CREATE TABLE peepsTable(name TEXT, age INTEGER, id INTEGER);"
createPeeps_Avg = "CREATE TABLE peeps_avg(id INTEGER, average NUMERIC);"
# Now execute your commands
c.execute(createCourses)
c.execute(createPeeps)
c.execute(createPeeps_Avg)

# Now populate your tables by inserting info in
courses = csv.DictReader(open("data/courses.csv"))

for row in courses:
    c.execute("INSERT INTO coursesTable VALUES (?,?,?);", (row['code'], int(row['mark']), int(row['id'])))

peeps = csv.DictReader(open("data/peeps.csv"))

for row in peeps:
    c.execute("INSERT INTO peepsTable VALUES (?,?,?);", (row['name'], int(row['age']), int(row['id'])))

c.execute("SELECT * from coursesTable")
#==========================================================
db.commit() #save changes
db.close()  #close database


