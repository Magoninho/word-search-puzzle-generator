from math import sqrt
from alphabet import *
import random

HORIZONTAL 	= 0
VERTICAL	= 1

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
			self.available_spots.append(True) # all spots are available at the beginning


	# generates the word grid with words
	# if this method is not called before printing the grid, 
	# it will print just some random letters
	def generate_with_words(self, words):
		# check if there are too much letters
		if self.can_generate(words):
			for word in words:
				finded_place_to_enter_word = False
				while not finded_place_to_enter_word:

					# chooses a random direction
					random_direction = random.choice([HORIZONTAL, VERTICAL])

					# random x and y positions of the first letter of the current word
					random_x = random.randint(0, self.width-1)
					random_y = random.randint(0, self.width-1)


					# making sure the word won't go out of bounds
					if random_x + len(word) > self.width and random_direction == HORIZONTAL:
						random_x -= (random_x + len(word)) - self.width
					if random_y + len(word) > self.width and random_direction == VERTICAL:
						random_y -= (random_y + len(word)) - self.width
					
					
					# checking if the word can be placed before placing it
					if self.is_placeable(word, random_x, random_y, random_direction):
						self.place_word(word, random_x, random_y, random_direction)
						finded_place_to_enter_word = True
					

			# when generating finishes, print itself
			self.print()
	
	# sets a word in a position and with a particular direction
	def place_word(self, word, x, y, direction):
		# for every letter on the word
		for l in range(len(word)):
			if direction == HORIZONTAL:
				# place horizontally
				self.grid[x+l + y * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[x+l + y * self.width] = False # making the horizontal spot unavaliable
			elif direction == VERTICAL:
				# place vertically
				self.grid[x + (y+l) * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[x + (y+l) * self.width] = False # making the vertical spot unavaliable
			
	
	# checks if a word can be placed in a position and with a particular direction
	def is_placeable(self, word, x, y, direction):
		# for every letter on the word
		for l in range(len(word)):
			spot_available = self.available_spots[x+l + y * self.width] if direction == HORIZONTAL else self.available_spots[x + (y+l) * self.width]

			# if the spot is available, then continue checking
			if spot_available:
				continue
			# if a spot is unavaliable, then is not placeable, returns false 
			else: 
				return False
		# if the loop finishes without returning false, it means that is placeable, returns true
		return True

	def can_generate(self, words):
		letter_count = 0
		for word in words:
			for letter in word:
				letter_count += 1
				# if there are much more letters than the grid area
				if letter_count > self.area:
					print("\nToo many words for a little grid!")
					return False
			if len(word) > self.width:
				print(f"\nYou entered a word too big for the grid size! (Grid size: {self.width})")
				return False
		return True

	# prints the grid on the terminal
	def print(self):

		print("\033[96m┌" + ("─"*(2*(self.width)+1)) + "┐\033[0m" ) # just a nice little line
		for y in range(self.width):
			print("\033[96m│\033[0m", end=" ")
			for x in range(self.width):
				print(self.grid[x + y * self.width], end=" ")
			print("\033[96m│\033[0m")
		print("\033[96m└" + ("─"*(2*(self.width)+1)) + "┘\033[0m" )

