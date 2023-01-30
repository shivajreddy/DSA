package Coachable.sorting;


import java.util.Arrays;


public class QuickSort {

	public static void main(String[] args) {

		int[] arr = new int[]{50, 70, 60, 90, 40, 80, 10, 20, 30, 9999};
		System.out.println(Arrays.toString(arr));
		partition(arr, 0, arr.length - 1);
		System.out.println(Arrays.toString(arr));

	}


	// partitioning technique
	private static void partition(int[] arr, int left, int right) {

		int pivot = arr[left];

		int i = left;
		int j = right;


		//while (i < j){
		do {
			do i++;
			while (arr[i] <= pivot);

			do j--;
			while (arr[j] > pivot);

			// swap elements at i, j. Only if i,j didn't cross
			if (i < j) {
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}

		}
		while (i < j);

		// swap pivot with element at j
		arr[left] = arr[j];
		arr[j] = pivot;
	}

}

