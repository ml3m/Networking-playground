# the hangman game idea
# - chose random word 
# - create a list of empty spaces of len(random_word)
# - take user_letter and check if in the random_word if it is then guessable
# '_' gets replaced with user_letter, do this until the guessable word has no
# '_'s left and is equal with the init random_word


word = 'cat'
guessable = ['_'] * len(word)

while True:
    print(''.join(guessable))

    user_letter = input('Enter a letter: ')

    for i in range(len(word)):
        if user_letter == word[i]:
            guessable[i] = user_letter

    if ''.join(guessable) == word:
        break

print(f'The word was found: {''.join(guessable)}')
