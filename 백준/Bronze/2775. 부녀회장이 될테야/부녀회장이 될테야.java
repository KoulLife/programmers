import java.util.*;

public class Main {

    public static int dp(int k, int n) {
        int[][] apt = new int[k + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            apt[0][i] = i;
        }

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++){
                if (j == 1) {
                    apt[i][j] = 1;
                } else {
                    apt[i][j] = apt[i - 1][j] + apt[i][j - 1];
                }
            }
        }

        return apt[k][n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            System.out.println(dp(k, n));
        }
    }
}
