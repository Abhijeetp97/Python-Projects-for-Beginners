import random

valid_choice = ('r', 'p', 's')

#Get computer choice
def get_comp_choice():
    return random.choice(valid_choice)

#Get player choice
def get_player_choice(player_no):
    choice = input(f"Player {player_no},enter your choice (r for rock, p for paper, s for scissor): ").lower()
    while choice not in valid_choice:
        choice = input(f"Invalid choice! Player {player_no}, please enter one of the following 'r', 'p', or 's': ").lower()
    return choice

#Add emojies to the choices
def display_choices(player1_choice, player2_choice, player2_name):
    choices = {
        'r': '🪨 Rock',
        'p': '📃 Paper',
        's': '✂️ Scissors'
    }
    print(f"Player 1 choose: {choices[player1_choice]}")
    print(f"{player2_name} choose: {choices[player2_choice]}")

#Determine the winner of a round
def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "tie"
    elif (
        (player1_choice == 'r' and player2_choice == 's') or
        (player1_choice == 'p' and player2_choice == 'r') or
        (player1_choice == 's' and player2_choice == 'p')
    ):
        return "player1"
    else:
        return "player2"
    
#Determine main function
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    #Select game mode
    game_mode = input("Choose the game mode: (1) Single Player vs Computer, or (2) Two Players: ")
    while game_mode not in ['1', '2']:
        game_mode = input("Invalid choice! Please enter '1' for Single player vs Computer, or '2' for Two players: ")

    #Important variables
    best_of_three = True
    player1_wins = 0
    player2_wins = 0
    ties = 0
    rounds_played = 0
    player2_name = "Computer" if game_mode == '1' else "Player 2"

    #while loop ensuring the best of three format
    while (player1_wins < 2 and player2_wins < 2) if best_of_three else True:
        player1_choice = get_player_choice(1)
        player2_choice = get_comp_choice() if game_mode == '1' else get_player_choice(2)
        display_choices(player1_choice, player2_choice, player2_name)
        result = determine_winner(player1_choice, player2_choice)

        #Result & win-tie counter
        if result == "tie":
            ties += 1
            print("It's a tie!")
        elif result == "player1":
            player1_wins += 1
            print("Player 1 wins this round!")
        else:
            player2_wins += 1
            print(f"{player2_name} wins this round!")

        rounds_played += 1

        #Loop break if we have a winner
        if (player1_wins == 2 or player2_wins == 2) if best_of_three else False:
            break

        #Option to continue playing
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            break

    #Overall Winner
    if player1_wins == 2:
        print("Player 1 is the overall winner!")
    elif player2_wins == 2:
        print(f"{player2_name} is the overall winner!")

    #final game stats
    print(f"Game Over! Here are the stats: Player 1 wins: {player1_wins}, {player2_name} wins: {player2_wins}, Ties: {ties}")
    print("Thank you for playing!")


# Main function to manage the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        play_game()

        restart = input("Do you want to restart the game? (y/n): ").lower()
        if restart != 'y':
            break

    print("Thank you for playing!")

#Run the main function
if __name__ =="__main__":
    main()