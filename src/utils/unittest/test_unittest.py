import unittest

def add(a, b):
	return a+b

def minus(a, b):
	return a-b

class TestMathFunc(unittest.TestCase):
	
	def test_add(self):
		self.assertEqual(add(1, 2), 3)
		self.assertNotEqual(add(1, 2), 4)

	def test_minus(self):
		self.assertEqual(minus(1, 2), -1)
		self.assertNotEqual(minus(1, 2), 1)

if __name__ == '__main__':
	unittest.main(verbosity=2)
		
