import java.util.*;

public class Main {

    public static int numOfZero = 0;
    public static int numOfOne = 0;
    public static int[][] arr;

    public static void paper(int x1, int x2, int y1, int y2) {
        int elem = arr[y1][x1];
        boolean isSame = true;

        if (x1 == x2) {
            if (elem == 0){
                numOfZero++;
            } else {
                numOfOne++;
            }
            return;
        }

        for (int i = y1; i <= y2; i++) {
            for (int j = x1; j <= x2; j++) {
                if (arr[i][j] != elem){
                    isSame = false;
                    break;
                }
                if (!isSame){break;}
            }
            if (!isSame){break;}
        }

        if (isSame) {
            if (elem == 0){
                numOfZero++;
            } else {
                numOfOne++;
            }
            return;
        }

        int midX = (x1 + x2) / 2;
        int midY = (y1 + y2) / 2;

        paper(x1, midX, y1, midY);
        paper(midX + 1, x2, y1, midY);
        paper(x1, midX, midY + 1, y2);
        paper(midX + 1, x2, midY + 1, y2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        arr = new int[n][n];

        for(int i = 0; i < n; i ++) {
            for(int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        paper(0, arr.length - 1, 0, arr.length - 1 );
        System.out.println(numOfZero);
        System.out.println(numOfOne);

    }
}