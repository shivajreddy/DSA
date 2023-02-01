package Coachable.sorting;

import java.util.Arrays;


public class MergeSortBU {

	public static void main(String[] args) {

		int [] arr = new int[] {10, 30, 1, -10, 20};
		System.out.println(Arrays.toString(arr));

		sort(arr);
		System.out.println(Arrays.toString(arr));

	}

	private static int[] auxArr;

	public static void sort(int[] arr) {
		int n = arr.length;
		auxArr = new int[n];

		for (int size = 0; size < arr.length; size = size + size) {


			for (int lo = 0; lo < n - size; lo += size + size)

				merge(arr, lo, lo + size - 1, Math.min(lo + size + size - 1, n - 1));


		}
	}

	//private static void merge(int[] arr, int[] auxArr, int low, int mid, int high) {
	private static void merge(int[] arr, int low, int mid, int high) {

		for (int i = 0; i < arr.length; i++)
			auxArr[i] = arr[i];

		int i = low, j = mid + 1;

		for (int k = low; k <= high; k++) {

			if (i > mid) arr[k] = auxArr[j++];

			else if (j > high) arr[k] = auxArr[i++];

			else if (auxArr[i] <= auxArr[j]) arr[k] = auxArr[i++];

			else arr[k] = auxArr[j++];
		}
	}

}


