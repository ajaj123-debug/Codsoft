import random

def main():
    print("Rock Paper Scissor Game")
    # 0 for Rock
    # 1 for Paper
    # 2 for Scissor
    print("Enter 0 for Rock, 1 for Paper, 2 for Scissor")
    user_input = int(input())
    computer_input = random.randint(0, 2)
    
    if user_input == computer_input:
        print("Tie-up")
    elif (user_input == 0 and computer_input == 2) or (user_input == 2 and computer_input == 1) or (user_input == 1 and computer_input == 0):
        print("You win")
    else:
        print("Computer wins")

if __name__ == "__main__":
    main()
