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

print("Let the games commence!")

playerLife = 3
dealerLife = 3

currentMatch = False


#shuffledRounds = []

liveRoundQouta = 1
blankRoundQouta = 2


gunHolder = "player"

while dealerLife > 0 and playerLife > 0:
    roundsList = []
    shuffledRounds = []

    while currentMatch:
         if gunHolder == "player":
              print("yippie!")
    
    #Set up for the rounds being inserted
    roundCount = randint(3,5)


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
    print("They are inserted in a random order")

    print(f"Unshuffled List: {roundsList}")

    for i in range(len(roundsList)):
         indexShuffle = i-1
         index = randint(0,len(roundsList)-1)

         Round = roundsList[index]
         roundsList.pop(index)

         shuffledRounds.append(Round)
    
    print(f"Shuffled List: {shuffledRounds}")


    yeild = input("stopcode")



   















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