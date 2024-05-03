package Coachable.sorting;

import java.util.Arrays;


public class QuickSortEntropyAssignment {
	private QuickSortEntropyAssignment() {
	}

	private static int count = 0;

	public static void sort(Comparable[] arr) {
		sort(arr, 0, arr.length - 1);
	}

	private static void sort(Comparable[] arr, int low, int high) {
		if (low >= high) return;

		Comparable pivot = arr[low];
		int i = low, lt = low, gt = high;

		while (i <= gt) {
			if (arr[i].compareTo(pivot) < 0)
				swap(arr, i++, lt++);
			else if (arr[i].compareTo(pivot) > 0)
				swap(arr, i, gt--);
			else i++;
		}
		System.out.println("count: " + (++count) + ". Pivot: " + pivot + ". low: " + low + ". high: " + high + ". i: " + i);
		System.out.println("arr: " + Arrays.toString(arr));
		sort(arr, low, lt - 1);
		sort(arr, gt + 1, high);
	}

	private static void swap(Comparable[] arr, int i, int j) {
		Comparable temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}
}

