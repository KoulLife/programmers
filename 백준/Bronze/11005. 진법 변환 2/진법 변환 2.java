import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int B = sc.nextInt();

		String res = "";

		while(N > 0) {
			int tmp = N % B;
			if (tmp < 10) res += tmp;
			else res += (char)(tmp - 10 + 'A');
			N /= B;
		}

		System.out.println(new StringBuilder(res).reverse());

	}
}