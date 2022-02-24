rules = dict()
messages = list()

with open("input.txt", "r") as f:
	for line in f:
		if line.strip(" \n") == "":
			break
		key = int(line.strip(" \n").split(": ")[0])
		t = line.strip(" \n").split(": ")[1]
		if t=="\"a\"":
			rules[key] = "a"
		elif t=="\"b\"":
			rules[key] = "b"
		
		else:
			rules[key] = [[int(x) for x in y.split(" ")] for y in t.split(" | ")]
	for line in f:
		messages.append(line.strip(" \n"))

rules[8] = [[42],[42,8]]
rules[11] = [[42,31],[42,11,31]]


def generate_all(rule, lst):
	if rules[rule] == "a" or rules[rule] == "b":
		for x in range(len(lst)):
			lst[x]+=rules[rule]
		return
	else:
		nested = []
		for x in rules[rule]:
			nes = [""]
			for r in x:
				generate_all(r,nes)
			nested.extend(nes)
		
		d = len(lst)
		lst*=len(nested)
		for x in range(len(lst)):
			lst[x]+=nested[x//d]

def is_rule_fulfilled(rule, word):
	#print(f"check rule {rule}, word: {word}")
	if len(word) < 1:
		return []
	if rules[rule] == "a":
		if word[0]=="a":
			return [1]
		else:
			return []
	if rules[rule] == "b":
		if word[0]=="b":
			return [1]
		else:
			return []
	
	all_sol=[]
	for alternative in rules[rule]:
		ind=[0]
		for r in alternative:
			#print(f"going to rule {r} in rule {rule}")
			res = []

			x=0
			while x<len(ind):
				t = is_rule_fulfilled(r, word[ind[x]:])
				if len(t)==0:
					del ind[x]
				else:
					res.append(t)
					x+=1

			if res==[]:
				#print(f"going to alternative of rule {rule}")

				break
			else:
				#print(f"ind: {ind}\nres: {res}\n")
				#print(f"did {r} in rule {rule}")
				d=len(ind)
				for x in range(d):
					#ind[x]+=res[x][0]
					for y in range(1,len(res[x])):
						ind.append(ind[x]+res[x][y])
					ind[x]+=res[x][0]
				#print(f"ind: {ind}\n\n")

		else:
			#print(f"One alternative of rule {rule} was successful")
			all_sol.extend(ind)
		#print("broken")
	#print(f"rule {rule} was bad")
	return all_sol

generated = [""]
#generate_all(0,generated)

#print("zrobione")
#print(generated)
#print("\n\n")

res = 0
for x in messages:
	if x in generated:
		res+=1
#print(f"Messages that matches: {res}")

#RES = is_rule_fulfilled(0, messages[2])
#print(isinstance(RES,bool))
#print(bool(RES))
#print(RES)


res = 0
for x in messages:
	t = is_rule_fulfilled(0, x)
	#print(t)
	if len(x) in t:
		res+=1
		#print(x)
		

print(f"Correct messages: {res}")
print(f"/{len(messages)}")
#g=[""]



#generate_all(0,g)
#print(f"\n\n{g}")