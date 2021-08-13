class Node:
    def __init__(self, value):
        self._value = value
        self._chidren = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def addChild(self, node):
        self._chidren.append(node)

    def removeChild(self, node):
        self._chidren.remove(node)

    def __iter__(self):#for n in Node
        return iter(self._chidren)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.addChild(child1)
    root.addChild(child2)
    for ch in root:
        print( ch )