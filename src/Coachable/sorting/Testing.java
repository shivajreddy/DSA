package Coachable.sorting;

import java.util.Arrays;


public class Testing {
	public static void main(String[] args) {

		//Integer[] arr = new Integer[]{10, -20, 0, 12, 5, 17};
		String[] arr = new String[]{"HELP", "IFYO", "UARE", "READ", "INGT", "HISI", "AMTR", "APPE", "DINS", "IDEA", "SORT", "INGA", "LGOR", "ITHM", "OHPL", "EASE", "SEND", "HELP", "RATS", "EVIL", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "HELP", "RATS", "AREW", "WATC", "INGM", "ETYP"};
		System.out.println(Arrays.toString(arr));

		// Using Merge Sort : 29th merge matches B
		MergeSortCopy.sort(arr);

		// Using Quick Sort
		//QuickSort.sort(arr);

		System.out.println(Arrays.toString(arr));
	}
}
