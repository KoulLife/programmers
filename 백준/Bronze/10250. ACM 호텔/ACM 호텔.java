import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		while(T-- > 0) {
			int H = sc.nextInt();
			int W = sc.nextInt();
			int N = sc.nextInt();

			N -= 1;

			int lastNum = N / H + 1;
			int firstNum = N % H + 1;

			System.out.printf("%d%02d\n", firstNum, lastNum);
		}
	}
}