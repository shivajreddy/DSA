package leetcode.hashmap;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;


public class Problem299 {
	public static void main(String[] args) {
		Solution solution = new Solution();
		//solution.getHint("1807", "7810");
		//solution.getHint("1123", "0111");
		solution.getHint("011", "110");
	}
}


/***************************************************************************
 Input: secret = "1807", guess = "7810"
 Output: "1A3B"

Input: secret = "1123", guess = "0111"
Output: "1A1B"
 ***************************************************************************/

class Solution {
	public String getHint(String secret, String guess) {

		int N = secret.length();
		HashMap<Character, Integer> map = new HashMap<>();

		for (int i = 0; i < N; i++) {
			char c = secret.charAt(i);
			if (map.containsKey(c)) map.put(c, map.get(c) + 1);
			else map.put(c, 1);
		}
		System.out.println(map);

		int bulls = 0, cows = 0;

		for (int i = 0; i < N; i++) {
			char c = guess.charAt(i);
			if (map.containsKey(c) && secret.charAt(i) == c){
				bulls++;
				map.put(c, map.get(c) - 1);
				if (map.get(c) == 0) map.remove(c);
			}
			//System.out.println("map: " + map);
		}
		for (int i = 0; i < N; i++) {
			char c = guess.charAt(i);
			if (map.containsKey(c) && secret.charAt(i) != c) {
				cows++;
				map.put(c, map.get(c) - 1);
				if (map.get(c) == 0) map.remove(c);
			}
			//System.out.println("map: " + map);
		}

		StringBuilder result = new StringBuilder().append(bulls).append("A").append(cows).append("B");
		System.out.println(result.toString());
		return result.toString();
	}
}