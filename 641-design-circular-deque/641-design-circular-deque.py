class MyCircularDeque:

    def __init__(self, k: int):
        self.l = k
        self.left = k-1
        self.right = 0
        self.node = [None] * k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.node[self.left] == None:
            self.node[self.left] = value
            if self.left != 0:
                self.left -= 1
            else:
                self.left = self.l-1
            self.count += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.node[self.right] == None:
            self.node[self.right] = value
            if self.right != self.l-1:
                self.right += 1
            else:
                self.right = 0
            self.count += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.node[(self.left+1)%self.l] != None:
            self.node[(self.left+1)%self.l] = None
            self.left = (self.left+1)%self.l
            self.count -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.node[(self.right-1)%self.l] != None:
            self.node[(self.right-1)%self.l] = None
            self.right = (self.right-1)%self.l
            self.count -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1    
        return self.node[(self.left+1)%self.l]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1    
        return self.node[(self.right-1)%self.l]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.l


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()