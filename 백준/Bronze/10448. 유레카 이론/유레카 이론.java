import java.util.*;

public class Main {

	public static int sumThree(int i) {
		return i * (i + 1) / 2;
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		while(T-- > 0) {
			int num = sc.nextInt();

			int wall = 0;
			boolean isSame = false;
			
			for(int i = 0; i < num; i++) {
				if((i * (i + 1) / 2) >= num) {
					wall = i - 1;
					break;
				}
			}

			for(int i = 1; i <= wall; i++) {
				for(int j = 1; j <= wall; j++) {
					for(int k = 1; k <= wall; k++) {
						if((sumThree(i) + sumThree(j) + sumThree(k)) == num) {
							isSame = true;
							break;
						}
					}
					if(isSame) break;
				}
				if (isSame) break;
			}

			if (isSame) {
				System.out.println(1);
			} else {
				System.out.println(0);
			}
			
		}

	}
}