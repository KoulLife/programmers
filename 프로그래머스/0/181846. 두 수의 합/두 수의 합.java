import java.math.*;

class Solution {
    public String solution(String a, String b) {
        
        BigInteger b1 = new BigInteger(a);
        BigInteger b2 = new BigInteger(b);
        
        BigInteger res = b1.add(b2);
        
        return res.toString();
    }
}