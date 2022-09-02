import pokebase as pb;

print('Using POKEAPI,this program will return the height and weight of a pokemon');

pokeSearch = input("Please enter Pokemon's name: ");
pokeSearch = pokeSearch.lower();

print(pokeSearch,"'s weight is: ", pb.pokemon(pokeSearch).weight);
print(pokeSearch,"'s height is: ", pb.pokemon(pokeSearch).height);


print('Thank you');