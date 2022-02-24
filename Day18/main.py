equations = []

with open("input.txt", "r") as f:
	for line in f:
		equations.append(line.strip(" \n"))

def find_closing_bracket(eq, ind):
	balance=0
	for i in range(ind,len(eq)):
		if eq[i] == "(":
			balance+=1
		if eq[i] == ")":
			balance-=1
		if balance == 0:
			return i
	return None


def find_opening_bracket(eq, ind):
	balance=0
	for i in range(ind,-1,-1):
		if eq[i] == "(":
			balance+=1
		if eq[i] == ")":
			balance-=1
		if balance == 0:
			return i
	return None


def solve_equation(eq):
	operation = "+"
	res = 0
	ind = 0
	while ind < len(eq):
		ch = eq[ind]
		if ch == " ":
			ind+=1
			continue

		elif ch == "+":
			operation = "+"
			ind+=1
			continue
		elif ch == "*":
			operation = "*"
			ind+=1
			continue
		elif ch == "(":
			closing_bracket = find_closing_bracket(eq,ind)
			if operation=="+":
				res+=solve_equation(eq[ind+1:closing_bracket])
			elif operation=="*":
				res*=solve_equation(eq[ind+1:closing_bracket])
			ind = closing_bracket+1
			continue
		else:
			if operation=="+":
				res+=int(ch)
			elif operation=="*":
				res*=int(ch)
			ind+=1
			continue
		
		print(f"WHAT CHAR IS THAT? {ch}")
	return res

def add_brackets(eq, start=0):
	new_eq = ""
	ind = start
	while ind<len(eq):
		if eq[ind] == "+":
			opening_bracket = -1
			closing_bracket = -1
			if eq[ind-2] == ")":
				opening_bracket = find_opening_bracket(eq,ind-2)
				new_eq += eq[0:opening_bracket]
				new_eq += "("
				new_eq += eq[opening_bracket:ind]
			else:
				new_eq += eq[0:ind-2]
				new_eq += "("
				new_eq += eq[ind-2:ind]
			
			new_eq += "+"

			if eq[ind+2] == "(":
				closing_bracket = find_closing_bracket(eq,ind+2)
				new_eq += eq[ind+1:closing_bracket]
				new_eq += ")"
				new_eq += eq[closing_bracket:]
			else:
				new_eq += eq[ind+1:ind+3]
				new_eq += ")"
				new_eq += eq[ind+3:]
			return add_brackets(new_eq,ind+2)
		ind+=1

	return eq		


res = 0
for eq in equations:
	res += solve_equation(eq)
print(f"The result is: {res}")

res_adv = 0
for eq in equations:
	res_adv += solve_equation(add_brackets(eq))
print(f"The advenced result is: {res_adv}")