# simple student system !

import sqlite3
import sys
from tkinter import *
import time



while True:
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    def createTable():
        cursor.execute("CREATE TABLE IF NOT EXISTS students(name TEXT,surname TEXT,number INT,students note TEXT)")


    def addStudents(name, surname, number, note):
        cursor.execute("INSERT INTO students VALUES('{} ','{}','{}','{}')".format(name, surname, number, note))
        con.commit()
        con.close()


    createTable()
    print("""
    
________________________________

Uniwersytecki System Studentów

1 -> Dodaj studenta
2 -> Wyjście z systemu
    """)
    selection = input("Wybierz opcję 1 lub 2 : ")
    if selection == "1":
        name = str(input("Imię    : "))
        surname = str(input("Nazwisko : "))
        number = int(input("Numer  : "))
        note = str(input("Notatka    : "))
        addStudents(name, surname, number, note)
    elif selection == "2":
        sys.exit()
