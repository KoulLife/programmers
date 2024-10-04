import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int t = sc.nextInt();
    for(int i = 0; i < t; i++){
      int data = 1;
      int a = sc.nextInt();
      int b = sc.nextInt();
      for(int j = 0; j < b; j++){
        data *= a;
        data %= 10;
      }
      if (data == 0){
        System.out.println(10);
      }
      else{
        System.out.println(data);
      }
    }
  }

}