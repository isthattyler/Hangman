import random

class HangMan():
	def __init__(self):
		self.file = "data/wordlist.txt"
		self._start()
	
	def _start(self):
		maxTrial = 10
		randWord, sol = self.printStart(maxTrial)
		maxTrial = self.play(randWord, maxTrial, sol)
		self.printEnd(maxTrial, randWord)
		

	def printStart(self, trial):
		name = input("Welcome to Hangman Game. Your name is: ") #take the name from user
		print("\n")
		print(name + ", you have " + str(trial) + " tries to guess the word I am thinking")
		wordList = self.loadFile()
		randWord = self.pickWord(wordList)
		print("I'm thinking of a word with length of " + str(len(randWord)) +"\n")
		sol = self.updateWord(randWord)
		print(sol)
		return randWord, sol

	def printEnd(self, trial, word):
		if trial:
				print("\nWow you're amazing!")
		else:
			print("\nAwww maybe next time!")
		print("The word is: " + word)

	def play(self, word, trial, sol):
		while trial:
			old_sol = sol
			print("You have " + str(trial) + " guesses left")
			letter = input("Your guess: ")
			sol = self.updateWord(word,letter, sol)
			if sol == old_sol:
				print("\nYou got it wrong!")
			else:
				print("\nYou got it right!")
			print(sol)
			trial -= 1
			if "_" not in sol:
				break
		return trial

	def loadFile(self):
		filelst = open(self.file, 'r')
		words_list = [line.rstrip() for line in filelst]	# Read each line
		return words_list

	def pickWord(self, word_list):
		return random.choice(word_list)
	
	def updateWord(self, word, letter=None, sol=None):	# Update the display word for user
		new_word = ""

		if not letter and not sol:
			for i in range(len(word)):
				new_word+="_"
		else:
			if letter == word:
				new_word = letter
				return new_word

			for i in range(len(word)):
				lett = word[i]
				if lett == letter:
					new_word += lett
				else:
					new_word += sol[i]

		return new_word

hangman = HangMan()