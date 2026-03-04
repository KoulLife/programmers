import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0; i < commands.length; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            int start = commands[i][0] - 1;
            int j = commands[i][1];
            int k = commands[i][2];
            
            for(int p = start; p < j; p++) {
                list.add(array[p]);
            }
            Collections.sort(list);
            int key = list.get(k - 1);
            answer[i] = key;
        }
        
        return answer;
    }
}