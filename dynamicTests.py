import unittest
import numpy
from dynamicProgramming import binHandler, commonSubSeq, editDistance

class TestFunctions(unittest.TestCase):

	#tests LCS correctness
	def test_LCS(self):
		word1 = 'aaaa0'
		word2 = 'aaba0'
		lcs = numpy.zeros((len(word1), len(word2)))
		subseq_len = commonSubSeq(word1, word2, lcs)
		self.assertTrue(subseq_len == 3)

	def test_LCS_None(self):
		word1 = None
		word2 = None
		lcs = None
		subseq_len = commonSubSeq(word1, word2, lcs)
		self.assertTrue(subseq_len == -1)

	def test_common_subseq(self):
		word1 = 'sunny'
		word2 = 'sunny'
		edits = numpy.zeros((len(word1), len(word2)))

		edit_distance = editDistance(word1, word2, edits)
		self.assertTrue(edit_distance == 0)

	def test_common_subseq_2(self):
		word1 = 'sunny'
		word2 = 'snowy'
		edits = numpy.zeros((len(word1), len(word2)))

		edit_distance = editDistance(word1, word2, edits)
		self.assertTrue(edit_distance == 3)

		"""
	def test_binHandler(self):
		m = [0,0,0,0,0, 5, 6, 10, 11, 12]
		p = [0,0,0,0,2, 7, 3, 3, 9, 10]
		s = []
		k = 4
		test = binHandler(m, p, s, k)
		self.assertTrue(s[0] == 28)

		"""
		
	def test_binHandler_None(self):
		m = None
		p = None
		s = []
		k = 4
		test = binHandler(m, p, s, k)
		self.assertTrue(test == -1)


def main():
	unittest.main()

if __name__ == '__main__':
	main()