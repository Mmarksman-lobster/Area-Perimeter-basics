#ask user for their name
username = input("What is your name? ")

#ask the user for favourite number  (integer)
Fav_num = int(input("what is your favourite number "))

# double halve and square the users favourite number
double = Fav_num * 2
Halve = Fav_num / 2
Square = Fav_num * Fav_num

#greet the user
print()
print(f"hi {username} Your favourite number is {Fav_num}")
#Output the results of halving doubling and squaring there favourite integer
print(f"your Number doubled is {double} ")
print(f" Your number halved is {Halve} ")
print(f" and your number squared is {Square}")
print()
print("have a nice day")