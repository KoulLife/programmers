import java.util.*;

class Solution {
    public int solution(int[] nums) {
        // M1. 배열 길이
        int arrLength = nums.length / 2;
        
        Map<Integer, Integer> hashMap = new HashMap<>();
        
        for (int num : nums){
            hashMap.put(num, 0);
        }
        
        int answer = Math.min(arrLength, hashMap.size());
        
        return answer;
    }
}