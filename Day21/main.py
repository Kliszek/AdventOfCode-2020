ingredients = []
allergens =[]

with open("input.txt", "r") as f:
	for line in f:
		splitted = line.strip(" \n)").split(" (contains ")
		ingredients.append(set(splitted[0].split(" ")))
		allergens.append(splitted[1].split(", "))


all_food = set()
allergens_dict = dict()

for x in range(len(allergens)):
	all_food.update(ingredients[x])
	for alrgn in allergens[x]:
		if not alrgn in allergens_dict:
			allergens_dict[alrgn]=ingredients[x]
		else:
			allergens_dict[alrgn]=allergens_dict[alrgn].intersection(ingredients[x])

list_bad=True
while list_bad:
	list_bad=False
	for entry in allergens_dict:
		if len(allergens_dict[entry]) > 1:
			list_bad=True
		if len(allergens_dict[entry]) == 1:
			for t in allergens_dict:
				if t==entry:
					continue
				allergens_dict[t].discard(*allergens_dict[entry])
		


allergic_food = set()
for entry in allergens_dict:
	allergic_food.update(allergens_dict[entry])

non_allergic_food = all_food - allergic_food

apperance=0
for composition in ingredients:
	for ing in composition:
		if ing in non_allergic_food:
			apperance+=1

print(f"Non allergic food apperance: {apperance}")
print(allergens_dict)


sorted_allergens = list()

for entry in allergens_dict:
	sorted_allergens.append(entry)
sorted_allergens.sort()

print("\nCanonical dangerous ingredient list:")
for alrgn in sorted_allergens:
	print(*allergens_dict[alrgn], end=",")
print("\b ")
