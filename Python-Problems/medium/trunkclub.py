# Question:

#  Given a standard English sentence passed in as a string,
#  write a method that will return a sentence comprised of the same words,
#  but sorted by their first letter.

#  However, the method of sorting has a twist to it:
#  all words that begin with a lowercase letter should be
#  at the beginning of the sorted sentence,
#  and sorted in ascending order. All words that begin with
#  an uppercase letter should come after that, and should be sorted
#  in descending order. If a word appears twice in the sentence,
#  it should be returned twice in the sorted sentence.

#  Any punctuation must be discarded.

#  Sample Run:

#    Input: `A Person who never Made a Mistake never tried anything New.`

#    Output `a anything never never tried who Person New Mistake Made A`

# # assumptions 

# # clarifications
# 1. create a function 
# 2. arguments 1 of str
# 3. returns str -> sorted
# 4. lowercase first ascending order...
# 5. uppercasse last in decending order
# 6. continue to add all words even if doubled

def caseSwap(sentence):
	'''
		Args: 		sentence: string sentence
		Returns: 	sentence: string with lowercase words first
					and in decending alphabetized order.
	'''
	sentence = sentence.split() # Convert string to list to work with.
	# OLD COOOODEAH
		# sentence = sorted(sentence, reverse=True) # sort the list in reverse, lowercases come first.
		
		# loop through the list and if a word is lower case

		# for index, word in enumerate(sentence):
		# 	if word.islower()
		# 	if word < nextWord:
		# 		sentence.insert(index, sentence.pop(index+1))
		# 	else:
		# 		sentence.insert(index+1, sentence.pop(index))
		# 	return sentence

			# and word < currentWord:
			# 	sentence.insert(index, sentence.pop(index))

	lowercases = []
	uppercases = []
	for word in sentence:
	# throw all the lowercase words into a list, sort it.
		if word.islower():
			lowercases.append(word)
		# throw all the uppercase words into a list, sort that.
		else:
			uppercases.append(word)

	# concatenate the list together and convert to a string to be returned.
	lowercases = sorted(lowercases) # sort the list in reverse, lowercases come first.
	uppercases = sorted(uppercases, reverse=True) # sort the list in reverse, lowercases come first.
	sortedSentence = ' '.join(lowercases + uppercases)
	return sortedSentence

print(caseSwap('A Person who never Made a Mistake never tried anything New.'))

# Expected output: `a anything never never tried who Person New Mistake Made A`