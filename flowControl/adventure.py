available_exits = ["North", "South", "East", "West"]

chosen_exit = None
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
else:
    print("aren't you glad you go out of there")