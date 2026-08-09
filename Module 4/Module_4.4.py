""" This module is about the use of variables, local, globals, buildeds or from a module. """

# Function that is going to print an error because you cant access the variable

""" 
def function():
    x = 1
    return None
    
    
print(x) # x is not accessible from the global environment because it was defined from as a local variable in the function """

# In the case we use a global variable in a function it CAN access it, lets build an example

def eg_function():
    print(f'indeed i known the variable {var}')
    
var = 'Yes i\'m the known variable'

eg_function()

""" You can modify the variable environment by using the reserved word 'global varname' lets build another example """

def et_function():
    global var2
    var2 = 5
    print(f'Mark the variable: {var2}')

var2 = 52
et_function()

print(var2) # As you can see in the value printed in this case the end variable for the global variable is going to be reassigned as the one writted in the line 26

""" Variable handling inside the function example """

def my_function(n): # Gets the global value of 1
    print("Yo recibí", n) # shows 1
    n += 1 # Modifies the LOCAL value to 2
    print("Ahora tengo", n) # shows 2


var = 1
my_function(var)
print(var) # Returns the global value of 1

""" Working with a list as an argument and modifying it, lets take a quick look at this """

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
