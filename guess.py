import random

# ANSI color codes
GREEN = "\033[1;32m"   # Correct letter in correct position
YELLOW = "\033[1;33m"  # Correct letter in wrong position
GRAY = "\033[1;37m"    # Incorrect letter
RESET = "\033[0m"      # Reset to default color

#List of words to guess

word_list = [
    "apple", "baker", "cabin", "delta", "eagle", "frost", "glide", "honey", "ivory", "joker",
    "karma", "lunar", "mango", "noble", "orbit", "piano", "quilt", "raven", "solar", "tiger",
    "ultra", "vivid", "waltz", "xenon", "yacht", "zebra", "acorn", "blaze", "crane", "drake",
    "event", "flare", "grape", "hatch", "inlet", "jolly", "knack", "ledge", "mirth", "nifty",
    "oxide", "pleat", "query", "reign", "sweep", "trick", "unite", "venom", "woven", "xerox",
    "yeast", "zesty", "angel", "bloom", "cider", "dough", "eject", "fable", "gnome", "hasty",
    "ideal", "jazzy", "koala", "lager", "medal", "nurse", "organ", "print", "quota", "round"
]

#Maximum guesses are 6
max_attempts = 6

#Function to choose a random word from the list for guessing
def get_random_word():
    return random.choice(word_list).lower()

# Function to validate player input
# Ensures word is 5 letters and alphabetic
def validate_word(word):
    return word.isalpha() and len(word) == 5

# Function to provide feedback after each guess
# Uses color-coded letters to show correctness
def get_feedback(secret, guess):
    feedback = [""] * 5
    secret_letters = list(secret)

    # First pass: check for correct letters in correct positions
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = f"{GREEN}{guess[i]}{RESET}"
            secret_letters[i] = None  # Mark as used

    # Second pass: check for correct letters in wrong positions
    for i in range(5):
        if feedback[i] == "":
            if guess[i] in secret_letters:
                feedback[i] = f"{YELLOW}{guess[i]}{RESET}"
                # Remove the first matching instance to avoid double counting
                secret_letters[secret_letters.index(guess[i])] = None
            else:
                feedback[i] = f"{GRAY}{guess[i]}{RESET}"

    return " ".join(feedback)
