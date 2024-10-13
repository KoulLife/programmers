class Solution {
    public String solution(int[] numLog) {
        String res = "";
        
        for(int i = 0; i < numLog.length-1; i++){
            int b = numLog[i + 1];
            int a = numLog[i];
            int opt = b-a;
            
            if(opt == 1){
                res+="w";
            }
            else if(opt == -1){
                res+="s";
            }
            else if(opt == 10){
                res+="d";
            }
            else{
                res+="a";
            }
        }
        return res;
    }
}