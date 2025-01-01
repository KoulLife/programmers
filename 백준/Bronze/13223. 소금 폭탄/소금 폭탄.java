import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String current = sc.next();
    String drop = sc.next();

    String[] currentUnit = current.split(":");
    int currentHour = Integer.parseInt(currentUnit[0]);
    int currentMinute = Integer.parseInt(currentUnit[1]);
    int currentSecond = Integer.parseInt(currentUnit[2]);
    int currentSecondAmount = currentHour * 3600 + currentMinute * 60 + currentSecond;

    String[] dropUnit = drop.split(":");
    int dropHour = Integer.parseInt(dropUnit[0]);
    int dropMinute = Integer.parseInt(dropUnit[1]);
    int dropSecond = Integer.parseInt(dropUnit[2]);
    int dropSecondAmount = dropHour * 3600 + dropMinute * 60 + dropSecond;

    int needSecond = dropSecondAmount - currentSecondAmount;
    if (needSecond <= 0) {
      needSecond += 24 * 3600;
    }
    int hour = needSecond / 3600;
    int minute = (needSecond % 3600) / 60;
    int second = needSecond % 60;

    System.out.printf("%02d:%02d:%02d", hour, minute, second);

  }
}