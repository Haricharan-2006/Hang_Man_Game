#hangman - project
import random
STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,  # 0 lives: Game Over
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,  # 1 life
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,  # 2 lives
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
       -
    """,  # 3 lives
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
       -
    """,  # 4 lives
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,  # 5 lives
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """   # 6 lives: Initial State
]
words = ["apple", "banana", "cherry", "dog", "elephant", "forest", "guitar", "house", "island", "jungle"]
number_of_lives = 6
number_of_correct_guess = 0
random_word = random.choice(words)
print("Welcome to Hangman Game!! You have 6 lives to guess the word(One wrong guess takes one life)")
lis = ["_"]*len(random_word)
guess_letters = []
for i in lis:
    print(i,end = " ")
print("")
while number_of_lives and number_of_correct_guess != len(random_word):
    char_input = input("Guess the Character: ").lower()
    if len(char_input) > 1:
        print("Invalid Input... Enter only one character")
    elif char_input in guess_letters:
        print("Already guessed the letter..Try another one!")
    elif char_input in random_word:
        count = 0
        for i in range(len(random_word)):
            if random_word[i] == char_input:
                lis[i] = char_input
                count += 1
            print(lis[i],end = " ")
        print("")
        guess_letters.append(char_input)
        number_of_correct_guess += count
    else:
        number_of_lives -= 1
        print(f"You lost one life.You have {number_of_lives}/6 remaining.")
    print(STAGES[number_of_lives])
if number_of_correct_guess == len(random_word):
    print("You won the game!")
else:
    print("You lose the game!")
