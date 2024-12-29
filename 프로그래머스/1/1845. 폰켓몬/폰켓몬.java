import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        int half = nums.length / 2;
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int num : nums) {
            if(!list.contains(num)) {
                list.add(num);
            }
        }
        
        return Math.min(half,list.size());
        
    }
}