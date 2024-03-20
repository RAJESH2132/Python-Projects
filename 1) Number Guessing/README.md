# Number Guessing Game

This is a simple number guessing game implemented in Python. The program generates a random number within a specified range, and the user has to guess that number within a limited number of attempts.

## Features

- Allows the user to set the lower and upper bounds for the range of numbers.
- Informs the user about the minimum number of guesses required to find the number.
- Gives feedback to the user after each guess, indicating whether the guess is too high or too low.
- Congratulates the user upon guessing the correct number within the allowed number of attempts.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Run the script `main.py`.
4. Follow the prompts to input the lower and upper bounds for the range of numbers.
5. Start guessing the number.
6. Keep guessing until you find the correct number or exhaust your attempts.

## Logic for Calculating Minimum Guesses

The program calculates the minimum number of guesses required using the formula:

    min_guesses = round(math.log(upperBound - lowerBound + 1, 2))

This formula calculates the logarithm base 2 of the range of numbers, which provides an estimate of the minimum number of guesses needed to find the correct number using a binary search strategy.

## Example

Enter the Lower Bound: 1
Enter the Upper Bound: 100

  You've only  7  chances to guess the Number!

Guess the Number: 50
You Guessed too high!

Guess the Number: 25
You guessed too small!

Guess the Number: 38
You guessed too small!

Guess the Number: 44
You Guessed too high!

Guess the Number: 41
Congratulations you did it in  5  try

Feel free to modify and extend the code as needed. Happy coding!
