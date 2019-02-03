import os 
import time
import sys
from datetime import datetime
from fuctions import Enrollment_functions

c = Enrollment_functions()


def loop_secundari():
	print('------------------------------------------------------------------------')
	print('1 -> Table create; 2 -> Adding credits; 3 -> Access counter; 5 -> Exit: ')
	print('------------------------------------------------------------------------')
	a = input()
	y = 1

	while (y):
		if int(a) == 1:
			c.make_table()
			print('\nTable created successfully...')
			a = 0
			main_loop()

		elif int(a) == 2:
			c.adding_credits()
			print('\nCredit added successfully...')
			a = 0
			main_loop()

		elif int(a) == 3:
			c.person_accounts()
			print('\nSomeone passed...')
			a = 0
			main_loop()

		elif int(a) == 5:
			print('\nExiting...')
			a = 0
			main_loop()

		else:
			print('\nBacking to begining')
			loop_secundari()


def main_loop():
	time.sleep(2)
	os.system('clear')
	print('\n------------------------------------')
	print('Para acessar remotamente o servidor!')
	print('Esse é o endereço de ip acessável')
	os.system('hostname -I')
	print('------------------------------------\n')

	x = 1
	while(x):
		print('\n---------------------------')
		print('Welcome to Face Recognition !')
		print('-----------------------------')
		print('\n')
		print('-------------------------------------------------------------------------------')
		print('1 -> New register; 2 -> Face Recognition; 3 -> Edit database; 4 -> Exit:')
		print('-------------------------------------------------------------------------------')
		NUMB_INIT = int(input())
		os.system('clear')

		if NUMB_INIT == 1:#Making new registers
			print('\n')
			c.create_user()
			os.system('python3 01_face_dataset.py')
			os.system('python3 02_face_training.py')
			print('\n\n')

		elif NUMB_INIT == 2: #Begin face recognition
			print('\n-----------------------------------')
			os.system('echo  Face recognition begin at:')
			os.system('date')
			print('-----------------------------------\n\n')

			os.system('echo  >> Logs/log.txt')
			os.system('echo --------------------------------- >> Logs/log.txt')
			os.system('echo Face recognition begin at: >> Logs/log.txt')
			os.system('date  >> Logs/log.txt')
			os.system('echo --------------------------------- >> Logs/log.txt')

			os.system('python3 03_facial.py')

			print('-----------------------------------\n')
			os.system('echo Face recognition close at:')
			os.system('date')
			print('-----------------------------------\n\n')

			os.system('echo  >> Logs/log.txt')
			os.system('echo --------------------------------- >> Logs/log.txt')
			os.system('echo echo Face recognition close at: >> Logs/log.txt')
			os.system('date  >> Logs/log.txt')
			os.system('echo --------------------------------- >> Logs/log.txt')

		elif NUMB_INIT == 3: #Editing database functions
			print('\n')
			loop_secundari()
			os.system('clear')
			print('\n\n')

		elif NUMB_INIT == 4: #Closing
			print('---------------------------')
			print('Closing Face Recognition...')
			print('---------------------------')
			print('\n')
			sys.exit(0)


		else:
			print('\nError: Press a valid number.')

main_loop()

		
	
	