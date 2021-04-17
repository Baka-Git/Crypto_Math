import random

from Modules.training.elliptic_train import elliptic_trainer


def interactive():

	print(f'Running elliptic training')

	quit = False

	while not quit:

		# run desired trainer
		elliptic_trainer()
		
		go_on = input('Next set of questions? (N will quit the program) Y/N: ')
		while go_on != 'Y' and go_on != 'N':
			go_on = input('Next set of questions? (N will quit the program) Y/N: ')

		if go_on == 'N':
			quit = True


