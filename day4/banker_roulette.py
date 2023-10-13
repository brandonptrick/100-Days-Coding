import random

names_string = input("Give me everyones name seperated by a comma: ")
names = names_string.split(", ")

x = len(names)

random_choice = random.randint(0, x - 1)

person_that_will_pay = names[random_choice]

print(f"{person_that_will_pay} will pay for the meal today!")
