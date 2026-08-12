import java.util.*;

class Solution {
    
    public int bfs(int[][] b) {
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        Queue<int[]> q = new ArrayDeque<>();
        
        q.offer(new int[]{0,0,1});
        b[0][0] = 0;
        
        while (!q.isEmpty()) {
            int[] list = q.poll();
            int beforeY = list[0];
            int beforeX = list[1];
            int cnt = list[2];
            
            for (int i =0; i < 4; i++) {
                int x = beforeX + dx[i];
                int y = beforeY + dy[i];
                
                if ( x < 0 || x >= b[0].length ||
                y < 0 || y >= b.length ||
                b[y][x] == 0
              ) {
                continue;
                }            
                else if (x == b[0].length-1 && y == b.length-1){
                    return cnt + 1;
                }            
                else {
                    b[y][x] = 0;
                    q.offer(new int[]{y,x,cnt+1});
                }
            }                        
        }
        return -1;                    
    }
    
    public int solution(int[][] maps) {
        return bfs(maps);
    }
}