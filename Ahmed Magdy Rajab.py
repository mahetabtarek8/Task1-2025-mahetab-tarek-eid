def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr =[1,11,2,22,3,33,4,44,5,55,6,66,7,77,8,88,9,99]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
