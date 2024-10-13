import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        
        ArrayList<String> arr = new ArrayList<String>();
        String tmp = "";
        
        for(int i = 0; i < myStr.length(); i++) {
            
            char c = myStr.charAt(i);
            
            if(c == 'a' || c == 'b' || c == 'c'){
                if(tmp != ""){
                    arr.add(tmp);
                }
                tmp = "";
            }
            else{
                tmp += String.valueOf(c);
            }
            
        }
        
        if(tmp != ""){
            arr.add(tmp);
        }
        
        if(arr.size() == 0){
            arr.add("EMPTY");
        }
        
        String[] res = new String[arr.size()];
        
        for(int i = 0; i < arr.size(); i++){
            res[i] = arr.get(i);
        }
        
        return res;
        
    }
}