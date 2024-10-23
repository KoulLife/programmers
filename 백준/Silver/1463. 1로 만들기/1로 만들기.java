import java.util.*;

public class Main {

    public static int dp(int n) {
        int[] arr = new int[(n <= 3?4:n+1)];

        arr[1] = 0;
        arr[2] = 1;
        arr[3] = 1;

        for (int i = 4; i <= n; i++) {

            int tmp1 = Integer.MAX_VALUE;
            int tmp2 = Integer.MAX_VALUE;
            int tmp3 = Integer.MAX_VALUE;

            if (i % 3 == 0){
                tmp1 = 1 + arr[i / 3];
            }

            if (i % 2 == 0) {
                tmp2 = 1 + arr[i / 2];
            }

            tmp3 = 1 + arr[i - 1];

            arr[i] = Math.min(Math.min(tmp1, tmp2), tmp3);

        }

        return arr[n];
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        System.out.println(dp(x));

    }
}
