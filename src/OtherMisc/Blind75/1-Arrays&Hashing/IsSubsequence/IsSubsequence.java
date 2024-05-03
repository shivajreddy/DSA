package IsSubsequence;

public class IsSubsequence {
  Solution s = new Solution();
}

class Solution {
  public boolean isSubsequence(String s, String t) {

    int p1 = 0;
    int p2 = 0;

    while (p1 < s.length() && p2 < t.length())
      {
      if (t.charAt(p2) == s.charAt(p1))
        {
        p1++;
        }
      p2++;
      }

    return p1 == s.length();
  }
}
