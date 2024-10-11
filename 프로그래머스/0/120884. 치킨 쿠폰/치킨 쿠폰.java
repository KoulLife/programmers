class Solution {
    public int solution(int chicken) {
        
        int coupon = 0;
        int stamp = 0;
        
        for(int i = 1; i <= chicken; i++){
            stamp++;
            if(stamp != 0 && stamp % 10 == 0){
                coupon++;
                stamp++;
            }        
        }
        return coupon;
    }
}