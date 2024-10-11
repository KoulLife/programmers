import java.util.*;

public class Main {

  public static int five(char a) {
    int res = 1;
    int n = Integer.parseInt(String.valueOf(a));
    for(int i = 0; i < 5; i++){
      res = res * n;
    }
  
    return res;
  }
  
  public static void main(String[] args){

    Scanner sc = new Scanner(System.in);

    String num = sc.next();
    int res = 0;
    
    for(int i = 0; i < num.length(); i++) {
      res += five(num.charAt(i));
    }

    System.out.println(res);
    
  }
}