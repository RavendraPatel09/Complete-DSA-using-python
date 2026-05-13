arr = [1, 2, 2, 4, 5, 6, 6, 7, 7, 8, 9]
maximum = arr[0]
for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
H = [0] * (maximum + 1)
for i in range(len(arr)):
    H[arr[i]] += 1
for i in range(maximum + 1):
    if H[i] > 1:
        print(i, "is repeated", H[i], "times")