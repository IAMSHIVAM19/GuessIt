from guess import get_random_word, validate_word, get_feedback, max_attempts

# Main game loop
def main():
    # Randomly choose a secret word
    secret_word = get_random_word()
    # Introduction and instructions
    print("Welcome to GuessIt!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print("Color guide:")
    print("Green = correct letter and position")
    print("Yellow = correct letter, wrong position")
    print("Gray = incorrect letter\n")

    attempts = 0
    # Game loop: runs until max_attempts is reached
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").strip().lower()

        # Validate guess (must be 5 alphabetic characters)
        if not validate_word(guess):
            print("Invalid input. Please enter a 5-letter word.")
            continue

        # Get and display feedback on the guess
        feedback = get_feedback(secret_word, guess)
        print("Feedback:", feedback)

        # Check if user has guessed the word correctly
        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            break # Exit loop if guessed correctly

        attempts += 1

    else:
        # If all attempts used, reveal the correct word
        print(f"Out of attempts! The word was: {secret_word}")

if __name__ == "__main__":
    main()
