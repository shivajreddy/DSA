package Coachable.sorting;

import java.util.Arrays;



public class HeapSort {

	public static void main(String[] args) {


		int[] arr = new int[]{0, 40, 25, 35, 10, 5, 20, 30};
		System.out.println(delete(arr, 7));

		//int[] arr = new int[]{0, 30, 10, 20};
		//System.out.println(delete(arr, 3));

		System.out.println(Arrays.toString(arr));

	}


	private static void createHeap(int[] arr) {
		for (int i = 2; i < arr.length; i++) {
			insert(arr, i);
		}
	}

	private static void insert(int[] arr, int newIdx) {

		int i = newIdx;
		int temp = arr[newIdx];

		while (i > 1 && arr[i / 2] < temp) {
			arr[i] = arr[i / 2];
			i = i / 2;
		}
		arr[i] = temp;
	}


	// delete number from heap
	private static int delete(int[] arr, int n) {

		// root goes out of 1-indexed array
		int root = arr[1];
		int last = arr[n];

		arr[1] = last;		// last comes to root
		arr[n] = root;		// first comes to last


		// Re-arrange the last, until it finds place
		int i = 1;
		int childIdx = i * 2;

		while (childIdx < n - 1) {

			// childIdx should point to the bigger child
			if (arr[childIdx + 1] > arr[childIdx])
				childIdx++;

			if (arr[i] < arr[childIdx]) {
				int temp = arr[i];
				arr[i] = arr[childIdx];
				arr[childIdx] = temp;

				i = childIdx;
				childIdx *= 2;
			} else
				break;
		}

		return root;

	}

}
