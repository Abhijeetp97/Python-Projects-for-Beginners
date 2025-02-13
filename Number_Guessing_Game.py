import random

def main():
    print("Welcome to the Enhanced Version of Number Guessing Game!")

    #Get the number range from the player
    min_value = int(input("Enter minimum value for the number range: "))
    max_value = int(input("Enter maximum value for the number range: "))

    if min_value >= max_value:
        print("Invalid range! The maximum value must be greater than minimum value.")
        return
    
    best_score = None

    while True:
        guess_num = random.randint(min_value, max_value)
        attempts = 0

        #Get the maximum number of attempts allowed for the game
        max_attempts = int(input("Enter the maximum number of guesses allowed: "))

        
        print(f"I have selected a number between {min_value} and {max_value}. Can you guess what it is? You have {max_attempts} attempts.")

        while attempts < max_attempts:
            guess = input(f"Attempt {attempts+1}> Guess the number: ")

            try:
                guess = int(guess)
                attempts += 1

                if guess < min_value or guess > max_value:
                    print(f"Please enter a number between {min_value} and {max_value}.")
                elif guess < guess_num:
                    print("Too low!! Try again.")
                elif guess > guess_num:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You have guessed the correct numer in {attempts} attempts.")
                    if best_score is None or attempts < best_score:
                        best_score = attempts
                    break
            except ValueError:
                print("Invalid Input! Please enter a valid number.")

        if  attempts == max_attempts:
            print(f"Sorry, you've used up all your attempts. The correct number was {guess_num}. Better luck next time.")

        print(f"Best Score so far is {best_score} attempts.")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()