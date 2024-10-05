import java.util.*;

public class Main {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    Dictionary<String, Integer> dic= new Hashtable<>();
    dic.put("black", 0);
    dic.put("brown", 1);
    dic.put("red", 2);
    dic.put("orange", 3);
    dic.put("yellow", 4);
    dic.put("green", 5);
    dic.put("blue", 6);
    dic.put("violet", 7);
    dic.put("grey", 8);
    dic.put("white", 9);

    String col1 = sc.next();
    String col2 = sc.next();
    String col3 = sc.next();    
    
    long res = 10 * dic.get(col1) + dic.get(col2);

    for(int k = 0; k < dic.get(col3); k++) {
      res *= 10;
    }
    System.out.println(res);
  }
}