class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.rear = 0
        self.front = 0

    def push(self):
        
