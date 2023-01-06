package leetcode.sorting;

import java.util.Arrays;


public class MergeSort {

    public static void main(String[] args) {
        // int[] arr = new int[]{9, 3, 7, 5, 6, 4, 8, 2};
        int[] arr = new int[]{1, 2, 3, 2, 1};
        sort(arr);
        System.out.println("arr=" + Arrays.toString(arr));
    }

    public static void sort(int[] arr) {

        // base condition
        if (arr.length < 2) return;

        int mid = arr.length / 2;

        int[] leftArr = new int[mid];
        System.arraycopy(arr, 0, leftArr, 0, mid);

        int[] rightArr = new int[arr.length - mid];
        System.arraycopy(arr, mid, rightArr, 0, arr.length - mid);

        sort(leftArr);
        sort(rightArr);

        // merging
        merge(arr, leftArr, rightArr);
    }

    private static void merge(int[] arr, int[] leftArr, int[] rightArr) {
        int m = leftArr.length;
        int n = rightArr.length;
        int i = 0, j = 0, k = 0;
        while (i < m && j < n) {
            if (leftArr[i] < rightArr[j]) {
                arr[k++] = leftArr[i++];
            } else {
                arr[k++] = rightArr[j++];
            }
        }
        for (; i < m; i++) arr[k++] = leftArr[i];
        for (; j < n; j++) arr[k++] = rightArr[j];
    }
}

