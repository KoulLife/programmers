class Solution {
    public int[] solution(int[] num_list) {
        int b = num_list[num_list.length-1];
        int a = num_list[num_list.length-2];
        int tmp = 0;
        if(b-a > 0){
            tmp = b - a;
        }
        else{
            tmp = b*2;
        }
        int[] res = new int[num_list.length+1];
        for(int i = 0; i < num_list.length; i++){
            res[i] = num_list[i];
        }
        res[num_list.length] = tmp;
        return res;
    }
}