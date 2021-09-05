choice = input("Would you like to play a game of adventure (y/n): ")
if choice == "y":
    choice = input("You are walking down a path in the middle of a forest and have arrived at a crossroad. Would you like to go right or left (r/l): ")
    if choice == "l":
        choice = input("You arrived at a river. There are no boats around and the only way across is a damaged bridge. Maybe it's safe... or maybe it isn't. Would you like to cross the bridge or continue along the river? (b/r): ")
        if choice == "b":
            print("You lost, the bridge was not stable and you drowned in the river.")
        else:
            choice = input("You arrived at a cave. Wanna go in? (y/n): ")
            if choice == "y":
                print("You found a lost treasure in the cave. You won!")
            else:
                print("You died of hunger outside the cave.")
    else:
        choice = input("You arrived at a mountain. Would you like to go to its summit (y/n): ")
        if choice == "y":
            print("Congratulations champion! You found a treasure chest full of gold and diamonds.")
        else:
            choice = input("You walked around the bottom of the mountain. You found a large hole in the ground. Maybe there's something interesting down there. Would you like to go in (y/n): ")
            if choice == "y":
                print("The hole was once a deep well - you died falling down.")
            else:
                choice = input("You continued wandering aimlessly around the base of the mountain and died of starvation.")
else:
    print("Bye!")
