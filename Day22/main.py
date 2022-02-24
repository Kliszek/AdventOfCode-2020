def load_decks(p1,p2):
	with open("input.txt", "r") as f:
		for line in f:
			if line.strip(" \n") == "Player 1:":
				current = p1
				continue
			elif line.strip(" \n") == "Player 2:":
				current = p2
				continue
			elif line.strip(" \n") == "":
				continue
			else:
				current.append(int(line.strip(" \n")))

def calculate_score(player):
	points = 0
	multiplier = len(player)
	for card in player:
		points+=card*multiplier
		multiplier-=1
	return points

def combat_round(p1, p2):
	if p1[0] > p2[0]:
		p1.extend([p1[0],p2[0]])
	else:
		p2.extend([p2[0],p1[0]])
	del p1[0]
	del p2[0]

#game=0
def recursive_combat(p1,p2):
	#global game
	#game+=1
	#game_loc = game
	p1_history = set()
	p2_history = set()

	#round_no=0
	while len(p1)>0 and len(p2)>0:
		#round_no+=1
		#print(f"-- Round {round_no} (Game {game_loc}) --")
		#print(f"Player 1's deck: {p1}")
		#print(f"Player 2's deck: {p2}\n")
		if tuple(p1) in p1_history or tuple(p2) in p2_history:
			return p1
		p1_history.add(tuple(p1))
		p2_history.add(tuple(p2))
		
		if len(p1)-1>=p1[0] and len(p2)-1>=p2[0]:
			p1_new_deck = []
			p2_new_deck = []
			for x in range(p1[0]):
				p1_new_deck.append(p1[1+x])
			for x in range(p2[0]):
				p2_new_deck.append(p2[1+x])
			winner=recursive_combat(p1_new_deck, p2_new_deck)

			if winner==p1_new_deck:
				p1.extend([p1[0],p2[0]])
			else:
				p2.extend([p2[0],p1[0]])
			del p1[0]
			del p2[0]

		else:
			combat_round(p1,p2)
	if len(p1)==0:
		return p2
	else:
		return p1


player1 = []
player2 = []
load_decks(player1, player2)

while len(player1)>0 and len(player2)>0:
	combat_round(player1, player2)

if len(player1)==0:
	winner = player2
else:
	winner = player1

print(f"Winner's points: {calculate_score(winner)}")

player1 = []
player2 = []
load_decks(player1, player2)
winner = recursive_combat(player1, player2)


print(f"Recursive winner's points: {calculate_score(winner)}")
