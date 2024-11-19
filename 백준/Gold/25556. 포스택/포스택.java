import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i <n ; i++) {
            arr[i] = sc.nextInt();
        }
        
        Stack<Integer>[] stack = new Stack[4];
        for (int i = 0; i < 4; i++) {
            stack[i] = new Stack<>();
        }
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < 4; j++) {
                if(stack[j].isEmpty()||stack[j].peek()<arr[i]){
                    stack[j].push(arr[i]);
                    break;
                }else if(j<3){
                    continue;
                }else{
                    System.out.println("NO");
                    return;
                }
            }
        }
        System.out.println("YES");
    }
}