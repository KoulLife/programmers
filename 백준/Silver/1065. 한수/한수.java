import java.util.*;

public class Main {

  public static boolean test(int n){
    boolean b = false;
    int diff = 0;
    String str = ""+n;

    if(n < 10){return true;}
    
    for(int i = 0; i < str.length()-1; i++){
      char first = str.charAt(i);
      char second = str.charAt(i + 1);
      
      if(i == 0){
        diff = Integer.parseInt(String.valueOf(second)) - Integer.parseInt(String.valueOf(first));
        b = true;
      }
      
      else{
        if(diff != 
           (
             Integer.parseInt(String.valueOf(second)) - Integer.parseInt(String.valueOf(first))
           )) {
          b=false;
          break;
        }
      }
    }
    
    return b;
  }

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    int cnt = 0;
    for(int i = 1; i <= n; i++){
      if(test(i) == true) cnt++;
    }
  System.out.println(cnt);
  }
}
