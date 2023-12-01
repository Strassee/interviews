from pprint import pprint

class Stack():

    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return True if len(self.stack) == 0 else False
    
    def push(self, new):
        self.stack.append(new)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

def balance(brackets):
    res_balance = dict()
    for bracket in brackets:
        stack = Stack()
        for s in list(bracket):
            if s in '([{':
                stack.push(s)
            elif s in ')]}':
                if stack.size() > 0 and check_pair(stack.peek(), s):
                    stack.pop()                  
                else:
                    res_balance[bracket] = 'No balanced'
                    break
        if bracket not in res_balance:
            if stack.is_empty():
                res_balance[bracket] = 'Balanced'
            else:
                res_balance[bracket] = 'No balanced'
    return res_balance

def check_pair(a, b):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    return open.index(a) == close.index(b)

brackets = ['(((([{}]))))', '}{}', '{{[(])]}}', '[([])((([[[]]])))]{()}', '[[{())}]', '{{[()]}}']
pprint(balance(brackets))