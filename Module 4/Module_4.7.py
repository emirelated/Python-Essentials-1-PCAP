""" This module is about exception handling. """

try:
    pass
	# This is a place where
	# you can do smt
    # without asking for permission.
except:
    pass
	# This is a place exclusively
    # to ask for pardon.

value = None
try:
    value = int(input('Type a natural number: '))
    print('The ^-1', value, 'is', 1/value)        
except ValueError:
    print('I don\'t known how to handle what you typed, i was expecting an int')
except ZeroDivisionError:
    print('Please, don\'t try to make a division by zero')
except:
    print('An unexpected error happened, please send us a ticket so we can fix it')


print('Chopped')
