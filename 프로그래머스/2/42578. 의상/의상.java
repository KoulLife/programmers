import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String[] c : clothes) {            
            if (map.containsKey(c[1])) {
                map.put(c[1], map.get(c[1]) + 1);
            } else {                
                map.put(c[1], 2);
            }
        }
        
        int answer = 1;
        
        for(HashMap.Entry<String, Integer> val : map.entrySet()) {
            answer *= val.getValue();
        }
        
        
        return answer - 1;
    }
}