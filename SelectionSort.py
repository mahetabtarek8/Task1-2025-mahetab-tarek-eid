#Section 4
#Rehab_Ahmed_Sharaf Al-Dein

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
numbers = [29, 10, 14, 37, 13]
print("Before:", numbers)
selection_sort(numbers)
print("After:", numbers)