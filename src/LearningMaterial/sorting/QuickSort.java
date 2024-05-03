package Coachable.sorting;

public class QuickSort {
	private QuickSort() {
	}

	public static void sort(Comparable[] arr) {
		sort(arr, 0, arr.length - 1);
	}

	private static void sort(Comparable[] arr, int low, int high) {
		// base condition
		if (low >= high) return;

		int partitionIdx = partition(arr, low, high);
		sort(arr, low, partitionIdx - 1);
		sort(arr, partitionIdx + 1, high);
	}

	private static int partition(Comparable[] arr, int low, int high) {
		Comparable pivot = arr[low];

		int i = low, j = high + 1;

		while (true) {

			while (isLess(arr[++i], pivot))
				if (i == high) break;

			while (isLess(pivot, arr[--j]))
				if (j == low) break;

			if (i >= j) break;
			exchange(arr, i, j);
		}
		exchange(arr, low, j);
		return j;
	}

	private static boolean isLess(Comparable a, Comparable b) {
		if (a.equals(b)) return false;
		return a.compareTo(b) < 0;
	}

	private static void exchange(Comparable[] arr, int i, int j) {
		Comparable temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}
}