class Array:
    def __init__(self, elements=None, size=10, length=0):
        if elements is None:
            elements = []
        self.A = elements + [0] * (size - len(elements))
        self.size = size
        self.length = length
def display(arr):
    print("Elements are:")
    for i in range(arr.length):
        print(arr.A[i], end=" ")
    print()
def swap(x, y):
    return y, x
def LinearSearch(arr, key):
    for i in range(arr.length):
        if key == arr.A[i]:
            arr.A[i], arr.A[i - 1] = swap(arr.A[i], arr.A[i - 1])
            return i
    return -1
def Get(arr, index):
    if index >= 0 and index < arr.length:
        return arr.A[index]
    return -1
def Set(arr, index, x):
    if index >= 0 and index < arr.length:
        arr.A[index] = x
def Max(arr):
    maximum = arr.A[0]
    for i in range(1, arr.length):
        if arr.A[i] > maximum:
            maximum = arr.A[i]
    return maximum
def Min(arr):
    minimum = arr.A[0]
    for i in range(1, arr.length):
        if arr.A[i] < minimum:
            minimum = arr.A[i]
    return minimum
def Sum(arr):
    total = 0
    for i in range(arr.length):
        total += arr.A[i]
    return total
def InsertSort(arr, x):
    i = arr.length - 1
    if arr.length == arr.size:
        return
    while i >= 0 and arr.A[i] > x:
        arr.A[i + 1] = arr.A[i]
        i -= 1
    arr.A[i + 1] = x
    arr.length += 1
def isSorted(arr):
    for i in range(arr.length - 1):
        if arr.A[i] > arr.A[i + 1]:
            return 0
    return 1
def Rearrange(arr):
    i = 0
    j = arr.length - 1
    while i < j:
        while arr.A[i] < 0:
            i += 1
        while arr.A[j] >= 0:
            j -= 1
        if i < j:
            arr.A[i], arr.A[j] = swap(arr.A[i], arr.A[j])
def Merge(arr1, arr2, arr3):
    i = j = k = 0
    while i < arr1.length and j < arr2.length:
        if arr1.A[i] < arr2.A[j]:
            arr3.A[k] = arr1.A[i]
            i += 1
        else:
            arr3.A[k] = arr2.A[j]
            j += 1
        k += 1
    while i < arr1.length:
        arr3.A[k] = arr1.A[i]
        i += 1
        k += 1
    while j < arr2.length:
        arr3.A[k] = arr2.A[j]
        j += 1
        k += 1
    arr3.length = arr1.length + arr2.length
    arr3.size = 10
def Union(arr1, arr2, arr3):
    i = j = k = 0
    while i < arr1.length and j < arr2.length:
        if arr1.A[i] < arr2.A[j]:
            arr3.A[k] = arr1.A[i]
            i += 1
        elif arr2.A[j] < arr1.A[i]:
            arr3.A[k] = arr2.A[j]
            j += 1
        else:
            arr3.A[k] = arr1.A[i]
            i += 1
            j += 1
        k += 1
    while i < arr1.length:
        arr3.A[k] = arr1.A[i]
        i += 1
        k += 1
    while j < arr2.length:
        arr3.A[k] = arr2.A[j]
        j += 1
        k += 1
    arr3.length = k
    arr3.size = 10
def Intersection(arr1, arr2, arr3):
    i = j = k = 0
    while i < arr1.length and j < arr2.length:
        if arr1.A[i] < arr2.A[j]:
            i += 1
        elif arr2.A[j] < arr1.A[i]:
            j += 1
        else:
            arr3.A[k] = arr1.A[i]
            i += 1
            j += 1
            k += 1
    arr3.length = k
    arr3.size = 10
def Difference(arr1, arr2, arr3):
    i = j = k = 0
    while i < arr1.length and j < arr2.length:
        if arr1.A[i] < arr2.A[j]:
            arr3.A[k] = arr1.A[i]
            i += 1
            k += 1
        elif arr2.A[j] < arr1.A[i]:
            j += 1
        else:
            i += 1
            j += 1
    while i < arr1.length:
        arr3.A[k] = arr1.A[i]
        i += 1
        k += 1
    arr3.length = k
    arr3.size = 10
arr1 = Array([2, 3, 6, 8, 10, 15, 25, 46, 77], 10, 9)
arr2 = Array([1, 4, 5, 8, 10, 35, 24, 67, 7], 10, 9)
arr3 = Array([0] * 10, 10, 0)
Difference(arr1, arr2, arr3)
display(arr3)