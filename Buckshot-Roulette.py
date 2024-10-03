#Rules:

#The round starts with being shown 3-5 shells which will be randomly Live or Blank (atleast 1 blanks and atleast 1 live)
#The rounds are put into a list in a random order
#You start first
#You can choose to either shoot yourself or the dealer
#Shooting yourself will use a round and remove it from the list  (blank will do nothing and Live will make you lose one life)
#Regardless of if you lose a life or not it will be your round again
#Shooting the dealer with either a live round will make them lose a life, a blank will do nothing.
#Regardless of outcome it will turn to the dealers round once you shoot them
#The dealer has the same options
#Both players get 3 lives, first to lose all of them looses
#Dealer works by keeping track of what shells have been used, giving him a % chance to either shoot himself or the other player depending on what he knows

#Expansion Things:

# multiple rounds where lives get reset, increasing difficulty?
# Items that can help you (saw: doubles damage, spyglass: shows the current bullet in the chamber)
# Allow dealer to use items as well
# Double or nothing at the end of game, can get a highscore if you win
# Cool visuals :)

from random import randint
from time import sleep

print("Let the games commence!")

playerLife = 3
dealerLife = 3








currentMatch = False

#Randomizes the positions of all values within a list
def ShuffleList(List):
     shuffledList = []
     for i in range(len(List)):
         index = randint(0,len(List)-1)

         listValue = List[index]
         List.pop(index)

         shuffledList.append(listValue)
     return shuffledList
     
def RenderRoom(gunholder,aim,message):
     playerTurn = " "
     dealerTurn = " "

     playerAim = "     "
     dealerAim = "     "

     playerHandle = "   _"
     dealerHandle = " "

     if gunHolder == "player":
          playerTurn = "V"
          if aim == "Other":
               playerAim =   "  ___"
               playerHandle = "/. _"
     else:
          dealerTurn = "V"
          if aim == "Other":
               dealerAim =   "___  "
               playerHandle = "_  .\\"
          elif aim == "Self":
               dealerAim = " ___"


     print(f"-----------------------------------")
     print(f"\t{message}")
     print(f"-----V----------------------V------")
     print(f"     O ___              ___ O      ")
     print(f"    /I\  .\____________/.  /I\     ")
     print(f"     M     I         I      M      ")
     print(f"    d b    I         I     d b     ")
     print(f"-----------------------------------")

#shuffledRounds = []

liveRoundQouta = 1
blankRoundQouta = 2


gunHolder = "player"

actionChosen = 0
actionList = ["Shoot Dealer","Shoot Yourself","PlaceHolderAction"]

dealerMemory = []



while dealerLife > 0 and playerLife > 0:
    roundsList = []

    
    #Set up for the rounds being inserted
    roundCount = randint(3,5)

    #Adds all rounds into a list and makes sure that the qoutas are met
    for i in range(roundCount):
         roundType = randint(1,2)
         actualRound = NotImplemented

         if roundType < 2:
              actualRound = "o"
         else:
              actualRound = "x"

         spaceLeft = len(roundsList) - roundCount

         liveCount = roundsList.count("x")
         blankCount = roundsList.count("o")


         if liveCount < liveRoundQouta and spaceLeft <= liveRoundQouta:
                actualRound = "x"
         elif blankCount < blankRoundQouta and spaceLeft <= blankRoundQouta:
                actualRound = "o"

         

         roundsList.extend(actualRound)

    liveCount = roundsList.count("x")
    blankCount = roundsList.count("o")

    print(f"{liveCount} Live rounds, {blankCount} Blanks")

    sleep(1)
    print("They are inserted in a random order")


    print(f"Unshuffled List: {roundsList}")
    sleep(2)

    roundsList = ShuffleList(roundsList)

    dealerMemory = roundsList
    
    print(f"Shuffled List: {roundsList}")

    currentMatch = True


    while currentMatch:
         if gunHolder == "player":
              print("Your turn")
              

              ShowCaseList = []

              for action in actionList:
                   if actionList.index(action) == actionChosen:
                         ShowCaseList.append(f"[{action}]")
                   else:
                         ShowCaseList.append(action)

              print(*ShowCaseList,sep="   ")

              playerAction = input("")
              playerAction = playerAction.upper()

              if playerAction == "A":
                   actionChosen -= 1
                   if actionChosen < 0:
                        actionChosen = len(actionList)-1
              elif playerAction == "D":
                   actionChosen += 1
                   if actionChosen > len(actionList)-1:
                        actionChosen = 0
              elif playerAction == "":
                   finalChoice = actionList[actionChosen]

                   target = NotImplemented

                   if finalChoice == "Shoot Yourself":
                        target = "player"
                   elif finalChoice == "Shoot Dealer":
                        target = "dealer"
                   
                   if target != NotImplemented:
                         activatedRound = roundsList[0]
                         roundsList.pop(0)
                         #dealerMemory.pop(0)
                         if target == "player":
                             print("\nYou hold the gun to your chin...")
                             sleep(3)
                            

                             if activatedRound == "x":
                                   print("BANG!!")
                                   playerLife -= 1
                                   sleep(1)
                                   print("You lose a life")
                                   currentMatch = False
                             else:
                                   print("*click*")
                                   sleep(1)
                                   print("It was a blank...")

                         elif target == "dealer":
                             
                             print("\nYou aim the gun at the dealer...")
                             sleep(3)

                             if activatedRound == "x":
                                   print("BANG!!")
                                   dealerLife -= 1
                                   sleep(1)
                                   print("The Dealer loses a life")
                                   currentMatch = False
                             else:
                                   print("*click*")
                                   sleep(1)
                                   print("It was a blank...")
                             gunHolder = "dealer"
         elif gunHolder == "dealer":
              """
              liveRange = [1,dealerMemory.count("x")]
              blankRange = [dealerMemory.count("x")+1,len(dealerMemory)]

              memorySize = len(dealerMemory)
              """
              liveRange = [1,roundsList.count("x")]
              blankRange = [roundsList.count("x")+1,len(roundsList)]

              memorySize = len(roundsList)

              if memorySize > 1:
                    dealerChoice = randint(1,memorySize)
              else:
                    dealerChoice = 1
                   

             
              target = NotImplemented


              if dealerChoice >= liveRange[0] and dealerChoice <= liveRange[1]:
                   target = "player"
              elif dealerChoice >= blankRange[0] and dealerChoice <= blankRange[1]:
                   target = "dealer"
               
              activatedRound = roundsList[0]
              roundsList.pop(0)
              #dealerMemory.pop(0)


              if target == "player":
                    print("\nThe dealer aims the gun at you...")
                    sleep(3)
                            

                    if activatedRound == "x":
                         print("BANG!!")
                         playerLife -= 1
                         sleep(1)
                         print("You lose a life")
                         currentMatch = False
                    else:
                         print("*click*")
                         sleep(1)
                         print("It was a blank...")
                    gunHolder = "player"

              elif target == "dealer":
                             
                    print("\nThe dealer aims the gun at themselves...")
                    sleep(3)

                    if activatedRound == "x":
                         print("BANG!!")
                         dealerLife -= 1
                         sleep(1)
                         print("The Dealer loses a life")
                         currentMatch = False
                    else:
                         print("*click*")
                         sleep(1)
                         print("It was a blank...")
 
                   
print("Game Over")
              
              
                             
                             
                              
                             
                        
                        



   















#Testing stuff with lists
"""
List = [["Steve",20,False],["Lisa",23,True]]
ListLength = len(List)

print(ListLength)

for i in range(ListLength):
    print(i)


for person in List:
    name = person[0]
    age = person[1]

    print(f"This person is named {name} and is {age} years old!")






List = ["x","o","x"]
List2 = ["o","o","o"]
List.extend(List2)

LiveNumber = List.count("x")
BlankNumber = List.count("o")

print(LiveNumber,BlankNumber)
print(List)

print(List.index("x"))
List.pop(List.index("x"))

LiveNumber = List.count("x")
BlankNumber = List.count("o")

print(LiveNumber,BlankNumber)
print(List)"""