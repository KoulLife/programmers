import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        
        ArrayList<String> al = new ArrayList<String>();
        for(int i = 0; i < my_string.length(); i++){
            String tmp = my_string.substring(i,my_string.length());
            al.add(tmp);
        }
        
        al.sort(Comparator.naturalOrder());
        String[] res = new String[al.size()];
        
        for(int i = 0; i < al.size(); i++){
            res[i] = al.get(i);
        }
        
        return res;
        
    }
}