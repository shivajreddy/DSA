package Coachable.sorting;

import java.util.Arrays;


public class InsertionSortIntegers {

	/**
	 * InsertionSort Algorithm
	 * Time Complexity -> O(n^2)
	 * Space Complexity -> O(1)
	 */

	public static void sort(int[] arr) {

		for (int i = 1; i < arr.length; i++) {

			int curr = arr[i];

			int j = i - 1;
			while (j >= 0 && arr[j] > curr) {    //**NOT while ( arr[j] > curr && j >= 0){
				// move to right
				arr[j + 1] = arr[j];
				j -= 1;
			}
			arr[j + 1] = curr;
		}
	}


	/**
	 * Insertion technique
	 * Time Complexity -> O(n)
	 * Space Complexity -> O(1)
	 */
	private static int[] insert(int[] input, int target) {

		int[] result = Arrays.copyOf(input, input.length + 1);

		int i = input.length - 1;
		while (i >= 0) {

			int curr = input[i];
			if (curr > target) {
				result[i + 1] = curr;
				i -= 1;
			} else {
				result[i + 1] = target;
				return result;
			}
		}

		return result;
	}

}
