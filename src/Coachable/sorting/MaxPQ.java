package Coachable.sorting;

public class MaxPQ<Key extends Comparable<Key>> {

	private Key[] pq;
	private int N;


	public MaxPQ(Key[] elements) {
		N = elements.length;
		pq = (Key[]) new Comparable[elements.length + 1];
		addAllKeysToPQ(elements);
	}

	private void addAllKeysToPQ(Key[] keys) {
		for (int i = 0; i < N; i++)
			pq[i + 1] = keys[i];
		for (int k = N / 2; k >= 1; k--)
			sink(k);
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public int getSize() {
		return N;
	}

	// Insert operation
	private void insert(Key newKey) {
		pq[++N] = newKey;
		swim(N);
	}

	// Delete max key operation
	private Key deleteMax() {
		Key max = pq[1];
		swap(1, N--);
		sink(1);
		pq[N + 1] = null;
		return max;
	}

	// Swim operation
	private void swim(int k) {
		while (k > 1 && isLess(k / 2, k)) {
			swap(k, k / 2);
			k = k / 2;
		}
	}

	// Sink operation
	private void sink(int k) {

		while (k * 2 <= N) {
			int j = 2 * k;        // j is the child node index
			if (j < N && isLess(j, j + 1)) j++; // j points to bigger child node
			if (!isLess(k, j)) break;
			swap(k, j);
			k = j;
		}
	}

	// helper methods
	private void swap(int i, int j) {
		Key temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}

	private boolean isLess(int i, int j) {
		if (pq[i].equals(pq[j])) return false;
		return pq[i].compareTo(pq[j]) < 0;
	}


}

