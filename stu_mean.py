import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#================================
#Basic DB stuff

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#=================================================================================
# NOTE:
#Create peeps_avg table was done in the db_builder.py just for convience 
#   (so that if u run stu_mean.py you don't always get the error of an existing database)
#==================================================================================

#Variables

#holds peep info in a list
peepsList = []

#==================================================================================
#Methods 

#calculate averages and puts them in peepsList
def avgCalc():
    #for each ID...
    for each in range(1,11):
        name = ""
        avg = 0
        numCourses = 0
        for nameMark in c.execute("SELECT name, mark FROM peepsTable, coursesTable WHERE peepsTable.id = %d AND coursesTable.id = %d" %(each, each)):
            #assign correct values to variables
            name = nameMark[0]
            numCourses += 1
            #for now avg holds the total score
            avg += nameMark[1]
        #calculate average as a float
        avg = float(avg)/numCourses
        #add people into peepsList for future use
        peepsList.append([name, avg, each])

#puts peeps into peeps_avg table
def insertPeepsAvg():
    #This following part is so I can spam this py.file without worrying about adding to peeps_avg
    idList = []
    for possibleID in c.execute("SELECT id FROM peeps_avg;"):
        print possibleID
        idList.append(possibleID[0])
    for each in peepsList:
        if each[2] not in idList:
            #Basically insert peeps into peeps_avg if they are not already in there; else pass
            c.execute("INSERT INTO peeps_avg VALUES (?,?);", (each[2], each[1]))
        else:
            pass
    print idList

#basic print out the peeps name + averages + ids
def displayPeepsAvg():
    for each in peepsList:
        print "Name: " + each[0] + "\nID: " + str(each[2]) + "\nAverage " + str(each[1]) + "\n\n"      

#update the average of a person by going through the table and recalculating average 
def updateAverage(ID):
    name = ""
    avg = 0
    numCourses = 0
    for nameMark in c.execute("SELECT name, mark FROM peepsTable, coursesTable WHERE peepsTable.id = %d AND coursesTable.id = %d" %(ID, ID)):
        print nameMark
        name = nameMark[0]
        numCourses += 1
        avg += nameMark[1]
    avg = float(avg)/numCourses
    peepsList[ID-1][1] = avg
    c.execute("UPDATE peeps_avg SET average = %s where id = %d;" %(avg,ID))
    print avg

#add course into table and write into csv by appending a row to it 
def addCourse(code, mark, ID):
    c.execute("INSERT INTO coursesTable VALUES (?,?,?);", (code,mark,ID))
    with open("data/courses.csv", "a'") as csvfile:
        writer = csv.DictWriter(csvfile, ["code", "mark", "id"])
        writer.writerow({"code": code, "mark": mark, "id": ID})

#==========================================================

#Initiate/Call Methods 
avgCalc()
insertPeepsAvg()
displayPeepsAvg()
addCourse("Underwater Basket Weaving", 103, 10)
updateAverage(10)
#==========================================================
db.commit() #save changes
db.close()  #close database
