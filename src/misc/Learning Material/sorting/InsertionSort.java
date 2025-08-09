package Coachable.sorting;


public class InsertionSort {

	private InsertionSort() {
	}

	public static void sort(Comparable[] arr) {

		for (int i = 0; i < arr.length; i++)

			for (int j = i; j > 0 && isLess(arr[j], arr[j - 1]); j--)
				swap(arr, j, j - 1);

	}

	private static boolean isLess(Comparable a, Comparable b) {
		if (a.equals(b)) return false;
		return a.compareTo(b) < 0;
	}

	// Helper function to swap elements in the given array
	private static void swap(Comparable[] arr, int i, int j) {
		Comparable temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}

}
