# Comparison
5 == 5
5 == 5.0

# Diff of
5 != 4
5 != 5

# Value
5 < 4
5 > 4
5 <= 4
5 >= 5

""" Prioridad de operadores
1. +, - (Unario)
2. **
3. *, /, //, %
4. +, - (Binario)
5. <, <=, >, >=
6. ==, != """


""" LAB 1 - Code """
n = int(input('Writte the value of n as an int:'))
print(f"{n >= 100}")


# Conditions and nested conditions

""" if [something]:
        [Something happens]
    else:
        if [something]:
            [something happens] 
            
This can also be writted as elif.

if [something]:
    [something happens]
elif [Something else happened]:
    [other thing happens]
else:
    [Something]
    
! The conditions always have to end with an else"""

# max(value1, value2, value3) gives us the max value of a n interval, and min does the oposite
print(max(1, 5, 6, 7, 2, 5, 3, 156))

""" Lab 2 - Code """
plant = str(input('What plant is it?: '))

if plant == 'Espatifilo':
    print('YES, the Espatifilo is the best plant of all time!')
elif plant == 'ESPATIFILO':
    print('Sorry, even if it is the best i don\'t want a big Espatifilo')
elif plant == 'espatifilo':
    print(f'Did you mean Espatifilo?, because you wrotte it {plant}')
else:
    print(f'Yuck, what kind of ugly plant is a {plant}')


""" Lab 3 - Code """

income = float(input('What is your income?: '))

if income < 85528:
    tax = (income * 0.18) - 556.2
elif income > 85528:
    excess = income - 85528
    tax = (14839.2 + (excess * 0.32))

print(f'Final tax: {round(tax, 2)}')

""" Lab 4 - Code """

yy = int(input('What year are we valuating?: '))

if ((yy % 4) != 0) and ((yy % 400) != 0):
    print('Normal year')
elif (yy % 100) != 0:
    print('Leap year')
else:
    print('Leap year')

if yy >= 1582:
    print('Included in the Gregorian Era.')
else:
    print('Not included in te Gregorian Era.')

""" Quick note in this excercise, it says that the years that aren't divided
 by 4 or 400 are common years, and the ones that aren divided by 100 are leap years...
 There is a tricky number of numbers like 400, 800, 1200, 1600... and so on. """
