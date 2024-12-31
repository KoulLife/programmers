import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int cnt = 0;

    String str1 = sc.nextLine();
    String str2 = sc.nextLine();

    String result = str1.replace(str2, "K");

    for(int i = 0; i < result.length(); i++) {
      if(result.charAt(i) == 'K') {
        cnt++;
      }
    }
    System.out.println(cnt);
  }
}
