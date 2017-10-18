import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peepsList = []
names = []

def getGrades():
    for each in range(1,11):
        listy = []
        #print "---"
        for i in c.execute("SELECT name, mark FROM peepsTable, coursesTable WHERE peepsTable.id = %d AND coursesTable.id = %d" %(each, each)):
            name = i[0]
            listy.append(i[1])
        names.append(name)
        peepsList.append(listy)

getGrades()

averages = []

def avgCalc():
    for i in peepsList:
        summ = 0
        for j in i:
            summ += j
        averages.append(summ / float(len(i)))

avgCalc()

#print averages

def display():
    for each in range(1, 11):
        print "name: %s, id: %d, average: %f" %(names[each - 1], each, averages[each - 1])

display()

#c.execute("CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)")

def addToAvg():
    for each in range(1, 11):
        c.execute("INSERT INTO peeps_avg VALUES (%d, %f)" %(each, averages[each - 1]))

#addToAvg()

def addRow(course, grade, id):
    c.execute('INSERT INTO coursesTable VALUES ("%s", %d, %d)' %(course, grade, id))

#addRow("greatbooks", 85, 1)

def updateAvgs():
    getGrades()
    avgCalc()
    for each in range(1, 11):
        c.execute("UPDATE peeps_avg SET average = %f WHERE id = %d" %(averages[each - 1], each))

updateAvgs()

#==========================================================
db.commit() #save changes
db.close()  #close database

