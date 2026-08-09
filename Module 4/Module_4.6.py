""" Tuples and dictionaries.
There is two types of dates in python, mutables and inmutables.
While mutables can be modified during the execution of the program the inmutables can't and are statics.


An e.g of an inmutable date is a tuple, that are defined by expression = (value1, value2, ... valuen) or expression = value1, value2, ..., valuen
a tuple can store diverse type of dates and also can be created empty, and also can be created with only one element, but it does need a coma to be differenced of a variable, so it
should be defined in the next form expression = (value, ) or expression = value,

To explore the elements of a tuple you can do it with the index exactly like an array. Let's writte an example.
"""

tuple_eg = (3, 2, 100, 99)
for elem in tuple_eg:
    print(elem)

print(tuple_eg[0])
print(tuple_eg[2])
print(tuple_eg[1:])
print(tuple_eg[:1])
print(tuple_eg[-1])

""" Tuples does accept certain operators """

print(tuple_eg + ('Fausto', ' Maxi'))
print(tuple_eg)
print(tuple_eg * 2)
print(tuple_eg)
print(len(tuple_eg))
print(3 in tuple_eg)
print(3 not in tuple_eg)

""" Dictionaries are a kind of date mutable, that are stored like {key: value, key1: value1} """

fishtank = {'Fausto': 'Station3',
             'Jere': 'Station1',
             'Nico': 'Station2',
             'Emir': 'Station4',
             'Maxi': 'Station5',
             'Vero': 'Station6'}
empty_fish = {}
miligrams_of_water = {'Station1': 100, 'station2': 250}

print(f'\n{fishtank}\n{empty_fish}\n{miligrams_of_water}\nLen of the fishtank: {len(fishtank)}')

# You can search for a value in a dictionarie by using the key as the index

print(fishtank['Fausto'])

# You can explore the dictionarie using a little iteration like the one showed below

testers = ('Fausto', 'Jere', 'Emir', 'Dami')

for tester_name in testers:
    if tester_name in fishtank:
        print(f'{tester_name}, belongs to the fishtank in the workspace {fishtank[tester_name]}')
    else:
        print(f'{tester_name} is not currently in the fishtank.\n')

# But there does exist a better way to explore them

for key in fishtank.keys():
    print(f'{key} is in the workspace {fishtank[key]}')

# Another alternative can be
print('\n')

for tester, workstation in fishtank.items():
    print(f'{tester} have the assigned the workstation {workstation}')

# The values inside a dictionarie can be modified too as the e.g below
fishtank['Fausto'] = 'Station10'

print(fishtank['Fausto'])

# Values can also be added normally
fishtank['FacundoDLF'] = 'Station9'

print(fishtank['FacundoDLF'])

# The values can also be inserted with the .update
fishtank.update ({'Dami': 'Ex-fish'})
print(fishtank['Dami'])

# The values can be deleted using the instruction del

del fishtank['Dami'] # If i try to print this value now is going to generate an error because it doesn't exist anymore inside the dictionarie
fishtank.popitem() # Will automatically pick the last item of the dictionarie, note tha this doesn't require the instruction del


# Example of a complex instruction with dictionaries and tuples
school_class = {}

while True: # The starting point of the iteration, but it doesn't gives the user any message to stop
    name = input("Type the student name: ")
    if name == '':
        break
    
    score = int(input("Type the qualification obtained in the exam (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,) # This does adds the value to the dictionary, that will help to count the ammount of notes that are in the dict and helps to do the prom
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1 # The counter of notes
    print(name, ":", adding / counter) # The prom of all the notes of the student

print(school_class)

""" There is a conversor that can help you to convert a serie of elements to a tuple, he instruction is tuple(expresion/arguments) """
list_e_g = [1, 2, 3]
tup = tuple(list_e_g)
print(tup)

# You can also delete the entire dictionare or all the items in a dictionarie
del fishtank # Will delete the entire dictionary
fishtank = {'Fausto': 'Station3',
             'Jere': 'Station1',
             'Nico': 'Station2',
             'Emir': 'Station4',
             'Maxi': 'Station5',
             'Vero': 'Station6'}
fishtank.clear() # Will remove all the elements inside the dictionary

# You can copy an entire dictionary using the instrucition .copy

fishcopy = fishtank.copy()

# Unpacking a tuple as variables
tupvar = 1, 5, 6
a, b, c = tupvar # Now that values can be used as variables

# Counting the duplicated values of a tuple
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
print(tup.count(2))