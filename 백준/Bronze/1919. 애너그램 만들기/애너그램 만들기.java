import java.util.Scanner;

public class Main{

    static int[] calAlphabet(String str) {
        int[] count = new int[26];
        for (int i = 0; i < str.length(); i++) {
            count[str.charAt(i) - 'a']++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();

        // cal Alphabet count
        int[] countStr1 = calAlphabet(str1);
        int[] countStr2 = calAlphabet(str2);

        // get Num
        int res = 0;
        for (int i = 0; i < 26; i++) {
            res += Math.abs(countStr1[i] - countStr2[i]);
        }
        System.out.println(res);
    }
}