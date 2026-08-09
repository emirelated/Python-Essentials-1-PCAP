# Lab 1 - Code
""" Evaluar los resultados de cuatro operaciones aritméticas básicas.

Los resultados deben imprimirse en la consola. """

x = 5.0
c = 6.0

print(f"Addition of x and c: {x + c}")
print(f"Difference of x and c: {x - c}")
print(f"Division of x and c: {round(x / c, 2)}")
print(f"Product of x and c {x * c}")

print("That's all friends!")


# Lab 2 - Code
""" iterations of divisions in test numbers """

x = float(input('What is the value of x?: '))
operation = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print(operation)

# Lab 3 - Code
"""  La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
 expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola. 
 
 Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16."""

hour = float(input("What is the hour of start?: "))
minute = float(input("What is the minute of start?: "))
duration = float(input("How long is going to be the show, in minutes?: "))

hour_aux = 0

while duration > 59:
    hour_aux += 1
    duration -= 60

minute += duration

while minute > 59:
    hour_aux += 1
    minute - 60

hour += hour_aux
if hour > 23:
    hour -= 24

print(f'The show will finish at: {int(hour)}:{int(minute)}')

