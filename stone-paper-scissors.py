from random import randint
print("This is Stone-Paper-Scissors Game")

print("Choice 1: STONE")
print("Choice 2: PAPER")
print("Choice 3: SCISSORS")

score = 0

while True:
    choice = ["stone", "paper", "scissors"]
    
    pc = choice[randint(0, 2)]
    
    user = int(input("Enter your choice: "))
    
    if user == 1:
        user_choice = "stone"
    elif user == 2:
        user_choice = "paper"
    elif user == 3:
        user_choice = "scissors"
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
        continue
    
    print("Computer's choice:", pc)
    print("Your choice:", user_choice)
    
    if user_choice == pc:
        print("It's a draw!")
    elif (user_choice == "stone" and pc == "scissors") or (user_choice == "paper" and pc == "stone") or (user_choice == "scissors" and pc == "paper"):
        print("You win!")
        score += 1
    else:
        print("Computer wins!")
        score -= 1
    
    print("Score:", score)
    break

        
        

        
        

