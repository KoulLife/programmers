import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int days = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < days; i++) {
            sum += arr[i];
        }
        maxSum = Math.max(maxSum, sum);

        for (int i = days; i < n; i++) {
            sum += arr[i];
            sum -= arr[i - days];
            maxSum = Math.max(sum, maxSum);
        }

        System.out.println(maxSum);

    }
}
