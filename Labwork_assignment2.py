# Let's build a guess game.
# In this game we would have a secret number and then
# ask the user to Guess the secret number.
# If the user guesses it right before the 5th guess,
# the user wins and if he doesn't the user loses the guess.


name = input('Enter your name:')
# print(f'{name}, welcome to the guess game ')

sn = 9
gn = int(input(f'Dear {name}, welcome to the guess game.\nEnter your guess number:'))

if gn != sn :
    print(int(input('Try another number: ')))

# elif gn != sn :
#     print('game over')

else :
    print(f'{name}, congratulations, you have won the game ')