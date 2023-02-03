package Coachable.sorting;

import java.util.Arrays;


public class Testing {
	public static void main(String[] args) {

		//Integer[] arr = new Integer[]{10, -20, 0, 12, 5, 17};
		int[] arr = new int[]{10, -20, 0, 12, 5, 17};

		//String[] arr = new String[]{"HELP", "IFYO", "UARE", "READ", "INGT", "HISI", "AMTR", "APPE", "DINS", "IDEA", "SORT", "INGA", "LGOR", "ITHM", "OHPL", "EASE", "SEND", "HELP", "RATS", "EVIL", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "HELP", "RATS", "AREW", "WATC", "INGM", "ETYP"};
		System.out.println(Arrays.toString(arr));

		// Using Merge Sort : 29th merge matches B
		//MergeSortAssignment.sort(arr);

		// Using MergeSortBU : 24th step after merge, matches D
		//MergeSortBUAssignment.sort(arr);

		// Using Quick Sort : After setting the 1st pivot: HELP, which goes to idx:9, matches C
		//QuickSortAssignment.sort(arr);

		// Using Quick Sort Entropy: i:10 pivot:HELP, low:0, high:31,
		//QuickSortEntropyAssignment.sort(arr);

		// Insertion Sort
		//InsertionSortAssignment
		InsertionSortIntegers.sort(arr);


		System.out.println(Arrays.toString(arr));
	}
}

