package Coachable.sorting;

public class SelectionSortIntegers {

	private SelectionSortIntegers() {
	}

	/**
	 * Selection Sorting
	 * Time Complexity -> O(n^2)
	 * Space Complexity -> O(1)
	 */
	public static void sort(int[] arr) {

		for (int i = 0; i < arr.length; i++) {

			int min = i;

			for (int j = i + 1; j < arr.length; j++)
				if (arr[j] < arr[min]) min = j;

			swap(arr, i, min);
		}

	}

	// Helper function to swap elements in the given array
	private static void swap(int[] arr, int i, int j) {
		int temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}


}

