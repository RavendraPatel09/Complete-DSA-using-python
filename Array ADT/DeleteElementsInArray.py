class Array:
    def __init__(self, elements, size, length):
        self.A = elements + [0] * (size - len(elements))
        self.size = size
        self.length = length
def display(arr):
    print("Elements are:")
    for i in range(arr.length):
        print(arr.A[i], end=" ")
    print()
def append(arr, x):
    if arr.length < arr.size:
        arr.A[arr.length] = x
        arr.length += 1
def insert(arr, index, x):
    if index >= 0 and index <= arr.length:
        for i in range(arr.length, index, -1):
            arr.A[i] = arr.A[i - 1]
        arr.A[index] = x
        arr.length += 1
def Delete(arr, index):
    x = 0
    if index >= 0 and index < arr.length:
        x = arr.A[index]
        for i in range(index, arr.length - 1):
            arr.A[i] = arr.A[i + 1]
        arr.length -= 1
        return x
    return 0
arr = Array([2, 3, 4, 5, 6], 10, 5)
print("Deleted element is", Delete(arr, 2))
display(arr)