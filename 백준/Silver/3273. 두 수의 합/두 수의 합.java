import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int lenOfArr = sc.nextInt();
		int[] arr = new int[lenOfArr];
		for(int i = 0; i < lenOfArr; i++) {
			arr[i] = sc.nextInt();
		}
		int goalVal = sc.nextInt();

		boolean[] checkVal = new boolean[1000001];

		for (int num : arr) {
			checkVal[num] = true;
		}

		int res = 0;
		for (int num : arr) {
			int pairNum = goalVal - num;
			if (0 <= pairNum && pairNum <= 1000000 && checkVal[pairNum]) {
				res += 1;
			}
		}

		System.out.println(res/2);
	}
}
