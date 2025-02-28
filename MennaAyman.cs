using System;

namespace SelectionSortAlgorithm
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] values = { 9, 34, 2, 15, 76, 41, 58 };
            Console.WriteLine("Array before sorting:");
            SelectionSort.PrintArray(values);

            SelectionSort.Sort(values);

            Console.WriteLine("\nArray after sorting:");
            SelectionSort.PrintArray(values);
        }

        public class SelectionSort
        {
            // Method to perform the selection sort
            public static void Sort(int[] values)
            {
                int size = values.Length;

                // Traverse through the entire array
                for (int i = 0; i < size - 1; i++)
                {
                    // Assume the current element is the smallest
                    int smallestIndex = i;
                    for (int j = i + 1; j < size; j++)
                    {
                        // Find the smallest element in the unsorted part of the array
                        if (values[j] < values[smallestIndex])
                        {
                            smallestIndex = j;
                        }
                    }

                    // Swap the found smallest element with the first unsorted element
                    int temp = values[smallestIndex];
                    values[smallestIndex] = values[i];
                    values[i] = temp;
                }
            }

            // Method to print the contents of the array
            public static void PrintArray(int[] values)
            {
                foreach (int value in values)
                {
                    Console.Write(value + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
