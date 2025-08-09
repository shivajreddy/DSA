package leetcode.array;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Set;
import java.util.TreeMap;

public class Problem128 {
    public static void main(String[] args) {
        Problem128Solution solution = new Problem128Solution();
        solution.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2});
        solution.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1});
    }
}


class Problem128Solution {

    public int longestConsecutive(int[] nums) {

        if (nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int result = 1;

        for (int num : nums) {
            if (!set.contains(num -1)){
                int count = 1;
                while (set.contains(num+1)){
                    num++;
                    count++;
                }
                result = Math.max(result, count);
            }
        }
        System.out.println("result = " + result);
        return result;
    }

}

