import java.util.*;

class Main {

  public static boolean check(int[] arr, int data) {
    int left = 0;
    int right = arr.length - 1;

    while(left <= right) {
      int mid = (left + right) / 2;
      if(arr[mid] == data) {
        return true;
      }
      else if (arr[mid] < data) {
        left = mid + 1;
      }
      else {
        right = mid - 1;
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

    int[] res = new int[n2];

    for(int i = 0; i < n2; i++) {
      if(check(arrA, arrB[i])){
        res[i] = 1;
      } else{
        res[i] = 0;
      }
    }

    for(int r : res) {
      System.out.println(r);
    }
    
  }
}
