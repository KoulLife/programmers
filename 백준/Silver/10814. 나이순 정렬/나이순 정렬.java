import java.util.Arrays;
import java.util.Scanner;

class Users implements Comparable<Users> {

	int age;
	String name;

	public Users(int age, String name) {
		this.age = age;
		this.name = name;
	}

	@Override
	public int compareTo(Users o) {
		return age - o.age;
	}
}

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		Users[] users = new Users[T];

		for(int i = 0; i < T; i++) {
			int age = sc.nextInt();
			String name = sc.next();
			Users user = new Users(age, name);
			users[i] = user;
		}

		Arrays.sort(users);

		for(Users user : users) {
			System.out.println(user.age +  " " + user.name);
		}
	}
}