import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String str1 = sc.next();
    String str2 = sc.next();
    String res = "";

    for (int i = 0; i < str2.length(); i++) {
      char[] ch = new char[1];
      ch[0] = str2.charAt(i);

      if (str1.contains(new String(ch))) {
        int idx = str1.indexOf(ch[0]);
        str1 = str1.substring(0, idx) + str1.substring(idx + 1, str1.length());
      } else {
        res += new String(ch);
      }
    }
    System.out.println(res.length() + str1.length());
  }
}