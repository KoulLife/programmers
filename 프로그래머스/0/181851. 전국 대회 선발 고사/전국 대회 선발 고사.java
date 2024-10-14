import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < rank.length; i++) {
            if(attendance[i]){
                hm.put(rank[i], i);
            }
        }
        
        Arrays.sort(rank);
        
        int[] resArr = new int[3];
        int cnt = 0;
        
        for(int i = 0; i < rank.length; i++){
            if(cnt >= 3) break;
            if(hm.containsKey(rank[i])){
                resArr[cnt] = hm.get(rank[i]);
                cnt++;
            }
        }
        
        return 10000 * resArr[0] + 100 * resArr[1] + resArr[2];
        
        
    }
}