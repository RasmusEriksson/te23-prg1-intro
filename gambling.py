print("Välkommen till tärnings spelet!!!!")
input("\nInput enter för att börja  ")

from random import randint

runda = 1
gameOver = False
vinnare = NotImplemented

datorPoäng = 0
spelarePoäng = 0


#In progress function
def repeatUntilInt():
    while True:
        nummer = input("\tSkriv numret du fick: ")

        if nummer:
            if nummer.isdigit == True:
                return int(nummer)
            else:
                print("ERROR: snälla skriv in det nummer du fick på din tärning (tal mellan 1-6)")
        else:
            print("ERROR: snälla skriv in det nummer du fick på din tärning (tal mellan 1-6)")






while gameOver == False:
    
    if runda == 1:
        #S kriver ut regler för första rundan
        print("\n------------Regler-------------")
        print("\nVarje runda ska du slå en fysisk tärning, sedan skriver du ner vilket nummer du fick")
        print("Efter det så kommer datorn slå sin tärning, den som får högst nummer är den som får poäng")
        print("Först till 5 poäng vinner, lycka till!")
        print("\n-------------------------------------------")

    # Skriver ut vilken runda det är och hur många poäng varje sida har
    print(f"\nRunda {runda}!")
    print(f"Spelare:{spelarePoäng} - Dator:{datorPoäng}")

    # spelaren skriver vilket nummer den fick när den slog sin tärning
    print("\nSlå din tärning...")

    #spelareNum = repeatUntilInt()
    spelareNum = input("\tSkriv numret du fick: ")
    spelareNum = int(spelareNum)

    # Datorn slår sin tärning
    datorNum = randint(1,6)

    print(f"\nSpelare:{spelareNum}\nDator:{datorNum}")

    # Kollar vilken som vann, om det blir lika så ändras inget och rundan spelas om
    if spelareNum > datorNum:
        print("\n\tSpelaren Vann!")
        spelarePoäng += 1
        runda += 1
    elif spelareNum < datorNum:
        print("\n\tDatorn vann!")
        datorPoäng += 1
        runda += 1
    else:
        print("\n\tDet blev lika! Rundan spelas om...")
    print("\n______________________________")

    # Kollar om någon har nog med poäng för att vinna, 
    # om det är sant så slutas spelet och vinnaren bestäms
    if spelarePoäng >= 5:
        vinnare = "Spelaren"
        gameOver = True
    elif datorPoäng >= 5:
        vinnare = "Datorn"
        gameOver = True
    
print("\nGAME OVER")
print("\n-------------------------------------------")
print(f"\n\t{vinnare} Vann hela spelet!!!")
print("\n-------------------------------------------")







