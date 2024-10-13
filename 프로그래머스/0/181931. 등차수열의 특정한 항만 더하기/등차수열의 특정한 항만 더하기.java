class Solution {
    public int solution(int a, int d, boolean[] included) {
        
        boolean isFirst = true;
        
        int res = 0;
        
        for(int i = 0; i < included.length; i++){
            if(included[i]){
                res += (a + i * d);
            }
        }
        return res;
    }
}