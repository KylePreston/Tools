class Levenshtein(object):
	"""Class that will utilize the Levenshtein distance"""

	def find_ldist(self, user_word, txt_word):
		"""Finds the Levenshtein distance between user_word and txt_word. """

		i, j = len(user_word), len(txt_word)
		if i > j:
			user_word, txt_word = txt_word, user_word
			i, j = j, i

		current = range(i+1)
		for x in range(1, j+1):
			prior, current = current, [x] + [0]*i

			for y in range(1, i+1):
				add, erase = prior[y] + 1, current[y-1] + 1
				change = prior[y-1]

				if user_word[y-1] != txt_word[x-1]:
					change += 1

				current[y] = min(add, erase, change)

		return current[i]
