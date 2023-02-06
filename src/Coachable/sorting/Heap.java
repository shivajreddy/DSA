package Coachable.sorting;

import java.util.Arrays;


public class Heap {

	private Heap() {
	}

	private static int count = 0;

	public static void sort(Comparable[] pq) {
		int n = pq.length;

		// heapify phase
		for (int k = n / 2; k >= 1; k--)
			sink(pq, k, n);

		System.out.println("step: " + (++count));
		System.out.println(Arrays.toString(pq));

		// sortdown phase
		int k = n;
		while (k > 1) {
			exch(pq, 1, k--);
			sink(pq, 1, k);
		}
	}

	/***************************************************************************
	 * Helper functions to restore the heap invariant.
	 ***************************************************************************/

	private static void sink(Comparable[] pq, int k, int n) {
		while (2 * k <= n) {
			int j = 2 * k;
			if (j < n && less(pq, j, j + 1)) j++;
			if (!less(pq, k, j)) break;
			exch(pq, k, j);
			k = j;
		}
	}

	/***************************************************************************
	 * Helper functions for comparisons and swaps.
	 * Indices are "off-by-one" to support 1-based indexing.
	 ***************************************************************************/
	private static boolean less(Comparable[] pq, int i, int j) {
		return pq[i - 1].compareTo(pq[j - 1]) < 0;
	}

	private static void exch(Object[] pq, int i, int j) {
		Object swap = pq[i - 1];
		pq[i - 1] = pq[j - 1];
		pq[j - 1] = swap;
	}

}

