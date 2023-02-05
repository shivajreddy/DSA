package Coachable.sorting;


import java.util.Arrays;


public class HeapSortOld {

	public static void main(String[] args) {


		//int[] arr = new int[]{0, 40, 25, 35, 10, 5, 20, 30};
		//System.out.println(delete(arr, 7));

		//int[] arr = new int[]{0, 30, 10, 20};
		//System.out.println(delete(arr, 3));

		//System.out.println(Arrays.toString(arr));


		String input = "PRIO*R**I*T*Y***QUE***U*E";

		int[] arr = new int[input.length() + 1];
		for (int i = 0; i < input.length(); i++)
			arr[i + 1] = input.charAt(i);

		for (int i = 0; i < input.length(); i++) {
			//System.out.println("now i = " + i);
			// letter
			int curr = input.charAt(i);
			if (curr != 42) {
				//System.out.println("running insert");
				insert(arr, i);
				System.out.println("after insert arr= " + Arrays.toString(arr));
			} else {
				//System.out.println("running delete");
				int deleted = delete(arr, i);
				System.out.println("deleted: " + deleted);
				//i -= 1;
			}
		}
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


	private static int delete(int[] arr, int n) {

		// root goes out of 1-indexed array
		int root = arr[1];
		int last = arr[n];

		arr[1] = last;        // last comes to root
		arr[n] = root;        // first comes to last

		int i = 1;
		int childIdx = i * 2;

		// Re-arrange the last, until it finds place
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

