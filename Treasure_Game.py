print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[]
********************************************************************************
''')

print("Welcome to Treausure Island")
print("Your  mission is to find the treausre")

path = input("You're at a crossroads, Where do you want to go?\n    Left or Right?\n").lower()
if path == "left":
    print("You've made it to the river!")
    river = input("You've come to a large river but the boat hasn't returned, what should you do?\n    "
                  "Wait or Swim?\n").lower()
    if river == "wait":
        print("You made it to the other side!")
    else:
        print("You were attacked by a sea snake! GAME OVER")
    door = input("You've come 3 doors into the castle, which will you enter?\n    Red, Blue, Yellow\n").lower()
    if door == "red":
        print("The room is on fire!  GAME OVER")
    elif door == "blue":
        print("You were devoured by beasts!  GAME OVER")
    else:
        print("You've found the treasure!  YOU WIN!")
else:
    print("You we're attacked by robbers on the road!  GAME OVER")
