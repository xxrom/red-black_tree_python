# node colors
RED = 'red'
BLACK = 'black'

class Node(object):
  def __init__(self, data, parent = None, color = RED):
    self.color = color
    self.data = data
    self.leftChild = None
    self.rightChild = None
    self.parent = parent

  def changeColor(self):
    if self.color == RED:
      self.color = BLACK
    else:
      self.color = RED
    print(' in changeColor %s ' % self.color)

# node = Node(12)

# print(' color %s ' % node.color)
# node.changeColor()
# print(' color %s ' % node.color)

class RedBlackTree(object):

  def __init__(self):
    self.root = None

  def insert(self, data, color = RED):
    self.root = self.insertNode(data, self.root, None, color)

  def insertNode(self, data, node, parent, color):
    if not node: # если подДерево пустое, то Вернем новую ноду
      # print(' * new node %d %s' % (data, color))
      print('')
      if parent:
        return Node(data, parent, color)
      else:
        return Node(data, parent, BLACK) # корень дерева BLACK

    if node.data < data: # идем в правое подДерево
      # print(' >>> ')
      node.rightChild = self.insertNode(data, node.rightChild, node, color)

      self.validateTree(node.rightChild)
      return node

    elif node.data > data: # идем в левое подДерево
      # print(' <<< ')
      node.leftChild = self.insertNode(data, node.leftChild, node, color)
      self.validateTree(node.leftChild)
      return node

    # прошли вставку ноды и теперь нужно провалидировать подДерево на правила
    return self.validateTree(node)

  # проверка дерева на соответствие правилам
  def validateTree(self, node):

    # case 1 левый правый
    if node.color == RED and node.parent:
      #      B
      #    /   \
      #   R     R
      #    \
      #     xR
      # recolor grendPa and his childs =>
      #     xR
      #    /   \
      #   B     B
      #    \
      #     R
      parent = node.parent
      if parent.color == RED and parent.parent and node.parent.parent:
        print(' %d parent => %d => grandPa => %d ' % (node.data, node.parent.data, node.parent.parent.data))
        grandPa = parent.parent
        if grandPa.color == BLACK:
          print('in grandPa')
          grandPaLeftChild = grandPa.leftChild
          grandPaRightChild = grandPa.rightChild
          if grandPaLeftChild.color == RED and grandPaRightChild.color == RED:
            # перекрасить нужно дедушку и его детей
            print('case 1 !!!')
            grandPa.changeColor()
            grandPaLeftChild.changeColor()
            grandPaRightChild.changeColor()
            return self.validateTree(grandPa) # запускаем валидацию от дедушки

    # case 2
    if node.color == RED and node.parent:
      #      5B
      #    /    \
      #   3R     6B
      #    \
      #     x4R
      # rotateLeft 3R =>
      #        5B
      #       /   \
      #      x4R   6B
      #     /
      #    3R
      parent = node.parent
      # if parent.color == RED and parent.parent and node.parent.parent:
      #   print(' %d parent => %d => grandPa => %d ' % (node.data, node.parent.data, node.parent.parent.data))
      #   grandPa = parent.parent
      #   if grandPa.color == BLACK:
      #     print('in grandPa')
      #     grandPaRightChild = grandPa.rightChild
      #     if parent.color == RED and grandPaRightChild.color == BLACK:
      #       # повернуть налево отца и вернуть его обратно
      #       print('case 2 !!! %d' % parent.data)
      #       if parent.leftChild.data == node.data:
      #         print('rotateLeft')
      #         grandPa.leftChild = self.rotateLeft(parent)
      #         return self.validateTree(grandPa.leftChild) # запускаем валидацию от родителя
      #       if parent.rightChild.data == node.data:
      #         print('rotateRight')
      #         grandPa.leftChild = self.rotateRight(parent)
      #         return self.validateTree(grandPa.leftChild) # запускаем валидацию от родителя


    return node

  def rotateLeft(self, node):
    tempRight = node.rightChild
    tempRightLeft = tempRight.leftChild

    tempRight.leftChild = node
    node.rightChild = tempRightLeft

    # переприсваиваем родителей
    tempRight.parent = node.parent
    node.parent = tempRight
    if node.rightChild and node.rightChild.parent:
      node.rightChild.parent = node

    return tempRight

  def rotateRight(self, node):
    tempLeft = node.leftChild
    tempLeftRight = tempLeft.rightChild

    tempLeft.rightChild = node
    node.leftChild = tempLeftRight

    # переприсваиваем родителей
    tempLeft.parent = node.parent
    node.parent = tempLeft

    if node.leftChild and node.leftChild.parent:
      node.leftChild.parent = node

    return tempLeft

  def traverse(self):
    if self.root:
      return self.traverseInOrder(self.root, [])
    return []
  ###
  def traverseInOrder(self, node, array):
    if node.leftChild:
      array = self.traverseInOrder(node.leftChild, array)

    parentData = None
    if node.parent:
      parentData = node.parent.data
    print(' => %d|%s /up %s' % (node.data, node.color, parentData))
    array.append([node.data, node.color, parentData]) # для проверки

    if node.rightChild:
      array = self.traverseInOrder(node.rightChild, array)

    return array


# rb = RedBlackTree()
# rb.insert(5)
# rb.insert(3)
# rb.insert(6)
# rb.insert(4)
# #       5
# #    /    \
# #   3      6
# #    \
# #     4
# print(rb.traverse())
# case1 = [[3, 'black'], [4, 'red'], [5, 'red'], [6, 'black']]
# assertEqual(rb.traverse(), case1)

# import sys
# sys.stdout.write('.')
# sys.stdout.write(' ,,,, \n')
# print(' ,,,,', end='')
# print(' ,,,,', end='', flush=True)





