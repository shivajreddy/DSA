package Coachable.sorting;

import java.util.Arrays;


public class SelectionSortAssignment {
	private SelectionSortAssignment() {
	}

	private static int count = 0;

	public static void sort(Comparable[] arr) {

		for (int i = 0; i < arr.length; i++) {

			// track the smallest item
			int min = i;
			for (int j = i + 1; j < arr.length; j++)
				if (isLess(arr[j], arr[min])) min = j;
			swap(arr, i, min);
			System.out.println("count: " + ++count);
			System.out.println("arr: " + Arrays.toString(arr));
		}

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

