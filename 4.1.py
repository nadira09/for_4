# задача 1

from sys import argv

def salary(hours, rate, bonus):
    print(hours * rate + bonus)

try:
    arg_0, arg_1, arg_2, arg_3 = argv
except ValueError:
    arg_1 = input('Enter the work in the hours: ')
    arg_2 = input('Enter the work rate: ')
    arg_3 = input('Enter bonuses: ')

salary(int(arg_1), int(arg_2), int(arg_3))

