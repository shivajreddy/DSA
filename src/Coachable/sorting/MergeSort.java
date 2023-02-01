package Coachable.sorting;

public class MergeSort {

	private MergeSort() {
	}

	public static void sort(int[] arr) {
		// create the auxiliary array
		int[] auxiliaryArr = new int[arr.length];
		// call the main sort method, using this auxiliary array
		sort(arr, auxiliaryArr, 0, arr.length - 1);
	}

	private static void sort(int[] arr, int[] aux, int low, int high) {

		if (high <= low) return;

		// split the array into sub-arrays, sort them
		int mid = low + ((high - low) / 2);

		// recursively sort the left half and right half
		sort(arr, aux, low, mid);
		sort(arr, aux, mid + 1, high);

		// merge the sorted arrays, back to main array
		merge(arr, aux, low, mid, high);
	}

	private static void merge(int[] originalArr, int[] auxiliaryArr, int low, int mid, int high) {

		// copy to aux[]
		if (high - low + 1 >= 0) System.arraycopy(originalArr, low, auxiliaryArr, low, high + 1 - low);

		int i = low, j = mid + 1;
		for (int k = low; k <= high; k++) {

			// 'i' went out of bounds, meaning, still items left in 2nd half
			if (i > mid) originalArr[k] = auxiliaryArr[j++];

				// j went out of bounds, meaning, still items left in 1st half
			else if (j > high) originalArr[k] = auxiliaryArr[i++];

				//add the smallest of both arrays
			else if (auxiliaryArr[i] < auxiliaryArr[j]) originalArr[k] = auxiliaryArr[i++];
			else originalArr[k] = auxiliaryArr[j++];
		}
	}
}
