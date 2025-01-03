import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		while(T-- > 0) {
			int[] arr = new int[7];

			int sum = 0;
			int minNum = 100;

			for(int i = 0; i < 7; i++)
				arr[i] = sc.nextInt();

			for(int n : arr) {
				if(n % 2 == 0) {
					sum += n;
					minNum = Math.min(minNum, n);
				}
			}

			System.out.println(sum + " " + minNum);
		}

	}
}