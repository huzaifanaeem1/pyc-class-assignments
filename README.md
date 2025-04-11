Assignment 2: Pyramid Pattern
Write a Python program to draw a pyramid of "*" using loops and string repetition.

Example Output:
    *
   ***
  *****
 *******
*********
Guidelines:
Use a loop to print each row of the pyramid.
Center align the stars using spaces.
You may use string multiplication (*) to repeat characters.
Assignment 3: Diamond Pattern
Write a Python program to draw a diamond of "*" using loops and string repetition.

Example Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
Guidelines:
First, print the upper pyramid (similar to the previous assignment).
Then, print the inverted pyramid below it.
Ensure the diamond remains symmetric.
Assignment 4: Deductive Logic Game - Guess the Secret Number
Write a Python program that implements a deductive logic game where the player must guess a secret three-digit number based on hints.

Game Rules:
The program generate a random three-digit secret number (e.g., "631").
The player has 10 attempts to guess the secret number.
After each guess, the program provides feedback:
“Correct” or 👌 → A correct digit in the correct place.
“Ok” or 👍 → A correct digit in the wrong place.
“Wrong” or ❌ → No correct digits.
The game ends if the player guesses correctly or exhausts all attempts.
Example Interaction:
Welcome to the Guessing Game!

Guess a 3-digit number: 123
❌👍👍 or Wrong Ok Ok

Guess a 3-digit number: 124
❌❌👍 or Wrong Wrong Ok

Guess a 3-digit number: 561
❌👌👍 or Wrong Correct Ok

Guess a 3-digit number: 671
❌👌👌 or Wrong Correct Correct

Guess a 3-digit number: 981
❌❌👌 or Wrong Wrong Correct

Guess a 3-digit number: 691
❌👌👌 or Wrong Correct Correct

Guess a 3-digit number: 621
❌👌👌 or Wrong Correct Correct

Guess a 3-digit number: 631
👌👌👌 or Correct Correct Correct or You Got IT
...
