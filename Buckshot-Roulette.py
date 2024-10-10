#Rules:

#The round starts with being shown 3-5 shells which will be randomly Live or Blank (atleast 2 blanks and atleast 1 live)
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



playerLife = 3
dealerLife = 3






instruction = ""

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
     
def RenderRoom(gh,aim,message):

     playerTurn = "---"
     dealerTurn = "---"


     playerAim = "     "
     dealerAim = "     "

     playerHandle = "   _"
     dealerHandle = "_    "

     if gh == "player":
          playerTurn = " V "
          if aim == "Other":
               playerAim =   "  ___"
               playerHandle = "/. _"
          if aim == "Self":
               playerAim =    "___  "
               playerHandle = "  .\\"
     else:
          dealerTurn = " V "
          if aim == "Other":
               dealerAim =    "___  "
               dealerHandle = "_  .\\"
          elif aim == "Self":
               dealerAim =   "  ___"
               dealerHandle = "/.   "
     print("\n")
     print(f"You: {playerLife}    Dealer: {dealerLife}")
     print(f"-----------------------------------")
     print(f"\n{message}")
     print(f"\n----{playerTurn}--------------------{dealerTurn}-----")
     print(f"")
     print(f"     O {playerAim}          {dealerAim} O      ")
     print(f"    /I\\{playerHandle}___________{dealerHandle}/I\\     ")
     print(f"     M     I         I      M      ")
     print(f"    d b    I         I     d b     ")
     print(f"-----------------------------------")
     print(f"{instruction}")
     print(f"")

def RenderShells(roundsL,roundsB,Message):

     shellTop =          " ___ "
     ShellSegmentTop =   "!___!"
     shellSegmentLive =  "! X !"
     shellSegmentBlank = "!   !"
     shellBottom =       "!___!"

     visualShellsListTOP = []
     visualShellsListTOP2 = []
     visualShellsList = []
     visualShellsListBOT = []

     totalRounds = roundsL + roundsB

     for i in range(totalRounds):
          visualShellsListTOP.append(shellTop)
          visualShellsListTOP2.append(ShellSegmentTop)
          visualShellsListBOT.append(shellBottom)

          if i <= roundsL-1:
               visualShellsList.append(shellSegmentLive)
          else:
               visualShellsList.append(shellSegmentBlank)
               



     print("\n")
     print(f"You: {playerLife}    Dealer: {dealerLife}")
     print(f"-----------------------------------")
     print(f"\n{Message}")
     print(f"\n-----------------------------------")
     print(*visualShellsListTOP,sep="  ")
     print(*visualShellsListTOP2,sep="  ")
     print(*visualShellsList,sep="  ")
     print(*visualShellsList,sep="  ")
     print(*visualShellsListBOT,sep="  ")
     print(f"-----------------------------------")
     print(f"{instruction}")
     print(f"")

     
#shuffledRounds = []

liveRoundQouta = 1
blankRoundQouta = 2


gunHolder = "player"

#RenderRoom(gunHolder,NotImplemented,"")

actionChosen = 0
actionList = ["Shoot Dealer","Shoot Yourself","PlaceHolderAction"]

dealerMemory = []

RenderRoom(NotImplemented,NotImplemented,"Lets play a little game...")
sleep(3)


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




    statement = f"{liveCount} Live rounds, {blankCount} Blanks"

    instruction = "*remember these*"

    #Shows all of the shells with the render shell function with the instruction "*remember these*"

    RenderShells(liveCount,blankCount,statement)
    sleep(5)

    instruction = ""

    RenderRoom("Dealer","Other","They are inserted in a random order.")
    sleep(3)


    

    #shuffles the list to add to the randomization
    roundsList = ShuffleList(roundsList)



    currentMatch = True
    first = False
    first2 = False


    while currentMatch:
         if gunHolder == "player":
              
              if first == False:
                   first = True
                   RenderRoom(gunHolder,NotImplemented,"Your Turn")
                   sleep(2)


              #Create a showcase list of the actions and puts squarebrackets around the choosen action to later print it
              #does this by checking which index the actionChosen variable is assigned to and 
              # appends the showCaseList with it if they share index
              ShowCaseList = []


              for action in actionList:
                   if actionList.index(action) == actionChosen:
                         ShowCaseList.append(f"[{action}]")
                   else:
                         ShowCaseList.append(action)

              print(ShowCaseList)
              print(*ShowCaseList ,sep="   ")

              #Creates a nicer looking string that can be printed in the renderroom function

              statement = "  ".join(ShowCaseList)

              instruction = "use [A] and [D] to switch options, hit [ENTER] to choose"

              RenderRoom(gunHolder,NotImplemented,statement)

              instruction = ""


              playerAction = input("")
              playerAction = playerAction.upper()

              #Allows the player to lower or higher the value of the actionChosen variable to switch options, 
              # goes around in circles if value is outside of the length of the list

              if playerAction == "A":
                   actionChosen -= 1
                   if actionChosen < 0:
                        actionChosen = len(actionList)-1
              elif playerAction == "D":
                   actionChosen += 1
                   if actionChosen > len(actionList)-1:
                        actionChosen = 0
              elif playerAction == "":
                   
                   #Assigns the finalChoice variable to the value in the actionList which has the same index as actionChosen
                   finalChoice = actionList[actionChosen]

                   target = NotImplemented

                   if finalChoice == "Shoot Yourself":
                        target = "player"
                   elif finalChoice == "Shoot Dealer":
                        target = "dealer"
                   
                   #Checks if there is a target for consistency reasons and for if you pick the PlaceHolderAction
                   if target != NotImplemented:
                         activatedRound = roundsList[0]
                         roundsList.pop(0)

                         #Checks who is the target when it's your turn and does the appropriet logic,
                         #resets the current match if a player has lost a life

                         if target == "player":
                             RenderRoom(gunHolder,"Self","You hold the gun to your chin...")
                             sleep(3)
                            

                             if activatedRound == "x":
                                   print("BANG!!")
                                   playerLife -= 1
                                   sleep(1)
                                   print("You lose a life")
                                   sleep(1.5)
                                   currentMatch = False
                             else:
                                   print("*click*")
                                   sleep(1)
                                   print("It was a blank...")
                                   sleep(1.5)

                         elif target == "dealer":
                             RenderRoom(gunHolder,"Other","You aim the gun at the dealer...")
                             #print("\nYou aim the gun at the dealer...")
                             sleep(3)

                             if activatedRound == "x":
                                   print("BANG!!")
                                   dealerLife -= 1
                                   sleep(1)
                                   print("The Dealer loses a life")
                                   sleep(1.5)
                                   currentMatch = False
                             else:
                                   print("*click*")
                                   sleep(1)
                                   print("It was a blank...")
                                   sleep(1.5)
                             gunHolder = "dealer"
         elif gunHolder == "dealer":

              if first2 == False:
                   first2 = True
                   RenderRoom(gunHolder,NotImplemented,"My Turn")
                   sleep(2)

              instruction = "*the dealer is thinking*"

              RenderRoom(gunHolder,NotImplemented,"")

              instruction = ""

              sleep(2.5)

              #Creates ranges of what choice will be the outcome of a randInt() (index 0 will be the lowest number and index 1 will be the highest number in that range),
              #If within the liverange, choose to shoot the player, if within blankrange choose to shoot yourself (dealer)
              #This serves so that the dealer knows what rounds are left but doesn't know the order and chooses based on chance
              #Similar to how the player has to play.

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

               #Same as player shooting logic, resets currentMatch depending on if player has lost life

              if target == "player":
                    RenderRoom(gunHolder,"Other","The dealer aims the gun at you...")
                    #print("\nThe dealer aims the gun at you...")
                    sleep(3)
                            

                    if activatedRound == "x":
                         print("BANG!!")
                         playerLife -= 1
                         sleep(1)
                         print("You lose a life")
                         sleep(1.5)
                         currentMatch = False
                    else:
                         print("*click*")
                         sleep(1)
                         print("It was a blank...")
                         sleep(1.5)
                    gunHolder = "player"

              elif target == "dealer":
                    RenderRoom(gunHolder,"Self","The dealer aims the gun at themselves...")
                    
                    sleep(3)

                    if activatedRound == "x":
                         print("BANG!!")
                         dealerLife -= 1
                         sleep(1)
                         print("The Dealer loses a life")
                         sleep(1.5)
                         currentMatch = False
                    else:
                         print("*click*")
                         sleep(1)
                         print("It was a blank...")
                         sleep(1.5)
    if playerLife > 0 and dealerLife > 0:
         RenderRoom(gunHolder,NotImplemented,"Lets run that back again...")
    else:
         winner = NotImplemented

         if playerLife == 0:
              winner = "dealer"
         else:
              winner = "player"

              instruction = "The game has finished, to play again restart program"

         RenderRoom(winner,"Other",f"The {winner} Wins!!!!")
         
    
    sleep(3)
 
              
              
                             
                             
                              
                             
                        
                        



   















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