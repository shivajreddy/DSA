package Coachable.sorting;

public class QuickSortEntropyIntegers {

	private QuickSortEntropyIntegers() {
	}

	public static void sort(int[] arr) {
		sort(arr, 0, arr.length - 1);
	}

	private static void sort(int[] arr, int low, int high) {
		if (low >= high) return;

		int pivot = arr[low];

		int lt = low, gt = high, i = low;

		while (i <= gt) {
			if (arr[i] < pivot) {
				swap(arr, lt, i);
				lt++;
				i++;
			}
			else if (arr[i] > pivot) {
				swap(arr, gt, i);
				gt--;
			} else {
				i ++;
			}
		}
		sort(arr, low, lt - 1);
		sort(arr, gt + 1, high);
	}

	private static void swap(int[] arr, int i, int j) {
		int temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}
}

