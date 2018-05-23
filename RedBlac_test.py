import unittest
from RedBlack import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
  def test_upper(self):
    self.assertEqual('foo'.upper(), 'FOO')

  def testCase1(self):
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6)
    rb.insert(4)
    case1 = [[3, 'black'], [4, 'red'], [5, 'red'], [6, 'black']]
    self.assertEqual(rb.traverse(), case1)


if __name__ == '__main__':
    unittest.main()