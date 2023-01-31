package Coachable.sorting;

import java.util.Arrays;


public class ProblemQuickSort {
	static int count = 0;
	static String[][] output = {
			{"AMTR", "APPE", "DINS", "EASE", "HELP", "HISI", "IDEA", "IFYO", "INGA", "INGT", "ITHM", "LGOR", "OHPL", "READ", "SORT", "UARE", "EVIL", "HELP", "MALL", "OVER", "RATS", "RATS", "SEND", "SWAR", "AREW", "ETYP", "HELP", "INGM", "LACE", "RATS", "THEP", "WATC"},
			{"EASE", "ETYP", "AREW", "HELP", "EVIL", "HELP", "AMTR", "APPE", "DINS", "HELP", "SORT", "INGA", "LGOR", "ITHM", "OHPL", "IDEA", "SEND", "HISI", "RATS", "INGT", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "READ", "RATS", "UARE", "WATC", "INGM", "IFYO"},
			{"HELP", "IFYO", "READ", "UARE", "AMTR", "APPE", "HISI", "INGT", "DINS", "IDEA", "INGA", "SORT", "EASE", "ITHM", "LGOR", "OHPL", "EVIL", "HELP", "RATS", "SEND", "MALL", "OVER", "RATS", "SWAR", "HELP", "LACE", "RATS", "THEP", "AREW", "ETYP", "INGM", "WATC"},
			{"DINS", "ETYP", "AMTR", "APPE", "HELP", "HELP", "AREW", "EASE", "HELP", "IDEA", "HISI", "EVIL", "LACE", "IFYO", "INGT", "INGA", "RATS", "INGM", "ITHM", "RATS", "SEND", "LGOR", "MALL", "RATS", "THEP", "SWAR", "OHPL", "READ", "UARE", "WATC", "OVER", "SORT"},
			{"AMTR", "APPE", "DINS", "HELP", "HISI", "IDEA", "IFYO", "INGA", "INGT", "READ", "SORT", "UARE", "LGOR", "ITHM", "OHPL", "EASE", "SEND", "HELP", "RATS", "EVIL", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "HELP", "RATS", "AREW", "WATC", "INGM", "ETYP"},
			{"WATC", "SWAR", "UARE", "SEND", "SORT", "THEP", "RATS", "READ", "RATS", "RATS", "MALL", "OVER", "LGOR", "ITHM", "OHPL", "ETYP", "APPE", "HELP", "DINS", "EVIL", "IDEA", "INGT", "IFYO", "HISI", "INGA", "LACE", "HELP", "HELP", "AREW", "AMTR", "INGM", "EASE"},
			{"AMTR", "APPE", "AREW", "DINS", "EASE", "ETYP", "EVIL", "HELP", "HELP", "HELP", "HISI", "IDEA", "LGOR", "ITHM", "OHPL", "INGT", "SEND", "IFYO", "RATS", "READ", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "INGA", "RATS", "UARE", "WATC", "INGM", "SORT"},
			{"ETYP", "AREW", "EVIL", "AMTR", "APPE", "DINS", "EASE", "HELP", "HELP", "HELP", "INGA", "LGOR", "ITHM", "OHPL", "SORT", "SEND", "IDEA", "RATS", "HISI", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "INGT", "RATS", "READ", "WATC", "INGM", "UARE", "IFYO"},
			{"AMTR", "APPE", "AREW", "DINS", "EASE", "ETYP", "EVIL", "HELP", "HELP", "HELP", "HISI", "IDEA", "IFYO", "INGA", "INGM", "INGT", "ITHM", "LACE", "LGOR", "MALL", "OHPL", "OVER", "RATS", "RATS", "RATS", "READ", "SEND", "SORT", "SWAR", "THEP", "UARE", "WATC"}
	};


	public static void main(String[] args) {

		String[] arr = {"HELP", "IFYO", "UARE", "READ", "INGT", "HISI", "AMTR", "APPE", "DINS", "IDEA", "SORT", "INGA", "LGOR", "ITHM", "OHPL", "EASE", "SEND", "HELP", "RATS", "EVIL", "RATS", "SWAR", "MALL", "OVER", "THEP", "LACE", "HELP", "RATS", "AREW", "WATC", "INGM", "ETYP"};

		System.out.println(Arrays.toString(arr));

		QuickSort(arr, 0, arr.length - 1);
		System.out.println(Arrays.toString(arr));


	}

	private static boolean check(String[] input) {
		for (String[] column : output) {
			System.out.println(Arrays.toString(column));
			System.out.println(Arrays.toString(input));
			System.out.println("------------");
			//for (int i = 0; i < column.length; i++) {
			//	String word = column[i];
			//	if (!Objects.equals(word, input[i])) return false;
			//}
		}
		return true;
	}

	private static void QuickSort(String[] arr, int low, int high) {

		if (low >= high) return;

		int partitionIdx = partition(arr, low, high);
		System.out.println("PASS:" + ++count + ", pivot = " + partitionIdx + ": " + arr[partitionIdx]);
		System.out.println("now arr= " + Arrays.toString(arr));
		//System.out.println("----");
		//System.out.println(check(arr));
		//check(arr);
		QuickSort(arr, low, partitionIdx - 1);
		QuickSort(arr, partitionIdx + 1, high);
	}

	private static int partition(String[] arr, int low, int high) {

		String pivot = arr[low];
		int i = low;
		int j = high + 1;


		while (true) {

			do {
				i++;
				if (i > high) break;
				//} while (isLess(arr[i], pivot));
			} while (arr[i].compareTo(pivot) < 0);

			do {
				j--;
				if (j < low) break;
			} while (arr[j].compareTo(pivot) > 0);
			//} while (isLess(pivot, arr[j]));

			if (i >= j) break;

			exchange(arr, i, j);
		}
		exchange(arr, low, j);
		return j;
	}

	private static void exchange(Object[] arr, int i, int j) {
		Object temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}

	private static boolean isLess(String a, String b) {
		if (a.equals(b)) return false;
		return a.compareTo(b) < 0;
	}
}
