import numpy as np
import os
import time
from datetime import datetime
import sqlite3
import sys


class Real_time_fuctions:

    def convert_list(self):
        id_list = []
        name_list = []
        id_number_list = []
        conn = sqlite3.connect('Banco_de_dados.db')
        print('Database open successfully...')

        cursor = conn.execute("SELECT ID, NAME, ID_NUMBER from REGISTER")
        for row in cursor:
            id_list.append(int(row[0]))
            name_list.append(row[1])
            id_number_list.append(int(row[2]))

        print("Change successfully...")
        conn.close()

class Enrollment_functions:

    def make_table(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print('\nDatabase open successfully...')

        conn.execute('''CREATE TABLE REGISTER
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME           TEXT    NOT NULL,
             ID_NUMBER            INT     NOT NULL);''')
        conn.execute('INSERT INTO REGISTER VALUES (0, "USER 0", 00000000)')
        conn.commit()
        print('Table criated successfully...')
        print('\n')
        conn.close()
        #sys.exit(1)

    def create_user(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print ('Database open successfully...')

        print('\n-----------------------------')
        name = input('Type the name: ')
        id_number = input('Type the ID number: ')
        print('-----------------------------\n')

        conn.execute("INSERT INTO REGISTER (NAME,ID_NUMBER) \
              VALUES (?, ?)", (name,id_number))

        conn.commit()
        print('Register saved successfully...')
        print('\n')
        conn.close()





