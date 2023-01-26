package Coachable;

import java.util.Arrays;


public class SelectionSort {
	public static void main(String[] args) {

		int[] arr = new int[]{-20, -10, 30, 0, -1, 4};

		selectionSorting(arr);

		System.out.println(Arrays.toString(arr));

	}

	/**
	 * Selection Sorting
	 * Time Complexity -> O(n^2)
	 * Space Complexity -> O(1)
	 */

	private static void selectionSorting(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			int curr = arr[i];
			int minIdx = i;
			for (int j = i; j < arr.length; j++){
				if (arr[j] < arr[minIdx])
					minIdx = j;
			}
			int temp = arr[i];
			arr[i] = arr[minIdx];
			arr[minIdx] = temp;
		}
	}

}

