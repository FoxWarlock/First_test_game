# ДЗ 3-8 камень ножницы бумага rock scissors paper
import random

# rock-1 scissors-2 paper-3
print('shall we play a game, "rock scissors paper"?')

end_game = 'y'
while end_game=='y':
    x = random.randint(1,3)
    o = input('Choose one element: r - rock, s - scissors, p - paper')
    print('My element: Rock') if x==1 else print('My element: Paper') if x==3 else print("My element: Scissors")
    print("Your element: Rock") if o=='r' else print("Your element: Papper") if o=='p' else print("Your element: Scissors")
    if (o=='r' and x==2) or (o=='p' and x==1) or (o=='s' and x==3):
        print('You win!')
        end_game=input('do you want to continue = y - yes, n - no: ')
    elif (o=='r' and x==1) or (o=='p' and x==3) or (o=='s' and x==2):
        print('Draw!')
        end_game=input('do you want to continue = y - yes, n - no: ')
    else:
        print('You lose!')
        end_game=input('do you want to continue = y - yes, n - no: ')