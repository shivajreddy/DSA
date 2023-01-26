package Coachable;

import java.util.Arrays;


public class InsertionSort {


	public static void main(String[] args) {

		int[] arr = new int[]{-1, 0, 4, 10, 20, 30, 40};

		int[] result = insert(arr, 3);
		result = insert(result, 20);

		System.out.println(Arrays.toString(result));

	}


	private static int[] insert(int[] input, int target) {

		int[] result = Arrays.copyOf(input, input.length + 1);

		int i = input.length - 1;
		while (i >= 0) {

			int curr = input[i];
			if (curr > target) {
				result[i + 1] = curr;
				i -= 1;
			} else {
				result[i + 1] = target;
				return result;
			}
		}

		return result;
	}

}

