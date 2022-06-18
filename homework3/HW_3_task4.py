import requests


pokemon_ID_1 = input('What is pokemon_1 ID? ')
pokemon_ID_2 = input('What is pokemon_2 ID? ')
pokemon_ID_3 = input('What is pokemon_3 ID? ')
pokemon_ID_4 = input('What is pokemon_4 ID? ')
pokemon_ID_5 = input('What is pokemon_5 ID? ')
pokemon_ID_6 = input('What is pokemon_6 ID? ')

pockemon_ids = [pokemon_ID_1, pokemon_ID_2, pokemon_ID_3, pokemon_ID_4, pokemon_ID_5, pokemon_ID_6]
with open('pokemon.txt', 'w') as file:
    for pokemon_num in pockemon_ids:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_num)
        r = requests.get(url)
        pokemon_data = r.json()
        moves = pokemon_data['moves']
        moves_str = ', '.join([move['move']['name'] for move in moves])
        file.write('pokemon name is {name}  '.format(name=pokemon_data['name']))
        file.write('pokemon moves are: {moves_str} \n'.format(moves_str=moves_str))
        