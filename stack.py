# Implement a stack

class Stack():
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)
    def peek(self):
        return self.items[-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == 0

# Build a function to check whether the parenthesis set is balanced.

def check_paren(string):
    s = Stack()
    left = "({["
    right = ")}]"
    ans = True
    for char in string:                
        if char in right:
            if s.isEmpty():
                return False
            else:
                last = s.pop()
                if left.index(last) != right.index(char):
                    ans = False
                else:
                    continue
        else:
            s.push(char)

    return ans                
                    

        
        
    

#print(check_paren("({}{}[]}"))

    