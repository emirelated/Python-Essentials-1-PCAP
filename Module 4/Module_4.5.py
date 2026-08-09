""" When you have long pieces of code you can separate them by using the inverted bar in front of the code piece, so it can identify that it needs to follow up the next line, per example for a
function that gives you the ibm  """

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200: # Here you can identify that you have an \ that will say to the function that it needs to read the next line

        return None

    return weight / height ** 2 

print(bmi(352.5, 1.65))

def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))

