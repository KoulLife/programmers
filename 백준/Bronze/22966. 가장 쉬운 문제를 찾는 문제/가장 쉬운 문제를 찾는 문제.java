import java.util.*;

public class Main {

  public static void main(String[] args){

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    int[] score = new int[n];
    String[] prob = new String[n];

    for(int i = 0; i < n; i++){
      prob[i] = sc.next();
      score[i] = sc.nextInt();
    }

    int min = score[0];
    int idx = 0;
    
    for(int i = 1; i < n; i++) {
      if(score[i] <= min){
        idx = i;
        min = score[i];
      }
    }
    System.out.println(prob[idx]);
  }
}
