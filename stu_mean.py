import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peepsList = []

def avgCalc():
    for each in range(1,11):
        listy = []
        print "---"
        for i in c.execute("SELECT name, mark FROM peepsTable, coursesTable WHERE peepsTable.id = %d AND coursesTable.id = %d" %(each, each)):
            print i
            listy.append(i[1])
        #print listy
avgCalc()

#==========================================================
db.commit() #save changes
db.close()  #close database

