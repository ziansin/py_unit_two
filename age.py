current_year = 2022

name = input("What is your name?:")
age_input = input("How old are you?:")
age = int(age_input)
time = 100 - age
date = time + current_year

print(name, "will turn 100 in", date)