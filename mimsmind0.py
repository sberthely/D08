############################   IMPORTS  #############################

import sys
import random

tries = 0
length = 0

######################   ADDITIONAL FUNCTIONS  ######################

def evaluate_number(user_number, random_number):
	global tries 
	tries += 1
	if random_number == user_number:
		print("Congratulations. You guessed the correct number in " + str(tries) + " tries.")
	else:
		if random_number > user_number:
			user_number = ask_user_number(False, 'higher')
		elif random_number < user_number:
			user_number = ask_user_number(False, 'lower')
		evaluate_number(user_number, random_number)

def ask_user_number(first_time, higher_lower):
	global length
	while True:
		try:
			if first_time == True:
				user_number = int(input("Guess a " + str(length) + "-digit number: "))
			else:
				user_number = int(input("Try again. Guess a " + higher_lower + " number: "))
		except:
			print("Warning: Integer Value Expected")
			continue

		if len(str(user_number)) > int(length) or user_number < 0:
			print("Provide a positive number of length: {}".format(length))
			continue
		else:
			break

	return user_number

def gen_random():
	global length
	length = get_number_length()
	max_integer = int('9'*int(length))
	random_number = random.randint(0, max_integer)
	return random_number

def get_number_length():
	try:
		return sys.argv[1]
	except:
		return 1

def ask_user_try_again():
	while True:
		try_again = input("Do you want to try again? Yes/No:  \n")
		if try_again in ('Yes', 'yes'):
			return True
		elif try_again in ('No', 'no'):
			return False
		else:
			print("I did not understand what your answer is!!!")
			continue

	return user_number

def mimsmind0_rutine():
	global tries
	tries = 0
	
	print("Let's play the mimsmind0 game.")
	random_number = gen_random()
	print('RANDOM: ', random_number)
	user_number =ask_user_number(True, '')
	evaluate_number(user_number, random_number)
	return ask_user_try_again()


##############################   MAIN  ##############################
def main():

	flag = True
	while flag == True:
		flag = mimsmind0_rutine()
		


if __name__ == '__main__':
	main()