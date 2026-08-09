""" Parametrized functions.
These are the functions that receive arguments, but those arguments can only be used inside the function """

# e.g of parametrized function
def par_funct(number):
    print('That is actually a pretty nice number', number)

par_funct(5)

""" the arguments of the function can coexist with a variable of the same name, and because the way of they exist as directions in the language they both can be used so: """

def epam(glasses): # The argument is the one passed in the line 17, not the one of the variable defined at line 15
    print(f'amazing glasses, with a x{glasses} of augment')

glasses = '30 Left, 40 Right' 

epam(input('What kind of glass')) 

""" Multi argument function """

def cool(artist, genre):
    print(f'So your favorite artist is {artist}, and his genre of music is {genre}, that is actually amazing')

artist = input('Tell me what is your favorite artist: ')
genre = input('What genre does your artist sing mostly?: ')
cool(artist, genre)

""" The previous parametrized functions that we looked are positionals, meaning that the argument sended in the function call matches the argument received by the function, but there is a way
to do it with a keyword, and is assigning them in the call of the function """

cool(genre='R&B', artist='Brook') # This will call the function, but it will assign the value of the arguments requested


""" Both ways of use for the functions can be mixed, per example """

cool('Goku', genre='Anime')

""" There can be exceptions, per e.g you can't give an argument the same value

cool('Michale Jackson', artist='Brook') # In this case you're sending the function argument 'artist' two values and it is going to print an error  """

# The arguments can also have aux values or initialized values like this function

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Enrique") # This overrides the value of the first argument
introduction(first_name="Guillermo") # This overrides the value of the first argument
introduction() # This will just use the initialized argument

