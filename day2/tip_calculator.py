print("Welcome to the Tip Calculator!")

billTotal = float(input("What was the total bill? $"))
tipAmount = int(input("How much would you like to tip? 10%, 12%, or 15%? "))
split = int(input("How many people to split the bill by? "))


tipDecimal = tipAmount / 100 + 1
splitTotal = (billTotal * tipDecimal) / split

# used to help display 2 decimal places in the output
finalBill = "{:.2f}".format(splitTotal) 

message = f"Each person should pay ${finalBill}"

print(message)






