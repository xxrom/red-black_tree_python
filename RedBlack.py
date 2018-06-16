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
    self.root = self.insertNode(data, self.root, None, color, True)

  def insertWithoutValidation(self, data, color = RED):
    self.root = self.insertNode(data, self.root, None, color, False)

  def insertNode(self, data, node, parent, color, validate):
    if not node: # если подДерево пустое, то Вернем новую ноду
      # print(' * new node %d %s' % (data, color))
      if parent:
        return Node(data, parent, color)
      else:
        return Node(data, parent, BLACK) # корень дерева BLACK

    if node.data < data: # идем в правое подДерево
      # print(' >>> ')
      node.rightChild = self.insertNode(data, node.rightChild, node, color, validate)

      if validate:
        self.validateTree(node.rightChild)
      return node

    elif node.data > data: # идем в левое подДерево
      # print(' <<< ')
      node.leftChild = self.insertNode(data, node.leftChild, node, color, validate)
      if validate:
        self.validateTree(node.leftChild)
      return node

    # прошли вставку ноды и теперь нужно провалидировать подДерево на правила
    if validate:
      return self.validateTree(node)
    return node

  # проверка дерева на соответствие правилам
  def validateTree(self, node):

    # case 1 левый правый
    if node.color == RED and node.parent:
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
      parent = node.parent
      if (
        parent.color == RED
        and parent.parent and node.parent.parent
        and node.parent.parent.color == BLACK
        and node.parent.parent.leftChild and node.parent.parent.leftChild.color == RED
        and node.parent.parent.rightChild and node.parent.parent.rightChild.color == RED
      ):
        print('case 1 !!!')
        print(' %d parent => %d => grandPa => %d ' % (node.data, node.parent.data, node.parent.parent.data))
        grandPa = parent.parent

        # перекрасить нужно дедушку и его детей
        grandPa.changeColor()
        grandPa.leftChild.changeColor()
        grandPa.rightChild.changeColor()

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
      #      4R   6B
      #     /
      #    x3R
      parent = node.parent

      # вот тут проверяем для левого поддерева!
      # TODO: сделать для grandPa.leftChild
      if (
        parent.color == RED
        and parent.rightChild and parent.rightChild == node # node in parent.right
        and parent.parent and parent.parent.color == BLACK # grandPa
        and parent.parent.rightChild and parent.parent.rightChild.color == BLACK # rightChild GrandPa
        and parent.parent.leftChild == parent # leftChild GrandPa
      ):
        print('CASE 2 / left subTree / in grandPa')
        print(' %d parent => %d => grandPa => %d ' % (node.data, parent.data, parent.parent.data))
        grandPa = parent.parent

        # повернуть налево отца и вернуть его обратно
        print('rotateLeft')
        grandPa.leftChild = self.rotateLeft(node.parent)

        print('grandPa.leftChild.leftChild %d' % grandPa.leftChild.leftChild.data)

        return self.validateTree(grandPa.leftChild.leftChild) # запускаем валидацию от ребенка


    return node

  def rotateLeft(self, node):
    tempRight = node.rightChild
    print('tempRight %s' % tempRight.data)
    tempRightLeft = tempRight.leftChild
    print('tempRightLeft %s' % tempRightLeft)

    tempRight.leftChild = node
    node.rightChild = tempRightLeft

    # переприсваиваем родителей
    tempRight.parent = node.parent
    tempRight.leftChild.parent = tempRight
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
    # print(' => %d|%s /up %s' % (node.data, node.color, parentData))
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





