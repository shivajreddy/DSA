package leetcode.array;

public class Problem14 {
    public static void main(String[] args) {
        Problem14Solution solution = new Problem14Solution();
        solution.longestCommonPrefix(new String[]{"flower", "flow", "flight"});
        solution.longestCommonPrefix(new String[]{""});
        solution.longestCommonPrefix(new String[]{"dog", "racecar", "car"});
    }
}

class Problem14Solution {
    public String longestCommonPrefix(String[] strs) {

        StringBuilder sb = new StringBuilder("");
        String smallWord = strs[0];

        for (int i = 0; i < smallWord.length(); i++) {

            for (String word : strs) {
                if (word.length() == i || word.charAt(i) != smallWord.charAt(i)) {
                    System.out.println("result=" + sb.toString());
                    return sb.toString();
                }
            }
            sb.append(smallWord.charAt(i));
        }
        System.out.println("result=" + sb.toString());
        return sb.toString();
    }
}

