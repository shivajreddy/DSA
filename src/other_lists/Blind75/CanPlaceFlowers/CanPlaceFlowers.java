package CanPlaceFlowers;

import java.util.Arrays;

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        int[] arr = new int[flowerbed.length + 2];
        System.arraycopy(flowerbed, 0, arr, 1, flowerbed.length);

        // System.out.println(Arrays.toString(arr));

        for (int i = 1; i != arr.length - 1; ++i) {
            // System.out.println("checking for " + arr[i - 1] + " " + arr[i] + " " + arr[i + 1]);
            if (arr[i - 1] == 0 && arr[i] == 0 && arr[i + 1] == 0) {
                arr[i] = 1;
                n -= 1;
            }
        }
        // System.out.println(n);
        return n <= 0;
    }
}

public class CanPlaceFlowers {
    public static void main(String[] args) {
        Solution s = new Solution();

        s.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1);

        assert s.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1);

    }
}
