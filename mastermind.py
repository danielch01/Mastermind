import random

# ----------------
# 	COLOR CODES
# ----------------
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white

choice = []
for _ in range(4):
	choice.append(str(random.randint(1,6)))

print "----------------------------"
print "-- Welcome to Mastermind! --"
print "----------------------------\n\n"

raw_input("Press enter to continue...")
maxTurn = int(raw_input("How many turns do you think you can solve this by: "))
while maxTurn > 12:
	print "Come on, I know it won't take you that long..."
	maxTurn = int(raw_input("Try again: "))
print "Great! Now let's begin..."
raw_input()

turn = 0
game = False
while (game == False):
	if turn == maxTurn:
		print "Sorry, the code was:"
		for i in choice:
			print i
		print "\nBetter luck next time!"
		break
	user_choice = []
	print "Choose numbers from 1 thru 6:\n"
	for _ in range(4):
		user_choice.append(raw_input("no: "))
	r = 0
	w = 0
	for i in range(4):
		if choice[i] in user_choice:
			if user_choice[i] == choice[i]:
				r += 1
			else:
				w += 1
	print "\nRed peg: " + str(r)
	print "White peg: " + str(w) + "\n"
	if (r == 4):
		print "CONGRATS, YOU WON!!!\n\n"
		game = True
	else:
		if turn < (maxTurn-1):
			print "\nSo close! Please try again\n"
	turn  += 1

