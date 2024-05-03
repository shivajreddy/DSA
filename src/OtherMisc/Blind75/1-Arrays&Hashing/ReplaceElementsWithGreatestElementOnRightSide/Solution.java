package ReplaceElementsWithGreatestElementOnRightSide;

import java.util.Arrays;
import java.util.HashMap;

class Solution {
  public int[] replaceElements(int[] arr) {
    int[] result = new int[arr.length];
    result[arr.length - 1] = -1;

    // 1 element check
    if (arr.length == 1)
      {
      return result;
      }

    // Hashmap to keep track of the highest numbers sequentially
    HashMap<Integer, Integer> hm = new HashMap<>();

    int high = arr[arr.length - 1];
    hm.put(arr.length, -1);

    for (int i = arr.length - 1; i >= 1; --i)
      {
      if (arr[i] > high)
        {
        high = arr[i];
        }
      hm.put(i, high);
      }
    System.out.println(hm);

    for (int key: hm.keySet()){
      result[key-1] = hm.get(key);
    }
    return result;
  }


  //  Run the solution
  public static void main(String[] args) {
    Solution s = new Solution();

    int[] input1 = new int[]{17, 18, 5, 4, 6, 1};
    int[] input2 = new int[]{400};

    int[] result1 = s.replaceElements(input1);
    int[] result2 = s.replaceElements(input2);
    System.out.println(Arrays.toString(result1));
    System.out.println(Arrays.toString(result2));
  }
}
