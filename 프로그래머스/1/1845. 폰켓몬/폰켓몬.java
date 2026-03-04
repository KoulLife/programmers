import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        int maxNum = nums.length / 2;
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {            
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int res = Math.min(maxNum, map.size());
        
        return res;
    }
}