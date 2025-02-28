name = "Hamza Khalid Elmandouh"
Section = 3

def selection(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

arr = [10, 15, 12, 22, 11]
sorted = selection(arr)
print("Sorted array:", sorted)