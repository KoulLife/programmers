import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		String[] arr = new String[T];

		for(int i = 0; i < T; i++)
			arr[i] = br.readLine();

		Arrays.sort(arr, new Comparator<String>(){

			@Override
			public int compare(String o1, String o2) {
				if (o1.length() == o2.length()) {
					return o1.compareTo(o2);
				} else {
					return o1.length() - o2.length();
				}
			}
		});

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 0; i < T; i++) {
			if (i != 0 && arr[i].equals(arr[i - 1])) {
				continue;
			}
			bw.write(arr[i] + "\n");
		}
		bw.flush();
	}
}