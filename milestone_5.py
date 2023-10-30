import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'watermelon', 'strawberry', 'pineapple', 'blueberry', 'kiwi']
    return random.choice(words)

def display_hangman(tries):
    stages = [  
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |      
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    guessed_word = ['_'] * len(word)
    tries = 6

    while tries > 0 and '_' in guessed_word:
        print(display_hangman(tries))
        print(' '.join(guessed_word))
        
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print("You've already guessed this letter. Try another one.")
            continue

        if guess in word_letters:
            guessed_letters.add(guess)
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

    if '_' not in guessed_word:
        print(f'Congratulations! You guessed the word: {word}')
    else:
        print(display_hangman(tries))
        print(f"Sorry, you ran out of tries! The word was: {word}")

if __name__ == "__main__":
    hangman()