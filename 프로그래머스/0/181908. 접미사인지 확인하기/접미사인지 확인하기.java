class Solution {
    public int solution(String my_string, String is_suffix) {
       
        boolean res = true;
        int strLen = my_string.length() - 1;
        int sufLen = is_suffix.length() - 1;
        
        if(strLen < sufLen)
            res = false;
        else
            for(int i = sufLen; i >= 0; i--){
                if(my_string.charAt(strLen) != is_suffix.charAt(sufLen)){
                    res = false;
                    break;
                }
                strLen--;
                sufLen--;                
            }
        if(res == true){
            return 1;
        }
        else{
            return 0;
        }
        
    }
}