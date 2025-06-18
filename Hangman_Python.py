# Hangman in Python


from Word_list import words

import random 



#dictionaray of key

hangman_art = { 0 : ("   ",
		     "   ",
		     "   ",),
		1 : (" o ",
		     "   ",
		     "   ",),
		2 : (" o ",
		     " | ",
		     "   ",),
		3 : (" o ",
		     "/| ",
		     "   ",),
		4 : (" o ",
		     "/|\\",
		     "   ",),
		5 : (" o ",
		     "/|\\",
		     "/  ",),
		6 : (" o ",
		     "/|\\",
		     "/ \\",)}


# for line in hangman_art[6]:
# 	print(line)


def display_man(wrong_guesses):
	print("**********")
	for line in hangman_art[wrong_guesses]:
		print(line)
	print("**********")


def display_hint(hint):
	print(" ".join(hint))

def display_answer(ans):
	print(" ".join(ans))

def main():
	ans = random.choice(words)
	hint = ["_"] * len(ans)
	wrong_guesses = 0
	guessed_letters = set()
	is_running = True

	while is_running:
		display_man(wrong_guesses)
		display_hint(hint)
		guess = input("Enter a letter: ").lower
	
		if guess in ans :
			for i in range(len(ans)) :
				if ans[i] == guess :					hint[i] = guess





if __name__ == '__main__':
	main()

















