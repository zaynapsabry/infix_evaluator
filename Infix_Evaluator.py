from decimal import Decimal as D
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Push(self, value):
        self.items.append(value)

    # Pre: Check if the stack not empty.
    def Pop(self):
        return self.items.pop()

    # Pre: Check if the stack not empty.
    def Peak(self):
        return self.items[len(self.items) - 1]
    def Size(self):
        return len(self.items)
    def Print(self):
        for i in (self.items):
            print(i)


def doMath(op, opr2, opr1):
    if op == '+':
        return D(opr1) + D(opr2)
    elif op == '-':
        return D(opr1) - D(opr2)
    elif op == '*':
        return D(opr1) * D(opr2)
    elif op == '/':
        if opr2 == '0':
            print("MATH ERROR")
            exit()
        return D(opr1) / D(opr2)
    else:
        return D(opr1) ** D(opr2)


# A function to evaluate infix expression.
def infixEval(strinput):
    strinput = strinput.split()
    # initializing stackes
    num = Stack()
    op = Stack()
    precd = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
        ')': 1
    }
    # Doing operations
    for i in strinput:
        if i not in '+-*/^()':
            num.Push(i)
        elif i in '+-*/^()':
            if op.isEmpty():
                op.Push(i)
            # Special case (parenthesis)
            elif i == ')':
                while not op.Peak() == '(':
                    num.Push(doMath(op.Pop(), num.Pop(), num.Pop()))
                op.Pop() #to pop the ')'
            # General case (Left to right)
            elif precd[i] > precd[op.Peak()] or i == '(' or i == '^':
                op.Push(i)
            else:
                while not op.isEmpty() and precd[i] <= precd[op.Peak()]:
                    num.Push(doMath(op.Pop(), num.Pop(), num.Pop()))
                op.Push(i)

    # Calculating remaining operations.
    while not op.isEmpty():
        num.Push(doMath(op.Pop(), num.Pop(), num.Pop()))
    return num.Pop()

if __name__ == '__main__':
    while True:
        inputb = input('Please enter your infix: ')

        print(infixEval(inputb))