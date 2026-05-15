class Array:
    def __init__(self, elements, size, length):
        self.A = elements + [0] * (size - len(elements))
        self.size = size
        self.length = length
def display(arr):
    print("Elements are:")
    for i in range(arr.length):
        print(arr.A[i], end=" ")
def append(arr, x):
    if arr.length < arr.size:
        arr.A[arr.length] = x
        arr.length += 1
arr = Array([2, 3, 4, 5, 6], 10, 5)
append(arr, 10)
display(arr)
