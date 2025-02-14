# Python-Projects-for-Beginners

Welcome to the "Python-Projects-for-Beginners" repository! This repository contains a collection of simple Python projects designed to help beginners learn and practice their Python skills. Each project focuses on different aspects of Python programming and provides a hands-on learning experience.

## Projects Included

This repository includes the following projects:

1.  **Dice Roller Simulation**
    *   Simulates rolling a pair of dice (or any number of dice).
    *   Generates random results for each die roll.
    *   Keeps count of the total number of rolls in a session.
    *   Provides user-friendly prompts and error handling.

2.  **Enhanced Number Guessing Game**
    *   A classic number-guessing game with enhancements.
    *   Customizable number range.
    *   Limited number of guesses.
    *   Tracks and displays the best score.

3.  **Rock, Paper, Scissors Game**
    *   Simulates the classic Rock, Paper, Scissors game.
    *   Offers single-player (vs. computer) and two-player modes.
    *   Keeps track of wins, losses, and ties.
    *   Declares the overall winner in a best-of-three format.

4.  **QR Code Generator**
    *   Generates QR codes from text or URLs.
    *   Allows customization of QR code and background colors.
    *   Supports generating multiple QR codes at once.

5.  **Currency Converter**
    *   Converts currency from one type to multiple currencies.
    *   Includes a range of currencies (USD, EUR, JPY, GBP, INR, CAD, AUD, CHF, CNY, SEK).
    *   Maintains a history of conversions.

6.  **Quiz Game**
    *   An interactive quiz game with multiple-choice questions.
    *   Questions are loaded from a JSON file for easy updating.
    *   Supports multiple categories and difficulty levels.
    *   Shuffles questions for a random experience.

## Getting Started

To get started with these projects, follow these steps:

1.  Clone the repository to your local machine:

    ```
    git clone [repository URL]
    ```

2.  Navigate to the project directory you want to explore.

3.  Make sure you have Python 3.x installed.

4.  Install any required libraries (if applicable - see project details below).

5.  Run the Python script for the project.

## Project Details and Requirements

Here's a more detailed look at each project, including any specific requirements:

### 1. Dice Roller Simulation

*   **Requirements:** Python 3.x
*   **How to Use:**
    *   Run the program.
    *   Enter 'y' to roll the dice.
    *   Specify the number of dice to roll.
    *   View the results and the total count of rolls.
    *   Repeat or exit by entering 'n'.

### 2. Enhanced Number Guessing Game

*   **Requirements:** Python 3.x
*   **How to Play:**
    *   Run the program.
    *   Enter the minimum and maximum values for the number range.
    *   Enter the maximum number of guesses allowed.
    *   Start guessing the number within the specified range.
    *   Receive hints if the guess is too high or too low.
    *   Continue guessing until the number is correctly guessed or the maximum attempts are reached.
    *   View your score and the best score so far.
    *   Option to play again or exit the game.

### 3. Rock, Paper, Scissors Game

*   **Requirements:** Python 3.x
*   **How to Play:**
    *   Run the program.
    *   Choose the game mode: Single Player vs. Computer or Two Players.
    *   Players take turns to input their choices (rock, paper, or scissors).
    *   The program displays the choices using emojis and determines the winner of each round.
    *   Continue playing until a best-of-three winner is declared.
    *   View the game statistics and choose to restart or exit.

### 4. QR Code Generator

*   **Requirements:** Python 3.x, `qrcode` and `Pillow` libraries.
*   **Installation:**

    ```
    pip install qrcode[pil]
    ```

*   **How to Use:**
    *   Run the program.
    *   Enter the desired color for the QR code and the background color.
    *   Input the text or URLs to generate QR codes, separated by commas.
    *   Provide filenames for each QR code, separated by commas.
    *   The program will generate the QR codes and save them with the specified filenames.

### 5. Currency Converter

*   **Requirements:** Python 3.x
*   **How to Use:**
    *   Run the program.
    *   Enter the amount to convert.
    *   Input the currency to convert from (e.g., USD, EUR, JPY, GBP, INR).
    *   The program will display the equivalent amount in multiple currencies.
    *   Continue with additional conversions or exit the program to view the conversion history.

### 6. Quiz Game

*   **Requirements:** Python 3.x
*   **How to Use:**
    *   Run the program.
    *   Enter the name of the JSON file with the quiz questions (e.g., 'questions.json').
    *   Choose a category from the available options.
    *   Select a difficulty level from the available options.
    *   Answer the multiple-choice questions.
    *   Your final score will be displayed at the end of the quiz.

## Author

These projects were created by Abhijeet Patil.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new projects, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
