print ('''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
       
''')
print ("Welcome to the treasure island !")
print ("your mission is to find the treasure ..!")

choice1 = input("you are at a crossrod. Type 'left' or 'right':"). lower()

if choice1 == "left":
    choice2 = input ("you come to a lake. Type 'wait' to 'wait' for a boat or 'swim' to 'swim' accross: "). lower()
    if choice2 =="wait":
        choice3 = input( "you arrive at a house wiht 3 doors. one red, one yellow and one blue. Which color do you choose .?") .lower()
        if choice3 == "yellow":
            print ("you found the treasure room !😁")
            choice4 = input ("You see 3 chests: A, B, and C. Which one do you open .?").upper()

            if choice4 =="A":
                print (" CHEST A IS FULL OF GOLD ! YOU WIN ! 🎉")
            elif choice4 == "B":
                print (" CHEST B IS EMPTY. GAME OVER .")
            elif choice4 == "C":
                print (" CHEST C IS FULL OF SNAKES . GAME OVER .")
            else:
                print ("INVALID CHOICE. GAME OVER.")
            
        elif choice3 =="red":
            print("BURNED BY FIRE. GAME OVER. ")
        elif choice3 == "blue":
            print ("EATEN BY BEASTS. GAME OVER. ")
        else:
            print ("INVALID CHOICE. GAEME OVER. ")
    else:
        print("ATTACKED BY TROUT. GAME OVER. ")

else:
    print("YOU FELL INTO A HOLE. GAME OVER. ")