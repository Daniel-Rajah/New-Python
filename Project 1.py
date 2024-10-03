
"""Introduction to Game"""
name = input('Hey type your name: ')
print('Welcome ' + name)

"""Asking user if they want to play"""
should_we_play = input('Do you want to play an adventure Game? ').lower()
if should_we_play == 'yes' or 'yh':
    print('Lets Play!!')

    direction = input('Wanna go left or right?? ').lower()
    if direction == 'left':
        print('Guess we going left then...oh wait, theres a tiger...you DEAD!')
    elif direction == 'right':
        print('Oh we going right! Lets do it!')
        
        question = input('You sure you wanna keep going? ').lower()
        if question == 'yes' or 'yh':
            print('you found treasure...Lets goo! You win!')
        else:
            print('Lets go back then!')
else:
    print('fuck off then!')
    print('hello')
    print('Does it work?')


