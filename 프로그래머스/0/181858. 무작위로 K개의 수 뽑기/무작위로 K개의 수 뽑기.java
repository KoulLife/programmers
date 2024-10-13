import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        ArrayList<Integer> al = new ArrayList<Integer>();
        
        for(int num:arr){
            if(!al.contains(num)){
                al.add(num);
                k -= 1;
                if(k == 0){
                    break;
                }
            }
        }
        
        if(k > 0){
            for(int i = 0; i < k; i++){
                al.add(-1);
            }
        }
        
        int[] res = new int[al.size()];
        for(int i = 0; i < al.size(); i++){
            res[i] = al.get(i).intValue();
        }
        
        return res;
    }
}