#Program to guess your number
import random
import math

number = str(random.randint(1, 10000))
number_found = 0
upper_bound = 10000
lower_bound = 0
turns = 0
print ('Think of a number up to 10000')
while number_found == 0:
	print ('Is your number ' + number + '? (say: yes, higher, or lower)')
	turns += 1
	user_input = input()
	if user_input == 'yes':
		print ('Your number was ' + number)
		print ('I guessed your number in ' + str(turns) + ' turns')
		number_found = 1
	elif user_input == 'higher' and int(number) < upper_bound:
		#if int(number) > lower_bound:
			lower_bound = int(str(number))
			middle = (upper_bound - lower_bound) / 2
			number = str(math.ceil(lower_bound + middle))
	elif user_input == 'lower' and int(number) > lower_bound:
		#if int(number) < upper_bound:
			upper_bound = int(str(number))
			middle = (upper_bound - lower_bound) / 2
			number = str(math.ceil(int(number) - middle))
