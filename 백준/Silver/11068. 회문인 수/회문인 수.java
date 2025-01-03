import java.util.*;

public class Main {

	public static boolean isPalindrome(String str) {
		char[] cArr = str.toCharArray();
		int l = 0;
		int r = cArr.length - 1;

		boolean res = true;

		while(l < r) {
			if (cArr[l] != cArr[r]){
				res = false;
				break;
			}
			l++;
			r--;
		}

		return res;
	}

	public static String formatting(int N, int i) {
		String ans = "";

		while(N > 0) {
			int tmp = N % i;
			if (tmp < 10) ans += tmp;
			else ans += (char)(tmp - 10 + 'A');
			N /= i;
		}

		return ans;
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		while(T-- > 0) {

			int res = 0;
			int N = sc.nextInt();

			for(int i = 2; i <= 64; i++) {

				String ans = formatting(N, i);

				if(isPalindrome(ans)){
					res = 1;
					break;
				}
			}

			System.out.println(res);
		}
	}
}