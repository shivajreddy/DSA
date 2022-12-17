package leetcode.binarysearch;

public class Problem704 {
    public static void main(String[] args) {

        Solution s = new Solution();

        System.out.println(s.search(new int[]{-1, 0, 3, 5, 9, 12}, 9));
        System.out.println(s.search(new int[]{-1, 0, 3, 5, 9, 12}, 2));

    }
}


class Solution {
    public int search(int[] nums, int target) {

        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {

            int mid_index = (l + r) / 2;
            int curr_num = nums[mid_index];
            System.out.println("mid_index = " + mid_index + ". curr_num = " + curr_num);

            if (curr_num == target) {
                return mid_index;
            } else if (curr_num < target) {
                l = mid_index + 1;
            } else {
                r = mid_index - 1;
            }

        }

        return -1;

    }
}
