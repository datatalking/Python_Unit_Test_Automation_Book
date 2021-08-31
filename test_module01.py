import unittest


class MyTestCase(unittest.TestCase):
	def test_something_equal1(self):
		self.assertEqual(False, False)  # add assertion here
	
	def test_something_equal2(self):
		self.assertEqual(True, True)  # add assertion here
	
	def test_something_not_equal1(self):
		self.assertNotEqual(True, False)  # add assertion here

	def test_something_not_equal3(self):
		self.assertNotEqual(False, True)  # add assertion here

class TestClass01(unittest.TestCase):
	
	def test_case01(self):
		my_str = "ASHWIN"
		my_int = 999
		self.assertTrue(isinstance(my_str, str))
		self.assertTrue(isinstance(my_int, int))
	
	def test_case02(self):
		my_pi = 3.14
		self.assertFalse(isinstance(my_pi, int))
		self.assertTrue(isinstance(my_pi, float))

if __name__ == '__main__':
	unittest.main()
