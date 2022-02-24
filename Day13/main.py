timestamp = 0
busses = []

with open("input.txt", "r") as f:
	timestamp = int(f.readline())
	my_list = f.readline().strip(" \n").split(",")
	busses = [(int(my_list[x]),x) for x in range(len(my_list)) if my_list[x] != "x"]

min_time = 100000
min_id = 0

for bus_id in busses:
	wait_time = bus_id[0] - (timestamp % bus_id[0])
	if min_time > wait_time:
		min_time = wait_time
		min_id = bus_id[0]

print(f"ID = {min_id}")
print(f"Time = {min_time}")
print(f"ID * time = {min_id*min_time}")



def number_with_modulus(numbers, modulus):
	""""Return a number which divided by specified numbers, gives specified remainders."""
	if len(numbers) == 2:
		if modulus[0]>modulus[1]:
			return number_with_modulus([numbers[1],numbers[0]],[modulus[1],modulus[0]])
		d = modulus[1]-modulus[0]
		mod=numbers[0]%numbers[1]
		mul=1
		while (mul*mod)%numbers[1]!=d:
			mul+=1
		return numbers[0]*mul+modulus[0]

	new_numbers = list()
	new_modulus = list()
	for x in range(1,len(numbers)):
		new_numbers.append(numbers[x])
		t=number_with_modulus([numbers[0], numbers[x]], [modulus[0], modulus[x]])
		t//=numbers[0]
		new_modulus.append(t)
	return number_with_modulus(new_numbers,new_modulus)*numbers[0]+modulus[0]

print("\n\n")
print(f"UWAGAAAA: {number_with_modulus([1789,37,47,1889],[0,36,45,1886])}")

final_nums = [x[0] for x in busses]
final_mods = [x[0]-x[1]%x[0] for x in busses]
final_mods[0] = 0

print(final_nums)
print(final_mods)

result = number_with_modulus(final_nums, final_mods)

print(f"THE AWAITED RESULT IS: {result}")