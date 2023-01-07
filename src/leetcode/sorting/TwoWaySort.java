package leetcode.sorting;

import java.util.Arrays;


public class TwoWaySort {

    public static void main(String[] args) {
        int[] arr = new int[]{9, 3, 5, 3, 7, 5, 6, 4, 8, 2};
        System.out.println("arr=" + Arrays.toString(arr));
        sort(arr);
        System.out.println("arr=" + Arrays.toString(arr));

        // base case
        // split them into two
    }

    private static void sort(int[] arr) {
        // base case
        if (arr.length < 2) return;

        // split them into two
        int mid = arr.length / 2;
        int[] leftArr = new int[mid];
        int[] rightArr = new int[arr.length - mid];
        System.arraycopy(arr, 0, leftArr, 0, mid);
        System.arraycopy(arr, mid, rightArr, 0, arr.length - mid);

        sort(leftArr);
        sort(rightArr);

        // join them
        mergeSort(leftArr, rightArr, arr);

    }

    private static void mergeSort(int[] leftArr, int[] rightArr, int[] finalArr) {

        int i = 0, j = 0, k = 0;

        while (i < leftArr.length && j < rightArr.length) {
            if (leftArr[i] < rightArr[j]) finalArr[k++] = leftArr[i++];
            else finalArr[k++] = rightArr[j++];
        }

        while (i < leftArr.length) finalArr[k++] = leftArr[i++];
        while (j < rightArr.length) finalArr[k++] = rightArr[j++];
    }

}

