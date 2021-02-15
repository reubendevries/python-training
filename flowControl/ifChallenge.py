name = input("Please type in your name: ")
age = int(input("Please type in your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
     print("Sorry {} this holdiay is for people between ages of 18 and 30".format(name))