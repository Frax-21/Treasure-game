print('''**********************************************************************     
    |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
***************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("The road ahead is dangerous so pirate beware! T_T")
choice1 = input('You\'re at a crossroad, where do you want to go ? left or right?\n').lower()
if choice1 == "left":
    print("Well done pirate!")
    choice2= input("You've come to a lake. There is an island in the middle of the lake. "
          "Type \"wait\" to wait for a boat or, type \"swim\" to swim to the island\n").lower()
    if choice2 == "wait":
        #game will continue
        print("Patience is highly rewarded")
        choice3 = input("You arrived at the island unharmed."
                        " There is a house with 3 doors. One red, one blue and one yellow\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. You are Dead!")
        elif choice3 == "yellow":
            print("The ghosts of the island have taken you. You are Dead!")
        elif choice3 == "blue":
            print("Congratulations! take your treasure pirate.")
        else:
            print("Invalid choice! the dead pirates took your soul. You are Dead!")
    else:
        print("You got attacked by a serpent. You are Dead!")
else:
    print("You fell in to a hole. You are Dead!")
