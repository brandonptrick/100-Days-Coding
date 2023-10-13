height = int(input("Please enter you height in inches: "))
weight = int(input("Please enter your weight in pounds: "))

body_mass = (((weight)/(height**2))*703)

print(round(body_mass, 2))

