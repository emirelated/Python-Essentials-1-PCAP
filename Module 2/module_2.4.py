# Variables and dates
# PEP 8: Should start with a char

# Possible naming for variables
# CamelCase
# UPPERCASE
# lowercase
# mixedCase
# under_scores

# You can't and also shouldn't use reserved words as var names

# LAB 1 - Code

john = 3; mary = 5; adam = 6

print(f'Apple Count\n1) Mary: {mary}\n2) Adam: {adam}\n3) John: {john}')

total_apples = john + mary + adam

print(f'\nTotal Ammount of apples: {total_apples}')


# Abreviation to iterative operators
i = var = rem = j = x = 1 # Just to not see that red line of undefined var

i = i + 2 * j 
# equal to
i += 2 * j

var = var / 2
# equal to
var /= 2

rem = rem % 10
# equal to
rem %= 10

j = j - (i + var + rem)
# equal to
j -= (i + var + rem)


x = x ** 2
# equal to
x **= 2


# Lab 2 - Code
miles = float(input('How many miles you want to convert to Km?: '))
km = miles * 1.61

print(f'Ammount of kilometers: {round(km, 2)}')

km_2 = float(input('If you insist we can also convert your Km to miles, how many?: '))
miles_2 = km_2 / 1.61

print(f"The ammount of miles you will get is: {round(miles_2)}")

# Lab 3 - Code
# Value 3(x**3)-2(x**2)+3(x)-1

x = float(input("What is going to be the value of x sir?: "))
cubic_func = (3 * (x**3)) - (2 * (x ** 2)) + (3 * (x)) - 1

print(f"Valuing x in the function the solution would've: {cubic_func}")
