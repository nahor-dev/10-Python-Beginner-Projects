import random # this select random number 
comp = random.randrange(1,100) # select random number from this range 

while True: # to ask till user gets it 
    num = int(input('guess a number from 1 to 100:  '))
    if num == comp:
        print(f'you guessed {num} and computer number is {comp}. its right ')
        respond = input('want to continue (y/n): ')
        if respond == 'n':
            break
            
    elif num > comp:
        print('go down')
    elif  num < comp:
        print('go up')
        

