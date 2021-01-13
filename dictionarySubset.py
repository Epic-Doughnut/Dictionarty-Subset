from english_words import english_words_lower_set
import sys

if len(sys.argv) == 1:
	print('You must include a list of letters to include!\nFormat: <include> [exclude]')
	exit()

# include words with every letter from include, exlcude words with any letter in exclude
include = sys.argv[1]

if len(sys.argv) > 2:
	exclude = sys.argv[2]
else:
	exclude = ''

for word in english_words_lower_set:
	if all([ele in word for ele in include]) and not any([ele in word for ele in exclude]):
		print(word)
