import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    int f = sc.nextInt();
    n = n/100 * 100;
    
    while(true){
      if(n % f == 0){
        break;
      }
      n += 1;
    }

    int res = n % 100;
    if(res < 10){
      System.out.printf("0"+res);
    }
    else{
      System.out.println(res);
    }
  }

}