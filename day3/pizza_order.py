print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza would you like? S, M, L? ")
addPepperoni = input("Would you like pepperoni? Y or N? ")
extraCheese = input("Would you like extra cheese? Y or N? ")

bill = 0

if size == "S":
    bill += 15
    if addPepperoni == "Y":
        bill += 2
    if extraCheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if addPepperoni == "Y":
        bill += 3
    if extraCheese == "Y":
        bill += 1
else:
    bill += 25
    if addPepperoni == "Y":
        bill += 3
    if extraCheese == "Y":
        bill += 1

print(f"Your total bill is: ${bill}.")