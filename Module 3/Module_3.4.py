# arrays

""" Fast refresh of indexs and declaration """

list1 = [1, 2, 3, 4, 5] # indexs go from [0: 4]
print(list1[0])

# You can get the size of the array using the function len()

size = len(list1)
print(f'The size of the list in terms of quantity of elements {size}')

# Items of a list can be removed using the del instrunction

del list1[0] # This removes the item in the position [0] of the array

""" now the quantity is 4 and the number of elements is 4 too """

# Negative indices are used to go from the inverse ranges so if you do list[-1] you're gonna encounter the last item


""" Lab 1 - Code """

hat_list = [1, 2, 3, 4, 5]
len_aux = int((len(hat_list) - 1) / 2)

hat_list[len_aux] = int(input('Input the item you\'re gonna replace in the middle of the array: '))

del hat_list[-1]

print(f'Final ammount of items in the hat list {len(hat_list)}, and the list goes {hat_list}\n')


# You can add an item to the end of the list using .append(item) or in a selected index using .insert(index, item)
# a list can be started empty

# You can explore an array in a very efficient way making use of a for bucle

for i in range(len(hat_list)):
    print(f'One by one: {hat_list[i]}')

for i in hat_list: # In this version you can make the i take the subsecuent value of the array
    print(f'One by one v2: {i}')


# Changing values in a list make this an example, we are going to do it w/out using an aux var

list_eg = [2, 1, 3, 4]

list_eg[0], list_eg[3] = list_eg[3], list_eg[0] # This will result in list_eg = [4, 1, 3, 2]

""" Lab 2 - Code """

beattles = []

beattles.append('John Lennon')
beattles.append('Paul McCartney')
beattles.append('George Harrison')

for i in range(2):
    beatle_name = str(input('What Beattle is missing?: '))
    beattles.append(beatle_name)

del beattles[-1]
del beattles[-1]
beattles.insert(0, 'Ringo Starr')

print(beattles)