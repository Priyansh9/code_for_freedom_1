pets_count = int(input())
pos = []
anime = []

anime_dictionary = {}

for i in range(pets_count):
	pos.append(int(input()))                                        # Positions into indices list
for i in range(pets_count):
	anime.append(input())                                           #appending the anime empty list

anime_dictionary = {pos[i]:anime[i] for i in range(pets_count)}   #combining two list into a dictionary

c = 1                                                           #creating a counter varaible to keep check on its position or not
for index, pets in anime_dictionary.items():                    #creating iteration to go through dictionary acc. to condition converting it to lower or upper
	if index != c:
		if index == len(pets):
			anime_dictionary[index] = pets.upper()              #Since pets already in desired position, make it uppercase
		else:
			anime_dictionary[index] = pets.lower()
	c+=1                                                   #increment of flagship varaible
anime_dictionary = dict(sorted(anime_dictionary.items()))           #using sorting function to sort the dictionary acc. to key
print()

for index, pets in anime_dictionary.items():
	print(pets)
print()
