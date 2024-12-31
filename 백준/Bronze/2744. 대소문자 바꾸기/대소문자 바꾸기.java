import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String str = sc.next();
    char[] arr = new char[str.length()];

    for (int i = 0; i < str.length(); i++) {
      if (str.charAt(i) <= 'Z') {
        arr[i] = str.toLowerCase().charAt(i);
      } else {
        arr[i] = str.toUpperCase().charAt(i);
      }
    }
    System.out.println(new String(arr));
  }
}
