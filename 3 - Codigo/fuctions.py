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
        money_list = []
        acess_list = []
        conn = sqlite3.connect('Banco_de_dados.db')
        print('Database open successfully...')

        cursor = conn.execute("SELECT ID, NAME, ID_NUMBER, MONEY, ACCESS from REGISTER")
        for row in cursor:
            id_list.append(int(row[0]))
            name_list.append(row[1])
            id_number_list.append(int(row[2]))
            money_list.append(float(row[3]))
            acess_list.append(int(row[4]))

        print("Change successfully...")
        conn.close()

    def zero_reset(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print('-----------------------------')
        print('Database open successfully...')

        conn.execute('UPDATE REGISTER set ACCESS = 0')
        conn.commit()
        print('Total columns number updates: ', conn.total_changes)
        if conn.total_changes > 0:
            print('Change successfully...')
            print('---------------------------')
        else:
            print('Failed something wrong...')


        print('\n')
        conn.close()

    def creating_logs(self, nome, matricula, credito_1, credito, ref):
        now = datetime.now()
        arq = open('Logs/log.txt', 'a')
        data = []
        data.append('\n-------------------------\n')
        data.append("Date: ")
        data.append(str(now.year))
        data.append(':')
        data.append(str(now.month))
        data.append(':')
        data.append(str(now.day))
        data.append(':')
        data.append(str(now.hour))
        data.append(':')
        data.append(str(now.minute))
        data.append(':')
        data.append(str(now.second))
        if ref == 1:
            data.append(str('\nWelcome: ' + nome))
            data.append(str('\nID Number: ' + matricula))
            data.append('\nMoney remening: ' + str(credito_1))
            data.append('\nMoney before: ' + str(credito))
            data.append('\n------------------------\n')
        elif ref == 2:
            data.append(str('\nAccess denied: ' + nome))
            data.append(str('\nID Number: ' + matricula))
            data.append('\nMoney remening: ' + str(credito_1))
            data.append('\nMoney before: ' + str(credito))
            data.append('\n------------------------\n')
        elif ref == 3:
            data.append('\nAccess numbers expired...')
            data.append(str('\nName ' + nome))
            data.append(str('\nID Number: ' + matricula))
            data.append('\nMoney: ' + str(credito))
            data.append('\n------------------------\n')

        arq.writelines(data)
        arq.close()

class Enrollment_functions:

    def person_accounts(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print('\nDatabase open successfully...')
        print('---------------------------')
        MATRICULA1 = input('Type your registrations number: ')

        conn.execute('UPDATE REGISTER set ACCESS = ACCESS+1 WHERE  ID_NUMBER=' + MATRICULA1)
        conn.commit()
        print('Numero total de colunas atualizadas: ', conn.total_changes)
        if conn.total_changes > 0:
            print('Change successfully...')
        else:
            print('Failed something wrong...')

        print('\n')
        # os.system('clear')
        conn.close()
        #sys.exit(1)

    def adding_credits(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print('\nDatabase open successfully...')

        matricula = input('Which registrations number:  ')
        dinheiro = input('Who much money do you wanna put ?: ')
        float(dinheiro)
        conn.execute("UPDATE REGISTER set MONEY = MONEY +" + dinheiro + " WHERE  ID_NUMBER = " + matricula)
        conn.commit()
        print('\nTotal columns number updates: ', conn.total_changes)
        if conn.total_changes > 0:
            print('Change successfully...')
        else:
            print('Failed something wrong...')

        print('\n')
        # os.system('clear')
        conn.close()
        #sys.exit(1)

    def make_table(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print('\nDatabase open successfully...')

        conn.execute('''CREATE TABLE REGISTER
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME           TEXT    NOT NULL,
             ID_NUMBER            INT     NOT NULL,
             MONEY        	REAL NOT NULL,
             ACCESS         INT NOT NULL);''')
        conn.execute('INSERT INTO REGISTER VALUES (0, "USER 0", 00000000 , 00.00, 0)')
        conn.commit()
        print('Table criated successfully...')
        print('\n')
        conn.close()
        os.system('sudo chmod 777 Banco_de_dados.db')
        #sys.exit(1)

    def create_user(self):
        conn = sqlite3.connect('Banco_de_dados.db')
        print ('Database open successfully...')

        print('\n-----------------------------')
        name = input('Type the name: ')
        id_number = input('Type the ID number: ')
        print('-----------------------------\n')
        money = 00.00
        access = 0

        conn.execute("INSERT INTO REGISTER (NAME,ID_NUMBER,MONEY,ACCESS) \
              VALUES (?, ?, ?, ?)", (name,id_number,money,access))

        conn.commit()
        print('Register saved successfully...')
        print('\n')
        conn.close()





