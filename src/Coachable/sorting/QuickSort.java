package Coachable.sorting;


import java.util.Arrays;


public class QuickSort {

	public static void main(String[] args) {

		int[] arr = new int[]{50, 70, 60, 90, 40, 80, 10, 20, 30, 9999};
		System.out.println(Arrays.toString(arr));


		QuickSorting(arr, 0, arr.length - 1);
		System.out.println(Arrays.toString(arr));
	}

	private static void QuickSorting(int[] arr, int low, int high) {

		// recursively call quick sorting
		if (low < high) {

			// get the partition using the entire array
			int partitionIdx = partition(arr, low, high);

			// recursive call on the left half
			QuickSorting(arr, low, partitionIdx);

			// recursive call on the right half
			QuickSorting(arr, partitionIdx + 1, high);
		}
	}

	private static int partition(int[] arr, int l, int h) {

		int pivot = arr[l];

		int i = l;
		int j = h;

		do {
			// find item > pivot, using i
			do i++;
			while (arr[i] <= pivot);

			// find item <= pivot, using j
			do j--;
			while (arr[j] > pivot);

			// swap both items, only if pointers didn't cross
			if (i < j) {
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		} while (i < j);

		// bring the pivot to j
		arr[l] = arr[j];
		arr[j] = pivot;

		return j;
	}


}

