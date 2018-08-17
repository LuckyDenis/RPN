# -*- coding: utf8 -*-

from collections import deque


def calc(expression):
    """
    Reverse Polish notation
    """

    # bin-operator
    operator = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y)
    }

    stack = deque()
    # get char in string
    for token in expression.split(' '):
        # char is bin-operator
        if token in operator:
            opt2, opt1 = stack.pop(), stack.pop()
            # calculate and push stack
            stack.append(operator[token](opt1, opt2))
        # char is not bin-operator
        elif token:
            # push char in stack
            stack.append(float(token))
    # last element in stack is answer
    return stack.pop()


print(calc('1 2 + 4 * 3 +'))
