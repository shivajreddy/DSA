package leetcode.array;


import java.util.Arrays;

public class Problem238 {

    public static void main(String[] args) {

        Problem238Solution solution = new Problem238Solution();

        solution.productExceptSelf(new int[]{1, 2, 3, 4});
        solution.productExceptSelf(new int[]{2, 5, 3, 4});
        solution.productExceptSelf(new int[]{-1, 1, 0, -3, 3});

    }


}

class Problem238Solution {

    public int[] productExceptSelf(int[] nums) {

        int size = nums.length;
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = 1;
        }

        // forward
        int pre = 1;
        for (int i = 0; i < size; i++) {
            result[i] *= pre;
            pre *= nums[i];
        }
        // System.out.println("pre" + Arrays.toString(result));

        // backward
        int post = 1;
        for (int i = size - 1; i >= 0; i--) {
            result[i] *= post;
            post *= nums[i];
        }
        // System.out.println("post" + Arrays.toString(result));

        return result;
    }

}

