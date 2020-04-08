import java.io.*;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws Exception {
    // input

    int num = Integer.parseInt(br.readLine()), pointer = 0, answer = 0;
    String[] input = new String[num], stack = new String[10000], alphabets;

    for (int i = 0; i < num; i++) {
      input[i] = br.readLine();
    }

    for (String word : input) {
      stack[0] = null;
      pointer = 0;
      alphabets = word.split("");

      // 홀수로 끝난다면 해당 단어는 좋지 않음
      if (alphabets.length % 2 == 1) {
        continue;
      }

      for (String next : alphabets) {
        // 포인터가 0이고 스택이 비었으면 next 넣어줘야함 무조건
        if (pointer == 0 && stack[0] == null) {
          stack[0] = next;
          continue;
        }
        // 스택에 들어있는게 다음 글자랑 같으면 스택 비워야함
        if (stack[pointer] != null && stack[pointer].equals(next)) {
          stack[pointer] = null;

          if (0 < pointer) {
            pointer--;
          }
          continue;
        }

        if (stack[pointer] != null && !stack[pointer].equals(next)) {
          stack[++pointer] = next;

        }
      }

      // 다 돌고 스택이 비면 좋은 단어
      if (stack[0] == null) {
        answer++;
      }
    }

    System.out.println(answer);
  }
}
