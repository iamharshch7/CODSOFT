import random

def play_game():
    print(" Welcome to Rock-Paper-Scissors ")
    print("Instructions: Type rock, paper, or scissors to play.")


    user_score = 0
    computer_score = 0

    while True:

        user_choice = input("\nEnter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print(" Invalid choice! Please try again.")
            continue


        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f" You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")


        if user_choice == computer_choice:
            print(" It's a Tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You Win!")
            user_score += 1
        else:
            print(" Computer Wins!")
            computer_score += 1


        print(f" Score -> You: {user_score} | Computer: {computer_score}")


        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Final Score:")
            print(f" You: {user_score} | 🤖 Computer: {computer_score}")
            print("Goodbye ")
            break

# Run the game
play_game()
