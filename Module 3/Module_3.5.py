# This is just bubble sort algorithm
""" For this you have to compare the value of the index of the iteration with the next index and swapp it based in if you want it to be ascendent
 or descendant """

list_bs = [5, 3, 2, 1, 52]
flag = True # This is going to be the indicator of if a swapp occurs

while flag: # While flag True
    flag = False # We change it in case the array is already ordered
    for i in range(len(list_bs) - 1): # Explore all the indexs
        if list_bs[i] > list_bs[i+1]: # If the value in i is higher than the value in i+1 we swapp it
            flag = True # We reactivate the the flag
            list_bs[i], list_bs[i+1] = list_bs[i+1], list_bs[i]

print(list_bs) # This can also be done with the function .sort e.g list_bs.reverse


""" Reversing the values in a descendant order """

flag = True # I reactivate it to show how to reverse the array, otherwise it wouldn't start

while flag: # While flag True
    flag = False # We change it in case the array is already ordered
    for i in range(len(list_bs) - 1): # Explore all the indexs
        if list_bs[i] < list_bs[i+1]: # If the value in i is higher than the value in i+1 we swapp it
            flag = True # We reactivate the the flag
            list_bs[i], list_bs[i+1] = list_bs[i+1], list_bs[i]

print(list_bs) # This can also be done with the function .reverse e.g list_bs.reverse



""" If you're working with a list of variables, the function is gonna take the value not the variable """
a = 3
b = 2
x = 1

list_test = [a, b, x]
list_test.sort()
print(list_test) # As you can see the order is made with the values