#!/usr/bin/python
# Filename: while.py
time = 0
number = 23
running = True
while running:
	time = time + 1
	guess = int(raw_input('Enter an integer : '))
	if guess == number:
		print 'Congratulations, you guessed it.'
		print 'You have guessed',time,'times'
		running = False # this causes the while loop to stop
	elif guess < number:
		print 'No, it is a little higher than that.'
	else:
		print 'No, it is a little lower than that.'
else:
	print 'The while loop is over.'
# Do anything else you want to do here
print 'Done'
