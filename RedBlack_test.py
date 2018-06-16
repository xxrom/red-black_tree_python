# python -m unittest RedBlack_test.py -v
import unittest
from RedBlack import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
  # def test_upper(self):
  #   self.assertEqual('foo'.upper(), 'FOO')

  # def multiply(self):
  #   self.assertEqual(2 * 2, 4)

  ##########################################
  # CASE 1
  #      B
  #    /   \
  #   R     R
  #    \
  #     xR
  # recolor grandPa and his children =>
  #     xR
  #    /   \
  #   B     B
  #    \
  #     R
  # test validateTree case 1
  def testCase1_leftTree_rightChild(self):
    #      5B
    #    /    \
    #   3R     6R
    #    \
    #     4R
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6)
    rb.insert(4)
    case1 = [[3, 'black', 5], [4, 'red', 3], [5, 'red', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), case1)

  # test validateTree case 1
  def testCase1_leftTree_leftChild(self):
    #      5B
    #    /    \
    #   3R     6R
    #  /
    # 2R
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6)
    rb.insert(2)
    case1 = [[2, 'red', 3], [3, 'black', 5], [5, 'red', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), case1)

  # test validateTree case 1
  def testCase1_rightTree_rightChild(self):
    #      5B
    #    /    \
    #   3R     6R
    #           \
    #            7R
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(6)
    rb.insert(7)
    case1 = [[3, 'black', 5], [5, 'red', None], [6, 'black', 5], [7, 'red', 6]]
    self.assertEqual(rb.traverse(), case1)

  # test validateTree case 1
  def testCase1_rightTree_leftChild(self):
    #      5B
    #    /    \
    #   3R     R7
    #         /
    #        6R
    rb = RedBlackTree()
    rb.insert(5)
    rb.insert(3)
    rb.insert(7)
    rb.insert(6)
    case1 = [[3, 'black', 5], [5, 'red', None], [6, 'red', 7], [7, 'black', 5]]
    self.assertEqual(rb.traverse(), case1)
  ##########################################

  ##########################################
  # CASE 2
  #      5B
  #    /    \
  #   3R     6B
  #    \
  #     x4R
  # rotateLeft 3R =>
  #        5B
  #       /   \
  #      4R   6B
  #     /
  #    x3R
  # test validateTree case 2
  def testCase2_leftTree_rightChild(self):
    #      5B
    #    /    \
    #   3R     6B
    #    \
    #     4R
    rb = RedBlackTree()
    rb.insertWithoutValidation(5)
    rb.insertWithoutValidation(3)
    rb.insertWithoutValidation(6, 'black')
    rb.insert(4)
    print(rb.traverse())
    case1 = [[3, 'red', 4], [4, 'red', 5], [5, 'black', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), case1)

  def testRotateLeft(self): # test rotate left
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
    rb.insertWithoutValidation(5)
    rb.insertWithoutValidation(3)
    rb.insertWithoutValidation(6, 'black')
    rb.insertWithoutValidation(4)
    rb.root.leftChild = rb.rotateLeft(rb.root.leftChild)
    out = [[3, 'red', 4], [4, 'red', 5], [5, 'black', None], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), out)

  # test rotate left > rotate right = same tree
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
    rb.insertWithoutValidation(5)
    rb.insertWithoutValidation(3)
    rb.insertWithoutValidation(6, 'black')
    rb.insertWithoutValidation(4)
    out = rb.traverse()

    rb.root.leftChild = rb.rotateLeft(rb.root.leftChild)
    rb.root.leftChild = rb.rotateRight(rb.root.leftChild)

    self.assertEqual(rb.traverse(), out)

  # test rotate right in the root
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
    rb.insertWithoutValidation(5)
    rb.insertWithoutValidation(3)
    rb.insertWithoutValidation(6, 'black')
    rb.insertWithoutValidation(4)

    rb.root = rb.rotateRight(rb.root)
    out = [[3, 'red', None], [4, 'red', 5], [5, 'black', 3], [6, 'black', 5]]
    self.assertEqual(rb.traverse(), out)

  # test rotate left in the root
  def testRotateLeftRoot(self):
    #      5B
    #    /    \
    #   3R     7B
    #         /  \
    #      x6R    8B
    # rotateRight 5B =>
    #      7B
    #    /    \
    #   5R     8B
    #  /  \
    # 3R   x6R

    rb = RedBlackTree()
    rb.insertWithoutValidation(5)
    rb.insertWithoutValidation(3)
    rb.insertWithoutValidation(7, 'black')
    rb.insertWithoutValidation(6)
    rb.insertWithoutValidation(8)

    rb.root = rb.rotateLeft(rb.root)
    out = [[3, 'red', 5], [5, 'black', 7], [6, 'red', 5], [7, 'black', None], [8, 'red', 7]]
    self.assertEqual(rb.traverse(), out)

if __name__ == '__main__':
    unittest.main()