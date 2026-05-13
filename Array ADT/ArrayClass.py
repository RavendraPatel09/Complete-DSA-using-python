class Array:
    def __init__(self, sz=10):
        self.size = sz
        self.length = 0
        self.A = [0] * sz
    def Display(self):
        print("Elements are:")
        for i in range(self.length):
            print(self.A[i], end=" ")
        print()
    def Insert(self, index, x):
        if index >= 0 and index <= self.length:
            for i in range(self.length, index, -1):
                self.A[i] = self.A[i - 1]
            self.A[index] = x
            self.length += 1
    def Delete(self, index):
        x = 0
        if index >= 0 and index < self.length:
            x = self.A[index]
            for i in range(index, self.length - 1):
                self.A[i] = self.A[i + 1]
            self.length -= 1
        return x
arr = Array(10)
arr.Insert(0, 2)
arr.Insert(1, 4)
arr.Insert(2, 6)
arr.Display()
arr.Delete(1)
print("After Deletion:")
arr.Display()