package Coachable.sorting;

public class MergeSort {

	private MergeSort() {
	}

	private static Comparable<Object>[] aux;


	public static void sort(Comparable[] arr) {

		// initiate the auxiliary array
		aux = new Comparable[arr.length];

		sort(arr, 0, arr.length - 1);
	}

	private static void sort(Comparable<Object>[] arr, int low, int high) {
		// base condition for recursive calls
		// merge sort needs at-least 2 elements
		if (low >= high) return;

		int mid = low + ((high - low) / 2);

		sort(arr, low, mid);
		sort(arr, mid + 1, high);

		merge(arr, low, mid, high);
	}

	private static void merge(Comparable<Object>[] arr, int low, int mid, int high) {

		if (high - low + 1 < 1) return;

		System.arraycopy(arr, 0, aux, 0, arr.length);

		// two pointers. i: low to mid, j:mid+1 to high
		// k: low to high
		int i = low, j = mid + 1;
		for (int k = low; k <= high; k++) {
			if (i > mid) arr[k] = aux[j++];
			else if (j > high) arr[k] = aux[i++];
			else if (isLess(aux[i], aux[j])) arr[k] = aux[i++];
			else arr[k] = aux[j++];
		}
	}

	private static boolean isLess(Comparable<Object> a, Comparable<Object> b) {
		if (a.equals(b)) return false;
		return a.compareTo(b) < 0;
	}

}
