import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 층, 부피 입력
		int height = sc.nextInt();
		int width = sc.nextInt();

		char[][] castle = new char[height][width];

		for(int i = 0; i < height; i++) {
			castle[i] = sc.next().toCharArray();
		}

		int heightRes = 0;
		for(int i = 0; i < height; i++) {
			boolean isExist = false;

			for(char c : castle[i]) {
				if (c == 'X') {
					isExist = true;
					break;
				}
			}
			heightRes = (isExist) ? heightRes : heightRes + 1;
		}

		int widthRes = 0;
		for(int j = 0; j < width; j++) {
			boolean isExist = false;

			for(int i = 0; i < height; i++) {
				if(castle[i][j] == 'X'){
					isExist = true;
					break;
				}
			}
			widthRes = (isExist) ? widthRes : widthRes + 1;
		}

		System.out.println(Math.max(heightRes, widthRes));
	}
}
