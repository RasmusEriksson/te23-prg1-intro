print("Välkommen till tärnings spelet!!!!")
input("\nInput enter för att börja  ")



def repeatUntilInt(max,min,msg):
    while True:
        nummer = input(f"\t{msg}")

        if nummer:
            if nummer.isdigit():
                if int(nummer) > max or int(nummer) < min:
                    print(f"Ditt tal är inte gilltigt! Skriv ett tal mellan {min}-{max}!")
                else:
                    return int(nummer)
            else:
                print(f"ERROR: snälla skriv ett tal! (tal mellan {min}-{max})")
        else:
            print(f"ERROR: snälla skriv ett tal! (tal mellan {min}-{max})")
        
        

print("\nVill du spela med en fysisk tärning eller en digital tärning?")
print("Skriv '1' för fysiskt,    eller '2' för digital")


modeType = repeatUntilInt(2,1,"Välj Mode: ")


from random import randint

runda = 1
gameOver = False
vinnare = NotImplemented

datorPoäng = 0
spelarePoäng = 0




while gameOver == False:
    
    if runda == 1:
        #S kriver ut regler för första rundan
        print("\n------------Regler-------------")
        if modeType == 1:
            print("\nVarje runda ska du slå en fysisk tärning, sedan skriver du ner vilket nummer du fick")
        else:
             print("\nVarje runda kan du slå en digital tärning genom att trycka enter")
        print("Efter det så kommer datorn slå sin tärning, den som får högst nummer är den som får poäng")
        print("Först till 5 poäng vinner, lycka till!")
        print("\n-------------------------------------------")
        

    # Skriver ut vilken runda det är och hur många poäng varje sida har
    print(f"\nRunda {runda}!")
    print(f"Spelare:{spelarePoäng} - Dator:{datorPoäng}")

    # spelaren skriver vilket nummer den fick när den slog sin tärning
    print("\nSlå din tärning...")

    if modeType == 1:
        spelareNum = repeatUntilInt(6,1,"Skriv talet du fick: ")
    else:
        input("Input enter för att slå tärningen: ")
        spelareNum = randint(1,6)

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
print(f"\tSpelare:{spelarePoäng} - Dator:{datorPoäng}")
print("\n-------------------------------------------")







