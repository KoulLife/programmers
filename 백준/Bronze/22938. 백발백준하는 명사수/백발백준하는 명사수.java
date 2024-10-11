import java.util.*;

public class Main {

  public static void main(String[] args){

    Scanner sc = new Scanner(System.in);

    int x1 = sc.nextInt();
    int y1 = sc.nextInt();
    int r1 = sc.nextInt();

    int x2 = sc.nextInt();
    int y2 = sc.nextInt();
    int r2 = sc.nextInt();

    double d1 = Math.pow((x1 - x2), 2);
    double d2 = Math.pow((y1 - y2), 2);
    double tmp = Math.sqrt(d1+d2);

    if(tmp < (double)r1+r2){
      System.out.print("YES");
    }
    else{
      System.out.print("NO");
    }
    
    
  }
}
