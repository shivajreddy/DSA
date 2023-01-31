package Coachable.sorting;


import java.util.Arrays;


public class QuickSort {

	public static void main(String[] args) {

		//int[] arr = new int[]{50, 70, 60, 90, 40, 80, 10, 20, 30, 9999};
		//int[] arr = new int[]{69, 65, 83, 89, 81, 85, 69, 83, 84, 73, 79, 78, 9999};
		//int[] arr = new int[]{69, 65, 83, 89, 81, 85, 69, 83, 84, 73, 79, 78};
		int[] arr = new int[]{60, 40, 80, 90, 10};
		System.out.println(Arrays.toString(arr));


		//QuickSorting3Way(arr, arr.length);
		//System.out.println(Arrays.toString(arr));

		QuickSorting(arr, 0, arr.length - 1);
		System.out.println(Arrays.toString(arr));
	}


	// quick sorts only 3 distant elements
	private static void QuickSorting3Way(int[] arr, int size) {

		int low = 0;
		int high = size - 1;
		int mid = 0;

		while (mid <= high) {
			if (arr[mid] == 0) {
				int temp = arr[low];
				arr[low] = arr[mid];
				arr[mid] = temp;
			} else if (arr[mid] == 1)
				mid++;
			else {
				int temp = arr[high];
				arr[high] = arr[mid];
				arr[mid] = temp;
				high--;
			}
		}
	}


	//
	private static void QuickSorting(int[] arr, int low, int high) {

		if (low >= high) return;

		int partitionIdx = partition(arr, low, high);
		QuickSorting(arr, low, partitionIdx - 1);
		QuickSorting(arr, partitionIdx + 1, high);
	}

	private static int partition(int[] arr, int low, int high) {
		int pivot = arr[low];

		int i = low;
		int j = high + 1;

		while (true) {

			while (arr[++i] < pivot)
				if (i == high) break;

			while (arr[--j] > pivot)
				if (j == low) break;

			if (i >= j) break;

			exchange(arr, i, j);
		}
		exchange(arr, low, j);
		return j;
	}

	private static void exchange(int[] arr, int i, int j) {
		int temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}

	//private static boolean isLess(Comparable<Object> v, Comparable<Object> w) {
	private static boolean isLess(int v, int w) {
		if (v == w) return false;
		//return v.compareTo(w) < 0;
		return v < w;
	}


	private static int partition2(int[] arr, int low, int high) {
		// assume last element is the pivot
		int pivot = arr[high];

		// pointer 'i' tracks the latest element that was smaller than pivot
		int i = low - 1;
		// pointer 'j' goes from low to the high-1, since pivot is at high
		for (int j = low; j < high; j++) {

			// search for item that is <= pivot
			if (arr[j] <= pivot) {

				// move 'i', since i current points to the element that is smaller than pivot
				i++;

				// swap the elements at i and j
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}

		// move 'i', swap that element with pivot, and return i
		i++;
		arr[high] = arr[i];
		arr[i] = pivot;

		return i;
	}

	private static int partitionUsingWhileLoop(int[] arr, int l, int h) {

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

