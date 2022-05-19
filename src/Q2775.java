import java.io.*;
import java.util.*;

public class Q2775 {

  public static void main(String[] args) throws Exception {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int count = Integer.parseInt((bf.readLine()));
    int k, n; // 입력값 - 층수, 호수
    int max_k, max_n; // 최댓값 - 층수, 호수
    int[] k_array = new int[count]; // 층수 리스트
    int[] n_array = new int[count]; // 호수 리스트

    for (int i = 0; i < count; i++) {
      k = Integer.parseInt((bf.readLine()));
      k_array[i] = k;
      n = Integer.parseInt((bf.readLine()));
      n_array[i] = n;
    }

    max_k = Arrays.stream(k_array).max().getAsInt(); // 층수 최댓값
    max_n = Arrays.stream(n_array).max().getAsInt(); // 호수 최댓값

    int[][] apt = new int[max_k + 1][max_n + 1];

    for (int j = 0; j <= max_k; j++) {
      apt[j][0] = 1;
    }

    for (int l = 0; l <= max_n; l++) {
      apt[max_k][l] = l + 1;
    }

    for (int floor = max_k - 1; floor >= 0; floor--) {
      for (int room = 1; room <= max_n; room++) {
        apt[floor][room] = apt[floor + 1][room] + apt[floor][room - 1];
      }
    }

    for (int m = 0; m < count; m++) {
      System.out.println(apt[max_k - k_array[m]][n_array[m] - 1]);
    }
  }
}
