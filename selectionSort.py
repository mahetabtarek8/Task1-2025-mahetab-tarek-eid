def selection_sort(arr):
    size = len(arr)
    for step in range(size):
        smallest_index = step
        for current in range(step + 1, size):
            if arr[current] < arr[smallest_index]:
                smallest_index = current
        arr[step], arr[smallest_index] = arr[smallest_index], arr[step]

values = [88, 17, 35, 12, 5]
print("قبل الترتيب:", values)
selection_sort(values)

print("بعد الترتيب:", values)