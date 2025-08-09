package leetcode.array;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.SortedSet;
import java.util.TreeSet;

import org.junit.Assert;

public class Problem347 {
    public static void main(String[] args) {
        Problem347Solution s = new Problem347Solution();
        Assert.assertEquals(
                Arrays.toString(s.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)),
                Arrays.toString(new int[]{1, 2})
        );
        Assert.assertEquals(
                Arrays.toString(s.topKFrequent(new int[]{1, 2}, 2)),
                Arrays.toString(new int[]{2, 1})
        );
    }
}

class Problem347Solution {

    public int[] topKFrequent(int[] nums, int k) {

        LinkedHashMap<Integer, Integer> hashMap = new LinkedHashMap<>();
        for (int num : nums) {
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        SortedSet<Map.Entry<Integer, Integer>> entrySortedSet = new TreeSet<>(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if (o1.getValue() < o2.getValue()) {
                    return 1;
                }
                return -1;
            }
        });

        entrySortedSet.addAll(hashMap.entrySet());

        int[] result = new int[k];
        Iterator<Map.Entry<Integer, Integer>> iterator = entrySortedSet.iterator();

        int i = 0;
        while (i < k && iterator.hasNext()) {
            int val = iterator.next().getKey();
            result[i] = val;
            i++;
        }
        System.out.println("result = " + Arrays.toString(result));
        return result;

    }
}
