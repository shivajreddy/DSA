package Coachable.sorting;

import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {

        int[] arr = new int[]{9, 3, 5, 3, 7, 5, 6, 4, 8, 2};

        System.out.println("arr=" + Arrays.toString(arr));
        mergeSort(arr);
        System.out.println("arr=" + Arrays.toString(arr));
    }

    private static void mergeSort(int[] arr) {
        // base condition
        if (arr.length < 2) return;

        // mid index
        int mid = arr.length / 2;

        int[] arr_left = new int[mid];
        int[] arr_right = new int[arr.length - mid];

        // copy elements to arr_left & arr_right
        System.arraycopy(arr, 0, arr_left, 0, mid);
        System.arraycopy(arr, mid, arr_right, 0, arr.length - mid);

        // recursive call both halves
        mergeSort(arr_left);
        mergeSort(arr_right);

        // merge
        merge(arr_left, arr_right, arr);
    }

    // Merge function
    private static void merge(int[] arr_a, int[] arr_b, int[] arr_result) {

        int m = arr_a.length;
        int n = arr_b.length;

        // pointers for first_array, second_array, result_array
        int i = 0, j = 0, k = 0;

        while (i < m && j < n) {
            if (arr_a[i] < arr_b[j]) {
                arr_result[k++] = arr_a[i++];
            } else {
                arr_result[k++] = arr_b[j++];
            }
        }
        // copy remaining items in each array, if any.
        for (; i < m; i++) arr_result[k++] = arr_a[i];
        for (; j < n; j++) arr_result[k++] = arr_b[j];
    }
}
