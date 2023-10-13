print("Welcome to the love calculator!")
firstName = str.lower(input("Enter your name: "))
secondName = str.lower(input("Enter your true loves name: "))

true_t = firstName.count("t") + secondName.count("t")
true_r = firstName.count("r") + secondName.count("r")
true_u = firstName.count("u") + secondName.count("u")
true_e = firstName.count("e") + secondName.count("e")

trueTotal = true_t + true_r + true_u + true_e

love_l = firstName.count("l") + secondName.count("l")
love_o = firstName.count("o") + secondName.count("o")
love_v = firstName.count("v") + secondName.count("v")
love_e = firstName.count("e") + secondName.count("e")

loveTotal = love_l + love_o + love_v + love_e

trueLove = str(trueTotal) + str(loveTotal)

trueLove = int(trueLove)

if trueLove < 10 or trueLove > 90:
    print(f"Your score is  {trueLove}, you go together like coke and mentos.")
elif trueLove >= 40 and trueLove <= 50:
    print(f"Your score is  {trueLove}, you are alright together.")
else:
    print(f"Your score is  {trueLove}.")
