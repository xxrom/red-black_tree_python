# python -m unittest RedBlack_test.py -v
import unittest
from RedBlack import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
  # def test_upper(self):
  #   self.assertEqual('foo'.upper(), 'FOO')

  # def multiply(self):
  #   self.assertEqual(2 * 2, 4)

  def testCase1(self):
    #       5
    #    /    \
    #   3      6
    #    \
    #     4
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6)
    rb.insert(4)
    case1 = [[3, 'black', 5], [4, 'red', 3], [5, 'red', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), case1)

  def testRotateLeft(self):
    #      5B
    #    /    \
    #   3R     6B
    #    \
    #     x4R
    # rotateLeft 3R =>
    #      5B
    #     /   \
    #    x4R   6B
    #   /
    #  3R
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6, 'black')
    rb.insert(4)
    rb.root.leftChild = rb.rotateLeft(rb.root.leftChild)
    out = [[3, 'red', 4], [4, 'red', 5], [5, 'black', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), out)

  def testRotateLeft_RotateRight(self):
    #      5B
    #    /    \
    #   3R     6B
    #    \
    #     x4R
    # rotateLeft 3R =>
    #      5B
    #     /   \
    #    x4R   6B
    #   /
    #  3R
    # rotateRight x4R =>
    #      5B
    #    /    \
    #   3R     6B
    #    \
    #     x4R

    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6, 'black')
    rb.insert(4)
    out = rb.traverse()

    rb.root.leftChild = rb.rotateLeft(rb.root.leftChild)
    rb.root.leftChild = rb.rotateRight(rb.root.leftChild)

    self.assertEqual(rb.traverse(), out)

  def testRotateRightRoot(self):
    #      5B
    #    /    \
    #   3R     6B
    #    \
    #     x4R
    # rotateRight 5B =>
    #      3R
    #         \
    #         5B
    #        /  \
    #      4R    6B

    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6, 'black')
    rb.insert(4)

    rb.root = rb.rotateRight(rb.root)
    out = [[3, 'red', None], [4, 'red', 5], [5, 'black', 3], [6, 'black', 5]]
    print(rb.traverse())
    self.assertEqual(rb.traverse(), out)


if __name__ == '__main__':
    unittest.main()