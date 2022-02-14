import random

variable = 'abcdefghijklmnopqrstuvwxyz123456789'

while True:
    nitro = ''

    for i in range(24):

        nitro = f'{nitro}{random.choice(variable)}'
    
    print(f'https://discord.gift/{nitro}')

    with open('nitro gratuit.txt', 'a') as file:
        file.write(f'https://discord.gift/{nitro}\n')
