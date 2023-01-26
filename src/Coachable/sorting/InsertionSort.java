package Coachable.sorting;

import java.util.Arrays;


public class InsertionSort {


	public static void main(String[] args) {

		int[] arr = new int[]{10, 20, 30, 0, -1, 4};

		insertionSort(arr);

		System.out.println(Arrays.toString(arr)); // [-1, 0, 4, 10, 20, 30]

	}


	/**
	 * InsertionSort Algorithm
	 * Time Complexity -> O(n^2)
	 * Space Complexity -> O(1)
	 */

	private static void insertionSort(int[] arr) {

		for (int i = 1; i < arr.length; i++) {

			int curr = arr[i];

			int j = i - 1;
			while (j > -1 && arr[j] > curr) {    //**NOT while ( arr[j] > curr && j > -1){
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
