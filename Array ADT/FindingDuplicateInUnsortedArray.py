n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print("Duplicate element found:", arr[i])