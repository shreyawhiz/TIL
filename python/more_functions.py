def break_words(stuff):
	print """This function will break up words for us"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print word

def print_last_word(words):
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words);

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = break_words(sentence)
	sorted_w = sort_words(words)
	print_first_word(sorted_w)
	print_last_word(sorted_w) 