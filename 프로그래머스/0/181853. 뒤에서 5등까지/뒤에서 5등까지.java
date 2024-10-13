import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        
        ArrayList<Integer> al = new ArrayList<Integer>();
        
        for(int num:num_list){
            al.add(num);
        }
        
        al.sort(Comparator.naturalOrder());
        
        int[] res = new int[5];
        
        for(int i = 0; i < 5; i++){
            res[i] = al.get(i).intValue();
        }
        return res;
    }
}