import math
coverage = 5
height = int(input("enter a height in meters: "))
width = int(input("enter a width in meters: "))

def cans_of_paint(height, width, coverage):
    number_of_cans = math.ceil((height * width) / coverage)
    print(f'youll need {number_of_cans} cans of paint')

cans_of_paint(height, width, coverage)



