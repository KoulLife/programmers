import java.util.*;

public class Main {

    public static int minusNum = 0;
    public static int zeroNum = 0;
    public static int plusNum = 0;

    public static int[][] paper;

    public static void score(int num) {
        if (num == -1){
            minusNum++;
        } else if (num == 0) {
            zeroNum++;
        } else if (num == 1) {
            plusNum++;
        }
    }

    public static void cutPaper(int x1, int x2, int y1, int y2) {

        if (x1 + 1 == x2) {
            score(paper[y1][x1]);
            return;
        }

        int checkNum = paper[y1][x1];
        boolean checkStatus = true;

        for (int y = y1; y < y2; y++) {
            if (checkStatus == false) {
                break;
            }
            for (int x = x1; x < x2; x++) {
                if (checkStatus == false){
                    break;
                }
                if (checkNum != paper[y][x]) {
                    checkStatus = false;
                }
            }
        }

        if (checkStatus == true) {
            score(checkNum);
            return;
        } else {
            int cutX = (x2 - x1) / 3;
            int cutY = (y2 - y1) / 3;

            cutPaper(x1, x1 + cutX, y1, y1 + cutY);
            cutPaper(x1 + cutX, x1 + cutX * 2, y1, y1 + cutY);
            cutPaper(x1 + cutX * 2, x2, y1, y1 + cutY);

            cutPaper(x1, x1 + cutX, y1 + cutY, y1 + cutY * 2);
            cutPaper(x1 + cutX, x1 + cutX * 2, y1 + cutY, y1 + cutY * 2);
            cutPaper(x1 + cutX * 2, x2, y1 + cutY, y1 + cutY * 2);

            cutPaper(x1, x1 + cutX, y1 + cutY * 2, y2);
            cutPaper(x1 + cutX, x1 + cutX * 2, y1 + cutY * 2, y2);
            cutPaper(x1 + cutX * 2, x2, y1 + cutY * 2, y2);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        paper = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                paper[i][j] = sc.nextInt();
            }
        }

        cutPaper(0, n, 0, n);

        System.out.println(minusNum);
        System.out.println(zeroNum);
        System.out.println(plusNum);

    }
}