import unittest
import numpy as np
from src.template.fit_line import *

class TestFuncs(unittest.TestCase):

	# def example_test(self):
		# in rough order of usefulness, these are some assert statements!
		# self.assertEqual(A, B) # asserts that floats or ints A, B are equal
		# self.assertNotEqual(A, B) # asserts that floats or ints A, B are not equal
		# self.assertTrue(A) # asserts that A is True
		# self.assertFalse(A) # asserts that A is False
		# self.assertCountEqual(A, B) # asserts that arrays A and B are element-wise equal
		# self.assertIn(A, B) # asserts that A in B
		# self.assertNotIn(A, B) # asserts that A not in B
		# self.assertIs(A, B) # asserts that A is B
		# self.assertIsNot(A, B) # asserts that A is not B
		# self.assertIsInstance(A, B) # asserts that A is an instance of B
		# self.assertNotIsInstance(A, B) # asserts that A is not an instance of B
		# self.assertRaises(A) # asserts that error A is raised

	def test_exponential_e(self):
		x = 0
		a = 1
		b = 1
		c = 0
		result = exp_func(x, a, b, c)
		expected_result = 1
		self.assertEqual(result, expected_result)



# class TestFitting(unittest.TestCase):

	# def test_fit_exponential(self):
		# INSERT CODE HERE