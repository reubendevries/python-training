menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam","egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        meal.count("spam")
        if meal.count("spam") == 1:
            meal.remove("spam")
            print(meal)
        elif meal.count("spam") == 2:
            meal.remove("spam")
            meal.remove("spam")
            print(meal)
        elif meal.count("spam") == 3:
            meal.remove("spam")
            meal.remove("spam")
            meal.remove("spam")
            print(meal)
        else:
            meal.remove("spam")
            meal.remove("spam")
            meal.remove("spam")
            meal.remove("spam")
            print(meal)
print(meal)

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()