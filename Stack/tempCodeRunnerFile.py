class Stack:
    
    def __init__(self):

        self.stack = []

    def push(self,value):

        self.stack.append(value)
    
    def isempty(self):

        if not self.stack:
            print('Stack is empty')
        else:
            print('Stack is not empty')

    def pop(self):

        if self.stack:
            popped_value = self.stack.pop()
            print(f'Popped value is {popped_value}')
        else:
            print('Stack is empty!')

    def peek(self):

        if self.stack:
            print(f'First element in stack : {(self.stack[-1])}')
        else:
            print('Stack is empty!')

    def size(self):

        print(f'Size of the stack is :{len(self.stack)}')

    def print(self):

        print(f'The stack is {self.stack[::-1]}')

    def clear(self):

        self.stack.clear()

    def search(self,value):

        while value in self.stack:
            list_index = self.stack.index(value)
            stack_index = len(self.stack)-1-list_index
            print(f'{value} is in {stack_index+1} from the top')
            return
        else:
            print('Item not in List')


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.print()
s.pop()
s.print()
s.search(40)
s.peek()
s.size()
s.isempty()
s.clear()
s.isempty()