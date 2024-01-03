#
# Implement a queue using two stacks. Then process  queries, where each query is one of the following  types:
#     1: Enqueue element  into the end of the queue.
#     2: Dequeue the element at the front of the queue.
#     3: Print the element at the front of the queue.
#
 
class Queue: 
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        # # Move all elements from s1 to s2 
        # while len(self.s1) != 0: 
        #     self.s2.insert(0, self.s1[-1]) 
        #     self.s1.pop()
 
        # Push item into self.s1 
        self.s1.append(x) 
 
        # # Push everything back to s1 
        # while len(self.s2) != 0: 
        #     self.s1.insert(0, self.s2[-1]) 
        #     self.s2.pop()
 
    # Dequeue first item from the queue 
    def deQueue(self):
         
        # if first stack is empty 
        if len(self.s1) == 0: 
            return 'Nothing in queue.'
     
        # Return top of self.s1 
        self.s2.insert(0, self.s1[0]) 
        self.s1.pop(0) 
    
    def inQueue(self):
        return self.s1

    def outQueue(self):
        return self.s2

# Driver code 
if __name__ == '__main__':
    q = Queue()
    print('Enqueue 42...')
    q.enQueue(42) 
    print(q.inQueue())
    print(q.outQueue())

    print('Dequeue head of the queue...')
    q.deQueue()
    print(q.inQueue())
    print(q.outQueue())

    print('Enqueue 14...')
    q.enQueue(14) 
    print(q.inQueue())
    print(q.outQueue())

    print('Enqueue 28...')
    q.enQueue(28) 
    print(q.inQueue())
    print(q.outQueue())

    print('Enqueue 60...')
    q.enQueue(60) 
    print(q.inQueue())
    print(q.outQueue())

    print('Enqueue 78...')
    q.enQueue(78) 
    print(q.inQueue())
    print(q.outQueue())

    print('Dequeue head of the queue...')
    q.deQueue()
    print(q.inQueue())
    print(q.outQueue())

    print('Dequeue head of the queue...')
    q.deQueue()
    print(q.inQueue())
    print(q.outQueue())
