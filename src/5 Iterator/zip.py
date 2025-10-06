print(list(zip([1, 2], [3, 4], [5, 6, 7])))
arr = [1, 2, 3, 4]
print(list(reversed(arr)))
print(arr)
arr1 = [3, 4, 5, 4, 3]
print(all(a == b for a, b in zip(arr, reversed(arr))))
print(all(a == b for a, b in zip(arr1, reversed(arr1))))
