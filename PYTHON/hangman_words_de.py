# Parameters
filename = "hangman_word_de_list.txt"
mode = "r"

# Code
file = open(filename, mode)

lines = file.read()
words = list(map(str, lines.split()))


file.close()
