'''
You need to write code that processes or navigates through a complicated data structure
consisting of many different kinds of objects, each of which needs to be handled in a
different way. For example, walking through a tree structure and performing different
actions depending on what kind of tree nodes are encountered.
Visitor Pattern vs Strategy Pattern
'''

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

#Visitor Pattern Part TODO::VISITOR PATTERN
class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__ #starts with visit_ , one visitor pattern implement
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node) #meth have visit , so  Recurion 
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)
    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)
    def visit_Negate(self, node):
        return -node.operand

e = Evaluator()
print( e.visit(t4) )

#Visitor Pattern Part 2#TODO::Stack machine
class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions
    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))
    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))
    def visit_Add(self, node):
        self.binop(node, 'ADD')
    def visit_Sub(self, node):
        self.binop(node, 'SUB')
    def visit_Mul(self, node):
        self.binop(node, 'MUL')
    def visit_Div(self, node):
        self.binop(node, 'DIV')
    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))
    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')

s = StackCode()
s.generate_code( t4 )
print( s.instructions )
