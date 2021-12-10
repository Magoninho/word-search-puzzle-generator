from word_grid import *

words = []

file1 = open('words.txt', 'r')
lines = file1.readlines()
file1.close()

for _ in range(8):
    words.append(lines[random.randint(0, len(lines)-1)].strip())

grid = WordGrid(20)
print("┌────────────────────┐")
print("│ Word Search Puzzle │")
print("└────────────────────┘")


grid.generate_with_words(words)

# printing the words to find
print("Words:")
count = 0
for word in words:
	count += 1
	print(f"{count}. {word}", end=" | ")
print()


# Created by Magoninho