class Array:
    def __init__(self):
        self.A=[100,300,400]+[0]*7
        self.size=10
        self.length=3
def display(arr):
    print("Elements are:")
    for i in range(arr.length):
        print(arr.A[i],end=" ")
    print()
def swap(x,y):
    return y,x
def LinearSearch(arr,key):
    for i in range(arr.length):
        if key==arr.A[i]:
            arr.A[i],arr.A[i-1]=swap(arr.A[i],arr.A[i-1])
            return i
    return -1
def Get(arr,index):
    if index>=0 and index<arr.length:
        return arr.A[index]
    return -1
def Set(arr,index,x):
    if index>=0 and index<arr.length:
        arr.A[index]=x
def Max(arr):
    maximum=arr.A[0]
    for i in range(1,arr.length):
        if arr.A[i]>maximum:
            maximum=arr.A[i]
    return maximum
def Min(arr):
    minimum=arr.A[0]
    for i in range(1,arr.length):
        if arr.A[i]<minimum:
            minimum=arr.A[i]
    return minimum
def Sum(arr):
    total=0
    for i in range(arr.length):
        total+=arr.A[i]
    return total
def InsertSort(arr,x):
    i=arr.length-1
    if arr.length==arr.size:
        return
    while i>=0 and arr.A[i]>x:
        arr.A[i+1]=arr.A[i]
        i-=1
    arr.A[i+1]=x
    arr.length+=1
def isSorted(arr):
    for i in range(arr.length-1):
        if arr.A[i]>arr.A[i+1]:
            return 0
    return 1
arr=Array()
print("Sorted:",isSorted(arr))
display(arr)