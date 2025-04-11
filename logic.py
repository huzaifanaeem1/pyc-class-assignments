import random

def get_feedback(guess, secret_number):
    feedback_emojis = []
    feedback_message = []

    for i in range(3):
        if guess[i] == secret_number[i]:
            feedback_emojis.append("👌")
            feedback_message.append("Correct")
        elif guess[i] in secret_number:
            feedback_emojis.append("👍")
            feedback_message.append("Ok")
        else:
            feedback_emojis.append("❌")
            feedback_message.append("Wrong")

    return feedback_emojis, feedback_message


def main():
    print("🎮 Welcome to the Guessing Game!")
    secret_number = str(random.randint(100, 999)) 
    attempts = 10

    while attempts > 0:
        guess = input("🔢 Guess a 3-digit number: ")

        if len(guess) != 3 or not guess.isdigit():
            print("⚠️ Invalid input! Please enter a valid 3-digit number.")
            continue

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it right: {secret_number}")
            break
        else:
            feedback_imojis, feedback_message = get_feedback(guess, secret_number)
            print(" ".join(feedback_imojis), "or", " ".join(feedback_message))

        attempts -= 1
        print(f"🔁 Attempts left: {attempts}\n")

    if attempts == 0:
        print(f"❌ Game Over! The secret number was {secret_number}.")

if __name__ == "__main__":
    main()
