'''define new visit method, without recursion( stack for loop )'''
#Data Part
class Node:
    pass
class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(UnaryOperator):
    pass
class Number(Node):
    def __init__(self, value):
        self.value = value

# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

import types

class NodeVisitor:
    def visit(self, node):
        stack = [ node ]
        last_reuslt = None
        while stack:
            try:
                last = stack[-1]
                if isinstance( last, types.GeneratorType):
                    stack.append( last.send( last_reuslt ) )
                    last_reuslt = None
                elif isinstance( last, Node):
                    stack.append(self._visit(stack.pop()))#yield will append new node!
                else:
                    last_reuslt = stack.pop()
            except StopIteration:
                stack.pop()
        return last_reuslt
    def _visit(self , node):
        methname = 'visit_'+type(node).__name__
        meth = getattr(self, methname, None )
        if meth is None:
            meth = self.generic_visit
        return meth( node )

    def generic_visit(self, node):
        raise  RuntimeError('No {} method'.format( 'visit_' + type(node).__name__ ))
# A sample visitor class that evaluates expressions
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        yield (yield  node.left) + (yield node.right) #Magic

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield  node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield  node.operand)

# Evaluate it
e = Evaluator()
print(e.visit(t4)) # Outputs 0.6

a = Number(0)
for n in range(1, 100000):
    a = Add( a, Number(n) )

e = Evaluator()
print( e.visit( a ))  #maxium recursion depth exceeded