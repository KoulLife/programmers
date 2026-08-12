import java.util.*;

class Solution {
    public int bfs(char[][] room, List<int[]> pList) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        for(int[] p : pList) {
            int startY = p[0];
            int startX = p[1];
            
            char[][] cRoom = new char[room.length][];
            
            for (int i = 0; i < room.length; i++) {
                cRoom[i] = room[i].clone();
            }

            Queue<int[]> q = new ArrayDeque<>();
            
            q.offer(new int[]{startY, startX, 0});
            
            cRoom[startY][startX] = 'X';
            
            while (!q.isEmpty()) {

                int[] cur = q.poll();

                int y = cur[0];
                int x = cur[1];
                int cnt = cur[2];

                // 맨해튼 거리 2까지만 확인
                if (cnt >= 2) {
                    break;
                }

                for (int i = 0; i < 4; i++) {

                    int afterY = y + dy[i];
                    int afterX = x + dx[i];

                    // 범위 밖이거나
                    // 파티션 또는 이미 방문한 곳이라면
                    if (
                        afterY < 0 || afterY >= cRoom.length ||
                        afterX < 0 || afterX >= cRoom[0].length ||
                        cRoom[afterY][afterX] == 'X'
                    ) {
                        continue;
                    }

                    // 다른 사람이 발견됨
                    if (cRoom[afterY][afterX] == 'P') {
                        return 0;
                    }

                    // 방문 처리
                    cRoom[afterY][afterX] = 'X';

                    q.offer(new int[]{
                        afterY,
                        afterX,
                        cnt + 1
                    });
                }
            }
        }

        return 1;
    }
    
    public int[] solution(String[][] places) {
        int[] res = new int[5];
        
        for (int i = 0; i < 5; i++) {
            String[] place = places[i];
            
            char[][] room = new char[5][];
            
            for (int j = 0; j < 5; j++) {
                room[j] = place[j].toCharArray();
            }
            
            List<int[]> pList = new ArrayList<>();
            
            for (int y = 0; y < 5; y++) {
                for (int x = 0; x < 5; x++) {
                    if (room[y][x] == 'P') {
                        pList.add(new int[]{y,x});
                    }
                }
            }
            res[i] = bfs(room, pList);
        }
        return res;
    }
}