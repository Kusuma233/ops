import unittest

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(60, 30), 90)

  def test_subtract(self):
    self.assertEqual(subtract(30, 10), 20)

  def test_multiply(self):
    self.assertEqual(multiply(5, 4), 20)

  if __name__ == "__main__":

    print("Student Calculator Application")
    print("Addition:", add(60,30))
    print("Subtraction:",subtract(30,10))
    print("Multiplication:",multiply(5,4))

    print("\nExecuting Automated tests...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit = False)
