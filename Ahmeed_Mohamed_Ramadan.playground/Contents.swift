import UIKit


// Mark Made By Ahmed Mohamed Ramadan (Section : 1)


func selectionSort<T: Comparable>(_ array: [T]) -> [T] {
    var arr = array
    for i in 0..<arr.count - 1 {
        var minIndex = i
        for j in i + 1..<arr.count {
            if arr[j] < arr[minIndex] {
                minIndex = j
            }
        }
        if i != minIndex {
            arr.swapAt(i, minIndex)
        }
    }
    return arr
}



let unsortedArray = [63, 25, 12, 22, 11, 200]
let sortedArray = selectionSort(unsortedArray)
print(sortedArray) // Output: [11, 12, 22, 25, 63, 200]
