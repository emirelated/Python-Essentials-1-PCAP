# This is a section abt while iterations, you can break an infinite by just
# adjusting the value of the condition or just using a break

""" Lab 1 - Code """

secret_number = 777

pick = int(input('Pick your number to see if you got the magic jack: '))

while pick != secret_number:
    pick = int(input('God has not helped you, pick again: '))

# Use of the for instruction with range()

for i in range(100): # This will repeat the instructions like it was n = (i += 1)100 times, starting from 0
    pass # this skips the instruction


import time

for i in range (5):
    print(f'{i + 1} Missisipi')
    time.sleep(1)
    
print('Ready or not here i go')


# Continue, continue simulates that the condition has been achieved

""" Lab 2 - Code """

secret_word = str(input('What is the secret word?: '))

while secret_word != 'chupacabra':
    secret_word = str(input('Wrong word, try again: '))

    if secret_word == 'chupacabra':
        break

print('You did manage to solve the secret word, congrats :)')

""" Lab 3 - Code """

wordToDevour = str(input('Writte your word: '))

for i in wordToDevour:
    i = i.upper()
    if (i != 'E') and (i != 'A') and (i != 'I') and (i != 'O') and (i != 'U'):
        print(i)

""" Lab 4 - Code """

wordToDevour = str(input('Writte your word: '))
aux = ''
for i in wordToDevour:
    i = i.upper()
    if (i != 'E') and (i != 'A') and (i != 'I') and (i != 'O') and (i != 'U'):
        aux += i

print(aux)

""" Lab 5 - Code """

blocks = int(input('How many blocks does the wall have: '))
height = 0
block_per_pile = 0
for (i) in range(blocks):
    if (i+1) > block_per_pile:
        height += 1
        block_per_pile += (i + 1)
        print(f'atm {i + 1}, block per pile {block_per_pile}')

print(f'The total height of the structure is {height}')

""" Every height level needs to have at least 1 block more, so, if the first one needs 1 block, the second one needs 2, and the third 3, etc.

How does this works, well, i starts in 0, so when it is valued with the block_per_pile it does get the height to 1, and the block_per pile accumulates that value
so in the next iteration it should've higher than i+1, being that 2, this may seem insignifcant, but in the next iteration it is going to be 3, and so on

iterations
one bpp = 1
two bpp = 1 + (2 blocks)
third bpp = 3 + (4 blocks)
and so on, being 

bpp = bpp + (i+1) """


""" Lab 6 - Code """

steps = 0

c0 = int(input('Pick your number to apply collatz conjecture: '))
while (c0 > 0):  

   if (c0 % 2) == 0:
      c0 /= 2
      steps += 1
      print(c0)
   elif (c0 % 2) != 0:
      c0 = 3 * c0 + 1
      steps += 1
      print(c0)

   if c0 != 1:
      pass
   else:
      break
      
print(f'Number of steps {steps}')

""" Lab X - Quiz """

aux = ''
for digit in "0165031806510":
    if digit == "0":
        digit = 'x'
        aux += digit
    else:
        aux += digit

print(aux)
