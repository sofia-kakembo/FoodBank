import requests
from pprint import pprint

pokemon_list = []
pokemon_namelist =[]
pokemon_movelist =[]

for choose in range (6): #hago repetir 6 veces para armar la lista
    choose = int(input ("select 1 poke nr"))
    pokemon_list.append (choose)
print ("Pokemon List ID: ", pokemon_list)

for num in pokemon_list: #hago repetir por cada elemento de la lista
    num2 = num + 1 # le sumo uno
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(num) #no se bien como lo hice pero salio bien
    #    print(url)

    response = requests.get (url) #pido a la api la url de cada elemento de la lista
    #    print (response)

    pokemon44 = response.json() #pido la respuesta en json

    pokemon_name = pokemon44 ["name"] #asigno variable para q busque el nonmbre dentro de la respuesta
    pokemon_namelist.append(pokemon_name)

    #moves = pokemon ["moves"]
    #for move in moves:
        #print(move ["move"]["name"])
     #   pokemon_movelist.append(move["move"]["name"])
print ("Pokemon list names: ", pokemon_namelist)
#print ("Pokemon moves list: ", pokemon_movelist)

def saves_pokemon_to_file(new_pokemon):
    # find a good way to save the pokemon without overwriting the file
    with open('pokemon.txt', 'r') as text_file:
        pokemon_file = text_file.read()
    pokemon44 = pokemon_file + new_pokemon + '\n'
    with open('pokemon.txt', 'w+') as text_file:
        text_file.write(pokemon44)
# loop through each pokemon and save to the file using the function
for pokemon44 in pokemon_namelist:
    saves_pokemon_to_file(pokemon44)


#moves = pokemon['moves'] # lo copie del ejemplo, sino los moves quedaban muy largos, creo
#for move in moves: # q asi es q pone solo el nombre del move
    #pprint(move['move']['name'])

    #se me ocurrio hacer un diccionario para poder imprimir todos los names y moves de los pokemones
    #en un archivo. sino solo me escribe el ultimo.

    #poke_dict = [{"id": num, "name": pokemon_name,}]
    #for poke in poke_dict:
    #print (poke["name"])

    #pprint (poke_dict)
    #print (poke_dict)
    #        for dato in poke_dict:
    #            print (poke_dict["name"])


    #with open ("pokemon.txt", "r") as pokemon_file:
    #    names = pokemon_name + "\n"
    #    pokemon_file.read()

    #names2 = names + pokemon_name + "\n"

#with open ("pokemon.txt", "r") as pokemon_file:
#    poke =  pokemon_name
#    pokemon_file.readlines()
#with open ("pokemon.txt", "w+") as pokemon_file:
#    poke2 = pokemon_namelist[0] + ", " + pokemon_namelist[1] + ", " + pokemon_namelist[2] + ", " + pokemon_namelist[3] + ", " + pokemon_namelist[4]+", "+pokemon_namelist[5]
#    pokemon_file.write(poke2)
#    pokemon_file.writelines(pokemon_movelist)

   #moves = pokemon ["moves"]
   # print (names)
 #   pokemon_file.write(names)