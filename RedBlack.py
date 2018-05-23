# node colors
RED = 'red'
BLACK = 'black'

class Node(object):
  def __init__(self, data, parent = None):
    if parent:
      self.color = RED
    else:
      self.color = BLACK
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

  def insert(self, data):
    self.root = self.insertNode(data, self.root, None)

  def insertNode(self, data, node, parent):
    if not node: # если подДерево пустое, то Вернем новую ноду
      print(' * new noda %d ' % data)
      print('')
      return Node(data, parent)

    if node.data < data: # идем в правое подДерево
      print(' >>> ')
      node.rightChild = self.insertNode(data, node.rightChild, node)

      self.validateTree(node.rightChild)
      return node

    elif node.data > data: # идем в левое подДерево
      print(' <<< ')
      node.leftChild = self.insertNode(data, node.leftChild, node)
      self.validateTree(node.leftChild)
      return node

    # прошли вставку ноды и теперь нужно провалидировать подДерево на правила
    return self.validateTree(node)

  # проверка дерева на соответствие правилам
  def validateTree(self, node):

    # case 1 левый правый
    if node.color == RED and node.parent:
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
            self.validateTree(grandPa) # запускаем валидацию от дедушки

    # case 2
    if node.color == RED and node.parent:
      parent = node.parent
      if parent.color == RED and parent.parent and node.parent.parent:
        print(' %d parent => %d => grandPa => %d ' % (node.data, node.parent.data, node.parent.parent.data))
        grandPa = parent.parent
        if grandPa.color == BLACK:
          print('in grandPa')
          grandPaRightChild = grandPa.rightChild
          if parent.color == RED and grandPaRightChild.color == BLACK:
            # перекрасить нужно дедушку и его детей
            print('case 2 !!!')
            newParent = self.turnLeft(parent)
            self.validateTree(newParent) # запускаем валидацию от родителя


    return node

  def turnLeft(self, node):
    tempRight = node.rightChild
    tempRightLeft = tempRight.leftChild

    node.rightChild = tempRightLeft
    tempRight.leftChild = node

    return tempRight

  def turnRight(self, node):
    tempLeft = node.leftChild
    tempLeftRight = tempLeft.rightChild

    node.leftChild = tempLeftRight
    tempLeft.rightChild = node

    return tempLeft

  def traverse(self):
    if self.root:
      return self.traverseInOrder(self.root)
    return []
  ###
  def traverseInOrder(self, node, array = []):
    if node.leftChild:
      array = self.traverseInOrder(node.leftChild, array)

    print(' => %d %s' % (node.data, node.color))
    array.append([node.data, node.color]) # для проверки

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





