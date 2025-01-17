import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int Q = sc.nextInt();

		int[] arr = new int[N + 1];
		int[] acc = new int[N + 1];

		for(int i = 1; i <= N; i++)
			arr[i] = sc.nextInt();

		for(int i = 1; i <= N; i++)
			acc[i] = arr[i] ^ acc[i - 1];

		int ans = 0;

		while (Q-- > 0) {
			int i = sc.nextInt();
			int j = sc.nextInt();

			ans ^= acc[j] ^ acc[i - 1];
		}

		System.out.println(ans);
		
	}
}