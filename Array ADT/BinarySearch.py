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
def BinarySearch(arr, key):
    l = 0
    h = arr.length - 1
    while l <= h:
        mid = (l + h) // 2
        if key == arr.A[mid]:
            return mid
        elif key < arr.A[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return -1
arr = Array([2, 3, 4, 5, 6], 10, 5)
print("Index of element is", BinarySearch(arr, 2))
display(arr)