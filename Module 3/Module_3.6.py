""" Operations with list """
list_1 = [1]
list_2 = list_1
list_1[0] = 2

print(list_2) # This is going to print 2, because it is pointing the direction of the list, not the original integer, to avoid this you need to use [:]

""" Slicing a list helps you to 'clone' the list rather than pointing to the same direction """
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2

print(list_2) # This is going to print 1, because before you re-evaluated your list 1 you 'cloned' it in the list 2

# You can also slice in an interval, per e.g

list_3 = [1, 2, 3, 4, 5, 6]
list_2 = list_3[1:3] # This is going to store the first two values of the interval, so the values in the list 2 are [1, 2] or 3 -1 elements

# The slices can also be used with negative indexs per e.g

list_4 = [3, 4, 5, 6, 7, 8, 9]
list_2 = list_4[1:-1] # So in this case the list is going to be almost the entire list, because the -1 index is the last one, so is something like [1:7]

print(list_2)

""" Take this as a [start:end] being start the elements and the end the last you're trying to store """
list_2 = list_4[3:] # This is going to store the elements starting from the one after the 3rd one
print(list_2)

list_2 = list_4[:3]
print(list_2) # This is going to store the first three elements


""" The del instruction can be used to remove items from the list with slices """
del list_4[:3]

print(list_4)

""" Operators that can check a list
in if you use [value] in [array] you can check if the item is included in the list
not in the opposite of being included haha """

print(5 in list_4) # Not included so it will print a False
print(5 not in list_4) # Not included so it will print a True

""" You can also check the values in one array on other array, per e.g take this lottery example """

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets: # This explores all the numbers in the ticket
    if number in drawn: # This compares the numbers of the ticket with the ones that actually won
        hits += 1 # This accumulateds every hit

""" Lab 1 - Code """
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list.sort() # I order the array  it can be done with a bubble sort too

""" Bubble sort solution for this array to not use sort:
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
bb_flag = True

while bb_flag:
    bb_flag = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            bb_flag = True
            break

 """
del_flag = True # Condition to run the iteration
j = 1 # I start from i + 1 to not outrun the index range of my_list[i]

while del_flag:
    del_flag = False # I deactivate the condition to be able to quit

    for i in range(len(my_list) - 1): # The range of the list is the quantity of the elements so the - 1 is so it matches the index    

        if my_list[i] == my_list[j]: # Comparison of i and i + 1
            del my_list[i] # If it matches the element is removed
            del_flag = True # The flag is activated to run the iteration again
            j = 1 # The control point is set to the starting value
            break # Breaking the for iteration so it can run the entire list again

        if (j < (len(my_list) - 1)): # If the control variable is less than the max index value it adds 1 so it can compare i and j = i + 1
                j += 1


print(my_list)
        