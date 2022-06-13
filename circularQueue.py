class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.lizt = [None] * k
        self.front = None
        self.rear = None

    def isEmpty(self) -> bool:
        if self.rear == None and self.front == None:
            return True

        else:
            return False
        

    def isFull(self) -> bool:
        if self.front == None:
            return False
        elif self.front == 0 and self.rear == (self.k - 1):
            return True
        elif (self.front - 1) == self.rear:
            return True
        else:
            return False
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front == None and self.rear == None:
                self.lizt[0] = value
                self.rear = 0
                self.front = 0
                return True
            elif self.rear < self.k - 1:
                self.lizt[self.rear + 1] = value
                self.rear += 1 
                return True
            else:
                self.lizt[0] = value
                self.rear = 0
                return True
                
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.lizt[self.front] = None
            if self.front == self.rear:
                self.front = None
                self.rear = None
            elif self.front < self.k - 1:
                self.front += 1
            
            else:
                self.front = 0
            return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.lizt[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.lizt[self.rear]
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


obj = MyCircularQueue(6)
param_1 = obj.enQueue(6)
param_7 = obj.Rear()
param_8 = obj.Rear()
param_9 = obj.deQueue()
param_11 = obj.enQueue(5)
print(param_11)
