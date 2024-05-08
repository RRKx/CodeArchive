mystery_word = input("Enter a word to guess: ")
mystery_characters = []
dash_characters = []

for i in mystery_word:
    mystery_characters.append(i)
    dash_characters.append("_")

wrong_guess = 0
tries = 7
won = False

def main(guess, mystery_characters):
    if guess in mystery_characters:
        for x in mystery_characters:
            if x == guess:
                guess_Index = mystery_characters.index(guess)
                mystery_characters.pop(guess_Index)
                dash_characters.pop(guess_Index)
                mystery_characters.insert(guess_Index, "RemovedValue")  
                dash_characters.insert(guess_Index, guess)
        
        string = '\n'
        for i in dash_characters:
            string = string + i
        print(string)
    else:
        global wrong_guess, tries
        wrong_guess = wrong_guess + 1
        tries = tries - 1
        print(f"\nYou guessed wrong! You have {tries} tries left.")

    if "_" not in dash_characters:
        global won
        won = True
        print("\nYou won!")

while wrong_guess < 7 and not won:
    guess = input("Guess a letter: ")
    main(guess, mystery_characters)