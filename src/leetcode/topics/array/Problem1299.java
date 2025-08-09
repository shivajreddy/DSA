package leetcode.array;

public class Problem1299 {
}


class Problem1299Solution {
    public int[] replaceElements(int[] arr) {

        int size = arr.length;
        int[] result = new int[size];
        int max = 0;
        for (int i = size - 1; i >= 0; i--) {
            int num = arr[i];
            max = Math.max(max, num);
            result[i] = max;
        }
        result[size - 1] = -1;
        return result;
    }
}
