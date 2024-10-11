class Solution {
    public String solution(String myString, String pat) {
        
        String res = "";
        int strLen = myString.length();
        int patLen = pat.length();
        
        for(int i = strLen - 1; i >= 0; i--) {
            String str = myString.substring(0, i + 1);
            if(str.endsWith(pat)){
                res = str;
                break;
            }
        }
        
        return res;
        
    }
}