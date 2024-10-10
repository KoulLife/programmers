import java.util.*;

public class Main {

  public static int test(int n) {
    int sum = n;
    while(n != 0){
      sum += n%10;
      n = n/10;
    }
    return sum;
  }

  public static void main(String[] args) {

    boolean[] check = new boolean[10001];

    for(int i = 1; i < 10001; i++) {
      int tmp = test(i);
      
      if(tmp <= 10000)
          check[tmp] = true;
    }

    StringBuilder sb = new StringBuilder();

    for(int i = 1; i <= 10000; i++){
      if(!check[i]){
        sb.append(i).append('\n');
      }
    }

    System.out.println(sb);
    
  }  
}
