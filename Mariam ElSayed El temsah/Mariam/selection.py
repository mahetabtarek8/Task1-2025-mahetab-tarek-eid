def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print(" ".join(map(str, arr)))

arr = [64, 25, 12, 22, 11]
print("For the matrix before sorting:")
print_array(arr)

selection_sort(arr)

print("For the matrix after sorting:")
print_array(arr)
