class Array:
    def __init__(self):
        self.A = []
        self.size = 0
        self.length = 0
def display(arr):
    print("Elements are:")
    for i in range(arr.length):
        print(arr.A[i], end=" ")
arr = Array()
arr.size = int(input("Enter the Size of an Array: "))
arr.A = [0] * arr.size
arr.length = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(arr.length):
    arr.A[i] = int(input(f"Enter element {i + 1}: "))
display(arr)