class Queue:

    def __init__(self):
        
        self.queue = []

    def enqueue(self,value):

        self.queue.append(value)

    def dequeue(self):

        if self.queue:
            dequeued_value = self.queue.pop(0)
            print(f'Dequeued value is {dequeued_value}')
        else:
            print('Queue is empty!')

    def isempty(self):

        if self.queue :
            print('Queue is not empty')
        else:
            print('Queue is empty')

    def get_position(self,value):

        while self.queue:
            if value in self.queue:
                print(f'{value} is present in position {self.queue.index(value)+1}')
                return
        else:
            print('Queue is empty')

    def size(self):
        
        print(f'Size of the queue is :{len(self.queue)}')

    def print(self):

        print(f'The Queue is {self.queue}')

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.size()
q.isempty()
q.get_position(30)