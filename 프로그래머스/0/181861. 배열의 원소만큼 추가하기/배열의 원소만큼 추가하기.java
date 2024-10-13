import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i = 0; i < arr.length; i++){
            int j = arr[i];
            for(int p = 0; p < j; p++){
                res.add(j);
            }
        }
        
        int[] resArr = new int[res.size()];
        
        for(int i = 0; i < res.size(); i++){
            resArr[i] = res.get(i).intValue();
        }
        
        return resArr;
    }
}