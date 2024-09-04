print("Yuh wassup, this my program")
# Print a welcoming statment
name = input("\tWhat's yo name:  ")
# Let the user assign a variable via the input function
print(f"Oh, welcome {name}!")
# Formating both string and the variable with f
# Yeah not writing comments everywhere haha :P'ä´

print("Now my next question will be, how old are you?")




def DefineAge():
        
        while True:
             age = input("\tInput your age: ")
             if age:
                  if age.isdigit() == True:
                       return(int(age))
                  else:
                       print("Sorry! Please input a valid number for your age! (like \"16\" or \"72\")")
             else:
                  print("Sorry! Please input a value! (like \"16\" or \"72\")")
        
            
        
    

    

  

# Doesn't work, not my problem

userAge = DefineAge()  


    
if userAge >= 15:
    print(f"Wow, you are a ripe age of {userAge} years old!")
else:
    print(f"You're only {userAge}? that's way too young")

    

print(f"That means that you will be {userAge + 1} years old next year!")









