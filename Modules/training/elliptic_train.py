import random

from elliptic_curve_tools import *

def choose_train_elliptic():
	# TODO mov attack training

	training_types = [
		'is_elliptic',
		'is_point',
		'possible_orders',
		'curve_order',
		'add_points',
	]	

	weights = ( 1, 2, 3, 4, 5 )

	random_training = random.choices(
			training_types,
			weights=weights,
			k=10 
		) 

	return random_training


def check_answer(user_answer, answer):
	if user_answer == 'Y' and answer:
		print('Correct!\n')
	elif user_answer == 'N' and not answer:
		print('Correct!\n')
	else:
		print('Incorrect!\n')



def elliptic_trainer():

	training_buffer = choose_train_elliptic()

	for training in training_buffer:

		if training == 'is_elliptic':
			answer = check_curve()

			user_answer = input('Is the curve elliptic? Y/N: ')
			while user_answer != 'Y' and user_answer != 'N':
				user_answer = input('Is the curve elliptic? Y/N: ')

			check_answer(user_answer, answer)


def check_curve():
	will_be_elliptic = random.choice([True,False]) 

	mess_up =random.choice([True,False])

	random_numbers = []

	for i in range(7):
		value = random.randint(0,99)
		random_numbers.append(value)

	if will_be_elliptic:
		random_numbers[0] = 1
		random_numbers[3] = 1

	if mess_up:
		random_numbers[3] = random.randint(2,99)

	check = is_elliptic(random_numbers, True, True)

	if not check:
		if random_numbers[0] == 1:
			print(f"y^2 + {str(random_numbers[1])} * y + {str(random_numbers[2])} * xy = " +
              f"{str(random_numbers[3])} * x^3 + {str(random_numbers[4])} * x^2 + {str(random_numbers[5])} * x + {str(random_numbers[6])}")
		
		elif random_numbers[3] == 1:
			print(f"{str(random_numbers[0])} * y^2 + {str(random_numbers[1])} * y + {str(random_numbers[2])} * xy = " +
            	  f"x^3 + {str(random_numbers[4])} * x^2 + {str(random_numbers[5])} * x + {str(random_numbers[6])}")
		else:
			print(f"{str(random_numbers[0])} * y^2 + {str(random_numbers[1])} * y + {str(random_numbers[2])} * xy = " +
              f"{str(random_numbers[3])} * x^3 + {str(random_numbers[4])} * x^2 + {str(random_numbers[5])} * x + {str(random_numbers[6])}")


	if check != False:
		check = True

	return check
