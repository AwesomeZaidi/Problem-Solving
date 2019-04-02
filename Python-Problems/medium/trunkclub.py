# Instructions / Question:
# 	Given a standard English sentence passed in as a string,
#  	write a method that will return a sentence comprised of the same words,
#  	but sorted by their first letter.

#  	However, the method of sorting has a twist to it:
#  	all words that begin with a lowercase letter should be
#  	at the beginning of the sorted sentence,
#  	and sorted in ascending order. All words that begin with
#  	an uppercase letter should come after that, and should be sorted
#  	in descending order. If a word appears twice in the sentence,
#  	it should be returned twice in the sorted sentence.

#  	Any punctuation must be discarded.

#  	Sample Run:

#    	Input: `A Person who never Made a Mistake never tried anything New.`

#    	Output `a anything never never tried who Person New Mistake Made A`

def caseSwap(sentence):
	'''
		Args: 		sentence: string sentence
		Returns: 	sorted_sentence: string with lowercase words first
					and uppercased words in decending alphabetized order
					and lowercase words in alphabetized order.

		n = number of words in input sentence (length of word_list)
		Time Complexity: 2n + 2 (n*log n) + 2n = O(n*log n) overall
	'''

	word_list = sentence.split() # O(n)

	lowercases = []
	uppercases = []
	for word in word_list: # n iterations x O(1) = O(n)
		if word[0].islower(): # O(1)
			lowercases.append(word) # O(1)
		else:
			uppercases.append(word) # O(1)

	lowercases = sorted(lowercases) # approximately n/2 log n/2 = O(n*log n)
	uppercases = sorted(uppercases, reverse=True) # also O(n*log n)
	sorted_sentence = ' '.join(lowercases) + ' ' # approximately n/2 = O(n)
	sorted_sentence += ' '.join(uppercases) # approximately n/2 = O(n)
	return sorted_sentence

print(caseSwap('A Person who never Made a Mistake never tried anything New'))

# Expected output: `a anything never never tried who Person New Mistake Made A`
