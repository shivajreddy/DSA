package leetcode.array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Problem49 {
    public static void main(String[] args) {
        Problem49Solution solution = new Problem49Solution();
        solution.groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});
        solution.groupAnagrams(new String[]{""});
        solution.groupAnagrams(new String[]{"a"});
        solution.groupAnagrams(new String[]{"ddddddddddg","dgggggggggg"});
        solution.groupAnagrams(new String[]{"bdddddddddd","bbbbbbbbbbc"});
    }
}

class Problem49Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // this string is key in hashmap, with value of it being an array of indexes
        HashMap<String, List<String>> hashMap = new HashMap<>();
        for (String currWord : strs) {
            String frequencyString = createFrequencyString(currWord);
            List<String> sameWords;
            if (hashMap.containsKey(frequencyString)) {
                sameWords = hashMap.get(frequencyString);
            } else {
                sameWords = new ArrayList<>();
            }
            sameWords.add(currWord);
            hashMap.put(frequencyString, sameWords);
        }
        var result = hashMap.values().stream().toList();
        System.out.println("result=" + result);
        return result;
    }

    // make a frequency-map string. Ex: "abc" -> "111000000000000000000000"
    private String createFrequencyString(String word) {
        int[] letterCount = new int[26];
        for (Character c : word.toCharArray()) {
            // indexes -> [a,b,c...z] = [0,1,2...26]
            // ascii code of 'a' = 97
            letterCount[c - 97] += 1;   // increase the letter count
        }
        StringBuilder sb = new StringBuilder();
        for (int i : letterCount) {
            sb.append(i);
            // when you add "10", and need separation if next is "0"
            sb.append("-");
        }
        // System.out.println(sb.toString());
        return sb.toString();
    }
}
