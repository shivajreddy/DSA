package LengthOfLastWord;

public class LengthOfLastWord {

}

class Solution {
  public int lengthOfLastWord(String s) {

    int i = s.length()-1, length = 0;

    while (s.charAt(i) == ' ')
      {
      i--;
      }
    while (i >= 0 && s.charAt(i) != ' ')
      {
      i--;
      length++;
      }
    return length;


  }
}
