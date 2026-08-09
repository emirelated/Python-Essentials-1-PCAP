""" We're going to work in functions.
The base principle for this is thinking in functions as a big problem that is divided in little ones, or so called each piece of the problem is going to be a different function.

This is how a function will work

Reserved word 'def' + the body + (arguments):
                    Things that happens inside the function """

def f_func():
    print('Congratz, you called the first builded function')


# Call example of a function
f_func()

""" When you call the function Python remembers the direction of the funcion and calls it .


Python reads from top to bottom, so if you define the function below were it is called you will have an error, per e.g

f_func()

def f_func():
    print('smt')
    
The result of this block will be an error."""

# An example of function with argument

def p_name(name):
    print('Nice to hear from you, ', name)


p_name(input('Tell me your name mate: '))


""" If you send an argument to a function that doesn't require arguments you're going to get a type error per e.g

def funct1():
    print('Hello, i'm a function')
    
and call it like this

funct(5)"""

