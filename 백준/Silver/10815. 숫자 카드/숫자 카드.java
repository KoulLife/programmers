// 5
// 6 3 2 10 -10
// 8
// 10 9 -5 2 3 4 5 -10
import java.util.*;

class Main {

  public static boolean check(int[] arr ,int data) {
    int l = 0;
    int r = arr.length - 1;
    while(l <= r){
      int m = (l + r) / 2;
      if(arr[m] == data) {
        return true;
      } else if(arr[m] > data){
        r = m - 1;
      } else {
        l = m + 1;
      }
    }
    
    return false;
  }
  
  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int[] arrA = new int[n];
    for(int i = 0; i < n; i++) {
      arrA[i] = sc.nextInt();
    }
    Arrays.sort(arrA);

    int n2 = sc.nextInt();
    int[] arrB = new int[n2];
    for(int i = 0; i < n2; i++) {
      arrB[i] = sc.nextInt();
    }

    for(int data : arrB){
      if(check(arrA ,data)){
        System.out.print("1 ");
      } else{
        System.out.print("0 ");
      }
    }
    
  }
}
