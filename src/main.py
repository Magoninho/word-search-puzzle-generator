from word_grid import *
import argparse


# Initialize parser
parser = argparse.ArgumentParser(description="Generates a word search puzzle")

# Adding optional argument
parser.add_argument("-c", "--cheated", action="store_true", help = "Hightlight words")
parser.add_argument("-f", "--file", type=str, default="words.txt", help = "Path to a custom words file. One word per line.")

# Read arguments from command line
args = parser.parse_args()

def main(cheated=False, words_file=None):
	words = []
	file1 = open(words_file, 'r')
	lines = file1.readlines()
	file1.close()

	for _ in range(6):
		words.append(lines[random.randint(0, len(lines)-1)].strip())

	grid = WordGrid(20)
	print("┌────────────────────┐")
	print("│ Word Search Puzzle │")
	print("└────────────────────┘")

	grid.cheated = cheated
	grid.generate_with_words(words)

	# printing the words to find
	print("Words:")
	count = 0
	for word in words:
		count += 1
		print(f"{count}. {word}", end=" | ")
	print()

if __name__ == "__main__":
	main(cheated=args.cheated, words_file=args.file)

# Created by Magoninho