package Coachable.sorting;

public class MergeSortIntegers {

	private MergeSortIntegers() {
	}

	public static void sort(int[] arr) {
		// create the auxiliary array
		int[] auxiliaryArr = new int[arr.length];
		// call the main sort method, using this auxiliary array
		sort(arr, auxiliaryArr, 0, arr.length - 1);
	}

	private static void sort(int[] arr, int[] aux, int low, int high) {

		// base condition for recursive calls
		// low shouldn't touch high, i.e., if they do, then it's a single element
		// minimum requirement is 2 elements for merging
		if (low >= high) return;

		// mid-point to split the array into two halves
		int mid = low + ((high - low) / 2);

		// split the array into sub-arrays, sort them
		// recursively sort the left half and right half
		sort(arr, aux, low, mid);
		sort(arr, aux, mid + 1, high);

		// merge the sorted arrays, back to main array
		merge(arr, aux, low, mid, high);
	}

	private static void merge(int[] originalArr, int[] auxArr, int low, int mid, int high) {

		if (high - low + 1 < 1) return;

		// copy to aux[]
		System.arraycopy(originalArr, low, auxArr, low, high + 1 - low);

		// two pointers. i: goes from low to mid, j: goes from mid to high
		int i = low, j = mid + 1;

		// k: goes from low to high (high is index, k should go until high)
		for (int k = low; k <= high; k++) {

			// 'i' went out of bounds, meaning, still items left in 2nd half
			if (i > mid) originalArr[k] = auxArr[j++];

				// j went out of bounds, meaning, still items left in 1st half
			else if (j > high) originalArr[k] = auxArr[i++];

				//add the smallest of both arrays
			else if (auxArr[i] < auxArr[j]) originalArr[k] = auxArr[i++];
			else originalArr[k] = auxArr[j++];
		}
	}
}

