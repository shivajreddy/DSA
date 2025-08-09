package leetcode.array;

public class Problem75 {
    public static void main(String[] args) {
        Problem75Solution solution = new Problem75Solution();
        solution.sortColors(new int[]{2, 0, 2, 1, 1, 0});
        solution.sortColors(new int[]{2, 0, 1});
    }
}

class Problem75Solution {
    public void sortColors(int[] nums) {

        // order -> 0, 1, 2
        System.out.println("Hi");

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
        }
    }
}

