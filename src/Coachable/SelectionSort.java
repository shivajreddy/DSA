package Coachable;

import java.util.Arrays;


public class SelectionSort {
	public static void main(String[] args) {

		//int[] arr = new int[]{-20, -10, 30, 0, -1, 4};
		int[] arr = new int[]{4,0,18,24,16,20,4,18,19,8,14,13};

		selectionSorting(arr);

		System.out.println(Arrays.toString(arr));


		for (int num : arr){
			char c = (char) (num + 65);
			System.out.print(c + " ");
		}
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

