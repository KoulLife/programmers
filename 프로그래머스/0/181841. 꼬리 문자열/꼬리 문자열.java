class Solution {
    public String solution(String[] str_list, String ex) {
        
        String ans = "";
        
        for(String str : str_list){
            if(!(str.contains(ex))){
                ans += str;
            }
        }
        return ans;
    }
}