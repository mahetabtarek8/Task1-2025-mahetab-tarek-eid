def selection_sort(arr):
    n = len(arr)

    print(f"the main list : {arr}\n")

    for i in range(n-1):
        min_index = i
        print(f" the step {i+1}:   unsorted array at index {i}")

       
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
       
        print(f"     the min number: {arr[min_index]} at index {min_index}")
        
       
        if min_index != i:
            print(f"   ↔️ swap {arr[i]} with {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print(f"   (no swapping)")

        print(f"    the list after sorting{i+1}: {arr}\n")
    
    print(f"the final result: {arr}")
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
