import java.util.*;

class Solution {
    public String[] solution(String[] names) {
        
        ArrayList<String> al = new ArrayList<String>();
        
        for(int i = 0; i < names.length; i++){
            if(i%5==0){
                al.add(names[i]);
            }
        }
        
        String[] res = new String[al.size()];
        
        for(int i = 0; i < al.size(); i++){
            res[i] = al.get(i);
        }
        
        return res;
        
    }
}