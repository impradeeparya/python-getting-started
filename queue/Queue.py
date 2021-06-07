# Implement a FIFO queue which uses an integer array (not List/ArrayList) to store elements and has enque, deque methods.
# Deque should return the dequeued number in a FIFO manner.

class Queue:

    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.rear_index = -1
        self.front_index = -1
        self.queue = [0 for index in range(queue_size)]

    def enque(self, element):
        if self.rear_index == -1 and self.front_index == -1:
            self.rear_index = 0
            self.front_index = 0
            self.queue[self.front_index] = element
            return
        else:
            self.rear_index = self.rear_index + 1

        if self.rear_index >= self.queue_size:
            self.rear_index = 0

        if self.front_index == self.rear_index and self.queue[self.rear_index] != -1:
            print("Queue if full")
        else:
            self.queue[self.rear_index] = element

    def dequeue(self):
        element = -1
        if self.rear_index != -1 and self.front_index != -1:
            element = self.queue[self.front_index]
        self.queue[self.front_index] = -1
        self.front_index = self.front_index + 1

        if self.front_index >= self.queue_size:
            self.front_index = 0

        return element


queue = Queue(3)
queue.enque(1)
queue.enque(2)
queue.enque(3)
print("enqueue : ", queue.queue)
print("dequeue : ", queue.dequeue())
print("dequeue : ", queue.dequeue())
print("dequeue : ", queue.dequeue())
queue.enque(1)
print("enqueue : ", queue.queue)
print("dequeue : ", queue.dequeue())
print("final queue : ", queue.queue)
print("front and rear index : ", queue.front_index, queue.rear_index)

print("######")
queue = Queue(3)
queue.enque(1)
queue.enque(2)
queue.enque(3)
print("enqueue : ", queue.queue)
print("dequeue : ", queue.dequeue())
print("dequeue : ", queue.dequeue())
queue.enque(1)
queue.enque(2)
print("enqueue : ", queue.queue)
print("final queue : ", queue.queue)
print("front and rear index : ", queue.front_index, queue.rear_index)
