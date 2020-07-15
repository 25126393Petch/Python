import random

"""Your assignment is to code, in python 3, a game of hangman. Specifically the program should choose a word from a predefined bank of words (the attached "word_list.docx"
you should download this and convert it to a .txt file, unfortunately .txt files cannot be attached to this site, frustratingly), and display to the user how many letters 
the word is (i.e. " ******** ". The user should then be able to guess one letter at a time, with the program either taking a "life" from them if it is an incorrect guess, 
or showing that the letter is correct and where it appears in the word (i.e. ***a**a*). The game ends when the user runs out of guesses (let's say 7 incorrect guesses) 
or the player has filled in all the letters of the word.

We require that the program you write does some things in a very specific way so please follow the bullet points below to the letter otherwise your program will be 
automatically failed.

The program must run in Python3 without error.
The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or other user input).
Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are necessary (I think)): “Please enter your next guess: “
The text printed before “Please enter your next guess: “ must END in the word to be guessed with the unknown letters starred out (i.e. hello would start as ***** and 
change into *e*** after ‘e’ was guessed). The string must not contain any other stars.
The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path (i.e. "open('word_list.txt', ...)").
If the user makes 7 wrong guesses then they lose the game.
now
"""

# import wordlist as list of words
with open("word_list.txt") as f:
    words = f.read().splitlines()

# uniformly randomly declare a word to be the target word - https://stackoverflow.com/questions/4394145/picking-a-random-word-from-a-list-in-python
targetWord = random.choice(words)
guesswords = list(targetWord) 

# generate string of asterisks the same length as the targetWord
hiddenWord = len(targetWord) * '*'
hiddenWordlist = list(hiddenWord)
print("Welcome to Hangman! Guess the word:")
print(hiddenWord)

# define how many guesses left and a list of guessed characters
guessesLeft = 7
lettersGuessed = []
wordReveal = list(len(targetWord) * '*')

# game loop that continues until all lives are spent or game is won
while guessesLeft > 0:
    
    # receive player input and check for errors

    # convert player entry to lowercase and string, if this fails, continue and identify the error
    try:
        guess = str(input("Please enter your next guess: ")).lower()
    except:
        continue

    if not guess.isalpha(): # ensure entry is a valid character
        print("You did not enter a letter.")    
    elif guess == "": # check for blank entry 
        print("Please enter a letter")
    elif len(guess) > 1: # ensure single-character entry
        print("Please only enter one letter.")
    elif guess in lettersGuessed: # check if the letter has previously been guessed
        print("You have already guessed that letter.")
    else:  # player entry is valid - continue

        # add player guess to list for tracking previous guesses
        lettersGuessed.append(guess)
        
        # check each character in guesswords by iterating each character index of the word and compare it to the guessed letter. 
        # If the letter matches then the corresponding wordReveal index is changed from an asterisk to the revealed letter.
        i = 0 
        while i < len(hiddenWord):
            if guess == targetWord[i]:
                wordReveal[i] = guesswords[i]
            i += 1
        print(''.join(wordReveal))
        
        # check for incorrect guess and decrement guesses
        if wordReveal == hiddenWordlist:
            print("Sorry, that letter is not in the word.")
            guessesLeft -= 1
            print("You have {} lives remaining".format(guessesLeft))
                  
        # check for correct guess
        if wordReveal != hiddenWordlist:
            print("Yes! That letter is in the word!")
            hiddenWordlist = wordReveal[:] #make hiddenWordlist the same as wordReveal
            # check for complete win
            if wordReveal == guesswords:
                print("Congratulations you win") # The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
                quit()
print("The word was:",targetWord)
print("You lose")
quit()