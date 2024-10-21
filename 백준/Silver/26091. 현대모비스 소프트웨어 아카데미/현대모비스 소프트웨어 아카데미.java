import java.util.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int res = 0;
        int left = 0;
        int right = arr.length - 1;

        while(left < right) {
            if (arr[left] + arr[right] >= m) {
                res++;
                left += 1;
                right -= 1;
            }
            else if (arr[left] + arr[right] < m) {
                left += 1;
            }
        }
        System.out.println(res);
    }
}