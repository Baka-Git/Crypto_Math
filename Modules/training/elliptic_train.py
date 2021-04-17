import random

from elliptic_curve_tools import *
def choose_train_elliptic():
	# TODO mov attack training

	training_types = [
		'is_elliptic',
		'is_point',
		'possible_point_orders',
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


def check_yes_no(user_answer, answer):
	if user_answer == 'Y' and answer:
		print('Correct!\n')
	elif user_answer == 'N' and not answer:
		print('Correct!\n')
	else:
		print('Incorrect!\n')

def check_answer(user_answer, answer):
	if user_answer == answer:
		print('Correct!\n')
	else:
		print(f'Incorrect! The correct answer is {answer}\n')

def elliptic_trainer():

	training_buffer = choose_train_elliptic()

	for training in training_buffer:

		if training == 'is_elliptic':
			answer = check_curve()

			user_answer = input('Is the curve elliptic? Y/N: ')
			while user_answer != 'Y' and user_answer != 'N':
				user_answer = input('Is the curve elliptic? Y/N: ')

			check_yes_no(user_answer, answer)

		if training == 'is_point':
			answer = check_point()

			user_answer = input('Does the point P belong on the given curve? Y/N: ')
			while user_answer != 'Y' and user_answer != 'N':
				user_answer = input('Does the point P belong on the given curve? Y/N: ')

			check_yes_no(user_answer, answer)	

		if training == 'possible_point_orders':
			answer = check_possible_point_orders()

			print('Answer format: a, b, c, ..., z!! One spaces between commas!!\n')
			user_answer = input('What are the possible orders of an EC of the given order? ')

			check_answer(user_answer, answer)


def gen_field():
	prime = [2, 3, 5]

	weights = ( 6, 5, 4) 

	prime_number = random.choices(
					prime,
					weights=weights,
					k=1
				)[0]

	return prime_number ** random.randint(1,3)



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



def check_point():
	random_numbers = []

	for i in range(7):
		value = random.randint(0,20)
		random_numbers.append(value)

	random_numbers[0] = 1
	random_numbers[3] = 1

	field = gen_field()

	point = [ random.randint(0,20), random.randint(0,20) ] 

	print(f"y^2 + {str(random_numbers[1])} * y + {str(random_numbers[2])} * xy = " +
      f"x^3 + {str(random_numbers[4])} * x^2 + {str(random_numbers[5])} * x + {str(random_numbers[6])}")

	print(f"P({point[0]},{point[1]})")
	print(f"Field: F{field}")

	check = is_point_on_elliptic_curve(point[0], point[1], field, random_numbers, True, True)

	return check



def check_possible_point_orders():
	order = random.randint(0,99)

	print(f'EC of order {order}')

	check = possible_orders(str(order), True)

	# remove the brackets
	check = str(check)[1:-1]

	return check
