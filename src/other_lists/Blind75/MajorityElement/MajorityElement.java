package MajorityElement;

import java.util.HashMap;

class Solution {
    public int majorityElement(int[] nums) {

        int major = nums.length / 2;

        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int num : nums) {
            if (hm.containsKey(num)) {
                hm.put(num, hm.get(num) + 1);
            } else {
                hm.put(num, 1);
            }
            if (hm.get(num) > major) {
                return num;
            }
        }
        return -1;
    }
}


public class MajorityElement {
    public static void main(String[] args) {
        Solution solution = new Solution();
        assert solution.majorityElement(new int[]{2, 2, 1, 1, 1, 2, 2}) == 3;
        assert solution.majorityElement(new int[]{3, 2, 3}) == 2;
    }
}
