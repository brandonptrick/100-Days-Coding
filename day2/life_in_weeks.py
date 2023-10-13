# how many days, weeks, months left until 90 years old

currentAge = input("What is your current age? ")
daysLeft = (32850 - (int(currentAge)*365))
weeksLeft = (4680 - (int(currentAge)*52))
monthsLeft = (1080 - (int(currentAge)*12))

message = f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left. "

print(message)
