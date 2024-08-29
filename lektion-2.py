print("Yuh wassup, this my program")
# Print a welcoming statment
Name = input("What's yo name:  ")
# Let the user assign a variable via the input function
print(f"Oh, welcome {Name}!")
# Formating both string and the variable with f
# Yeah not writing comments everywhere haha :P'ä´

print("Now my next question will be, how old are you?")




def DefineAge():
        Age = input("Input Your Age: ")
        if Age:
            if Age.isdigit() == True:
                print(Age)
                return int(Age)
            else:
                print("Sorry, please input a valid number for age!")
                DefineAge()
        else:
            print("Please write a value in the input!")
            DefineAge()
        
            
        
    

    

  

# Doesn't work, not my problem

UserAge = DefineAge()  


    
if UserAge >= 15:
    print(f"Wow, you are a ripe age of {UserAge} years old!")
else:
    print(f"You're only {UserAge}? that's way too young")

    

print(f"That means that you will be {UserAge + 1} years old next year!")









