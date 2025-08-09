package Coachable.sorting;


import java.util.Arrays;


public class MergeSortBUAssignment {

	private MergeSortBUAssignment() {
	}

	private static Comparable[] aux;

	private static int count = 0;

	public static void sort(Comparable[] arr) {

		int N = arr.length;
		aux = new Comparable[N];

		for (int sz = 1; sz < N; sz = sz + sz) {

			for (int low = 0; low < N - sz; low += sz + sz) {
				merge(arr, low, low + sz - 1, Math.min(low + sz + sz - 1, N - 1));
				System.out.println("Step: " + (++count) + ". after merging: " + Arrays.toString(arr));
			}
		}
	}

	private static void merge(Comparable[] arr, int low, int mid, int high) {

		if (low >= high) return;
		System.arraycopy(arr, 0, aux, 0, arr.length);

		int i = low, j = mid + 1;

		for (int k = low; k <= high; k++) {
			if (i > mid) arr[k] = aux[j++];
			else if (j > high) arr[k] = aux[i++];
			else if (isLess(aux[i], aux[j])) arr[k] = aux[i++];
			else arr[k] = aux[j++];
		}
	}

	private static boolean isLess(Comparable a, Comparable b) {
		if (a.equals(b)) return false;
		return a.compareTo(b) < 0;
	}

}


