import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		Set<String> S = new HashSet<String>();

		for(int i = 0; i < N; i++)
			S.add(sc.next());

		int res = 0;

		for (int i = 0; i < M; i++) {
			String name = sc.next();
			if (S.contains(name))
				res += 1;
		}

		System.out.println(res);

	}
}