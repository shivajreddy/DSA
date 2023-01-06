package leetcode.array;

import java.util.HashMap;
import java.util.Objects;


public class Problem242 {
    public static void main(String[] args) {

        Problem242Solution solution = new Problem242Solution();
        solution.isAnagram("anagram", "nagaram");
        solution.isAnagram("rat", "car");

    }
}

class Problem242Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> hm_s = new HashMap<>();
        for (Character c : s.toCharArray()) {
            hm_s.put(c, hm_s.getOrDefault(c, 0) + 1);
        }

        HashMap<Character, Integer> hm_t = new HashMap<>();
        for (Character c : t.toCharArray()) {
            hm_t.put(c, hm_t.getOrDefault(c, 0) + 1);
        }

        if (hm_s.size() != hm_t.size()) return false;

        for (Character c : hm_s.keySet()) {
            if (!hm_t.containsKey(c)) return false;

            if (!Objects.equals(hm_s.get(c), hm_t.get(c))) return false;
        }

        return true;

    }
}
