name = input("What is your name? ")
name = name + "."
print("Nice to meet you, ", name, "My name is Chatbot.")
location = input("And where are you from? ")
print(location, "sounds like a nice place.")
number_input = input("What is your favorite number? ")
number = float(number_input)
times = number / 7
number = round(number)
print("Your favorite number", number, "is", times, "times as big as my favorite number (7).")
car = input("What is your dream car? ")
print("I have always wanted a", car, "as well.")
p_input = input("How much does the car cost? ")
p = float(p_input)
print("This sounds very expensive.")
years_input = input("How many years would you take a loan out to pay for the car? ")
y = int(years_input)
rate_input = input("What is the annual interest rate (percent) you expect to get for this car? ")
annual = float(rate_input)
r = (annual / 100) / 12
n = y * 12
mpmyt = (r * p) / (1 - (1 + r) ** -n)
print("If you bought the", car, "you would have a monthly payment of", mpmyt, "which is a total of", (mpmyt * n))
print("I hope you can buy the car someday. Goodbye, ", name)