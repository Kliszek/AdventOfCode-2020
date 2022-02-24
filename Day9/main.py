numbers = []
with open("input.txt", "r") as f:
	for line in f:
		numbers.append(int(line.strip(" \n")))

def is_sum(index):
	global numbers
	for x in range(index-25,index):
		for y in range(index-25, index):
			if x==y:
				continue
			if numbers[x]+numbers[y]==numbers[index]:
				return True
	return False

wrong_number = 0
for x in range(25, len(numbers)):
	if is_sum(x) == False:
		wrong_number = numbers[x]
		print(f"Number {wrong_number} is wrong!")
		break

worm = numbers[0]
bot = 0
up = 0
while worm != wrong_number:
	if worm < wrong_number:
		up += 1
		worm += numbers[up]
	elif worm > wrong_number:
		worm -= numbers[bot]
		bot += 1

encryption_weakness = min(numbers[x] for x in range(bot,up+1)) + max(numbers[x] for x in range(bot,up+1))

print(f"The encryption weakness is {encryption_weakness}")