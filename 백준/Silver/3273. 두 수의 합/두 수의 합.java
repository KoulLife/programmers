import java.util.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int res = 0;
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int goal = sc.nextInt();

        int left = 0;
        int right = arr.length - 1;

        while(left < right) {
            if (arr[left] + arr[right] < goal) {
                left += 1;
            } else if (arr[left] + arr[right] > goal) {
                right -= 1;
            }

            if (arr[left] + arr[right] == goal) {
                res += 1;
                left += 1;
                right -= 1;
            }
        }
        System.out.println(res);
    }
}
