using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp7
{
    using System;

    class Program
    {
        static void SelectionSort(int[] A)
        {
            int n = A.Length;
            for (int j = 0; j < n - 1; j++)
            {
                int smallest = j;
                for (int i = j + 1; i < n; i++)
                {
                    if (A[i] < A[smallest])
                    {
                        smallest = i;
                    }
                }
                if (smallest != j)
                {
                    // Swap A[j] and A[smallest]
                    int temp = A[j];
                    A[j] = A[smallest];
                    A[smallest] = temp;
                }
            }
        }

        static void Main()
        {
            int[] arr = { 64, 25, 12, 22, 11 };
            SelectionSort(arr);

            Console.WriteLine("Sorted array: " + string.Join(", ", arr));
        }
    }
}

