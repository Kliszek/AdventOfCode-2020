def bin_to_dec(number):
	res = 0
	i = len(number)-1
	for x in number:
		if x == "1":
			res += (2**i)
		i-=1
	return res

def dec_to_bin(number):
	res = ""
	while number != 0:
		if number % 2 == 1:
			res = "1"+res
		else:
			res = "0"+res
		number//=2
	return ("0"*(36-len(res)))+res

def use_mask(number, mask):
	res = ""
	for x in range(len(mask)):
		if mask[x] == "0":
			res += number[x]
		else:
			res += mask[x]
	return res

def floating(number):
	res = []
	if number.count("X") == 0:
		return [bin_to_dec(number)]
	else:
		ind = number.index("X")
		str_lst = list(number)
		str_lst[ind] = "0"
		res.extend(floating("".join(str_lst)))
		str_lst[ind] = "1"
		res.extend(floating("".join(str_lst)))
		return res



memory = dict()
mask = ""
with open("input.txt", "r") as f:
	for line in f:
		data = line.strip(" \n").split(" = ")
		if data[0] == "mask":
			mask = data[1]
		else:
			n = int(data[0][ 4 : data[0].index("]") ])
			n = dec_to_bin(n)
			n = use_mask(n, mask)
			mem_list = floating(n)
			for x in mem_list:
				memory[x] = int(data[1])


mem_sum = 0
for entry in memory:
	mem_sum += memory[entry]
	
print(f"The sum is: {mem_sum}")