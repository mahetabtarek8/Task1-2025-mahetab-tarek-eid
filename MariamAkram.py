def selection_sort(A):
    n = len(A)
    for j in range(n - 1):
        smallest = j
        for i in range(j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

# Example usage
arr = [12, 3, 5, 7, 19, 26, 2]
selection_sort(arr)
print("Sorted array:", arr)
