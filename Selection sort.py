def selection_sort(arr):
    n = len(arr)  # عدد العناصر في الليست
    for i in range(n - 1):  # بنلف على كل العناصر ماعدا آخر واحد
        min_index = i  # بنفترض إن العنصر ده أصغر واحد
        for j in range(i + 1, n):  # بنقارن مع اللي بعده
            if arr[j] < arr[min_index]:  
                min_index = j  # لو لقينا أصغر، بنحدث الإندكس بتاعه
        arr[i], arr[min_index] = arr[min_index], arr[i]  # نبدلهم

# تجربة الكود
nums = [64, 25, 12, 22, 11]
selection_sort(nums)
print("sorted list :", nums)