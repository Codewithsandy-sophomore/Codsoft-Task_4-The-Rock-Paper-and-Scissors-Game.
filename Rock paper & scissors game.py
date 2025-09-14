import random

def play_game():
    user_score=0
    comp_score=0
    print("🎮 Welcome to Rock, Paper, Scissors 🎮")
    print("First to 5 points wins the match!\n")
    
    while True:
        print("Make your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice=input("Enter 1/2/3: ")
        
        if choice not in ["1","2","3"]:
            print("Invalid choice, try again.\n")
            continue
        
        user_choice={"1":"Rock","2":"Paper","3":"Scissors"}[choice]
        comp_choice=random.choice(["Rock","Paper","Scissors"])
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        
        if user_choice==comp_choice:
            print("It’s a tie!\n")
        elif (user_choice=="Rock" and comp_choice=="Scissors") or (user_choice=="Scissors" and comp_choice=="Paper") or (user_choice=="Paper" and comp_choice=="Rock"):
            print("🎉 You win this round!\n")
            user_score+=1
        else:
            print("💻 Computer wins this round!\n")
            comp_score+=1
        
        print(f"Score → You: {user_score} | Computer: {comp_score}\n")
        
        if user_score==5 or comp_score==5:
            if user_score>comp_score:
                print("🏆 Congratulations! You win the match! 🏆\n")
            else:
                print("😢 Computer wins the match. Better luck next time!\n")
            break
        
        again=input("Play again? (yes/no): ").lower()
        if again!="yes":
            print("Thanks for playing! 👋")
            break

play_game()
import random

def play_game():
    user_score=0
    comp_score=0
    print("🎮 Welcome to Rock, Paper, Scissors 🎮")
    print("First to 5 points wins the match!\n")
    
    while True:
        print("Make your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice=input("Enter 1/2/3: ")
        
        if choice not in ["1","2","3"]:
            print("Invalid choice, try again.\n")
            continue
        
        user_choice={"1":"Rock","2":"Paper","3":"Scissors"}[choice]
        comp_choice=random.choice(["Rock","Paper","Scissors"])
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        
        if user_choice==comp_choice:
            print("It’s a tie!\n")
        elif (user_choice=="Rock" and comp_choice=="Scissors") or (user_choice=="Scissors" and comp_choice=="Paper") or (user_choice=="Paper" and comp_choice=="Rock"):
            print("🎉 You win this round!\n")
            user_score+=1
        else:
            print("💻 Computer wins this round!\n")
            comp_score+=1
        
        print(f"Score → You: {user_score} | Computer: {comp_score}\n")
        
        if user_score==5 or comp_score==5:
            if user_score>comp_score:
                print("🏆 Congratulations! You win the match! 🏆\n")
            else:
                print("😢 Computer wins the match. Better luck next time!\n")
            break
        
        again=input("Play again? (yes/no): ").lower()
        if again!="yes":
            print("Thanks for playing! 👋")
            break

play_game()
