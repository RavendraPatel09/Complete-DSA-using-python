arr = [1, 2, 2, 4, 5, 6, 6, 7, 7, 8, 9]
n = len(arr)
i = 0
while i < n - 1:
    if arr[i] == arr[i + 1]:
        j = i + 1
        while j < n and arr[i] == arr[j]:
            j += 1
        print(arr[i], "is repeated", j - i, "times")
        i = j - 1
    i += 1
    