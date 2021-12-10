from math import sqrt
from alphabet import *
import random

class WordGrid:
	def __init__(self, width) -> None:
		self.grid = []
		self.width = width
		self.area = width**2
		self.cheated = False

		# creating the grid array
		for col in range(self.area):
			self.grid.append(get_random_letter())

		self.available_spots = []

		# all the available spots that a letter can be placed
		# True: can be placed
		# False: can not be placed
		for spot in range(self.area):
			self.available_spots.append(True)


	# generates the word grid with words
	# if this method is not called before printing the grid, 
	# it will print just some random letters
	def generate_with_words(self, words):
		# check if there are too much letters

		if self.can_generate(words):
			for word in words:
				finded_place_to_enter_word = False
				while not finded_place_to_enter_word:
					if len(word) > self.width:
						print(f"\nYou entered a word too big for the grid size! (Grid size: {self.width})")
						return

					
					random_direction = random.choice([0, 1]) # 0: horizontal; 1: vertical;

					# random x and y positions of the first letter of the current word
					random_x = random.randint(0, self.width-1)
					random_y = random.randint(0, self.width-1)


					# making sure the word won't go out of bounds
					if random_x + len(word) > self.width and random_direction == 0:
						random_x -= len(word) - self.width
					if random_y + len(word) > self.width and random_direction == 1:
						random_y -= len(word) - self.width

					
					# checking if the word can be placed before placing it
					if self.can_put_word_at(word, random_x, random_y, random_direction):
						self.set_word(word, random_x, random_y, random_direction)
						finded_place_to_enter_word = True

			# when generating finishes, print itself
			self.print()
	
	# sets a word in a position and with a particular direction
	def set_word(self, word, x, y, direction):
		for l in range(len(word)):
			if direction == 0: # horizontal
				# print(f"{l} + {y} * {self.width} = ", l + y * self.width)
				self.grid[l + y * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[l + y * self.width] = False
			else: # vertical
				# print(f"{x} + {l} * {self.width} = ", x + l * self.width)
				self.grid[x + l * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[x + l * self.width] = False
			
	
	# checks if a word can be placed in a position and with a particular direction
	def can_put_word_at(self, word, x, y, direction):
		for l in range(len(word)):
			if direction == 0: # horizontal
				spot_available = self.available_spots[l + y * self.width]
				if spot_available:
					continue
				else: 
					return False

			else: # vertical
				spot_available = self.available_spots[x + l * self.width]
				if spot_available:
					continue
				else: 
					return False
		return True

	def can_generate(self, words):
		letter_count = 0
		for word in words:
			for letter in word:
				letter_count += 1
				if letter_count > self.area:
					print("\nToo many words and little grid!")
					return False
		return True

	# prints the grid on the terminal
	def print(self):

		print("\033[96m" + ("-"*(2*(self.width)-1)) + "\033[0m" ) # just a nice little line
		for y in range(self.width):
			for x in range(self.width):
				print(self.grid[x + y * self.width], end=" ")
			print()
		print("\033[96m" + ("-"*(2*(self.width)-1)) + "\033[0m" )

