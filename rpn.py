#!/usr/bin/env python3

import operator

import readline

#from colored import fg, bg

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '%': operator.mod,
        '-': operator.neg,
}
def calculate(myarg):
    #colors = bg('rosy_brown') + fg('sea_green_2')
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            print(stack)
#        print(colors + stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

   # tokens = arg.split()
   # print(tokens)

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
