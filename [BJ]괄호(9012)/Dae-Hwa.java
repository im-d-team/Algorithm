import java.io.*;

class Main {
  private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(final String[] args) throws NumberFormatException, IOException {
    final String[] input = initInput(br);
    final String[] answer = getAnswer(input);
    print(answer);
  }

  static String[] initInput(final BufferedReader br) throws NumberFormatException, IOException {
    final int num = Integer.parseInt(br.readLine());
    final String[] result = new String[num];
    for (int i = 0; i < num; i++) {
      result[i] = br.readLine();
    }

    return result;
  }

  static String[] getAnswer(final String[] input) {
    final String[] result = new String[input.length];
    final String successStr = "YES";
    final String failStr = "NO";
    boolean isVps = true;
    int leftCnt = 0;
    int strLength = 0;
    char cmprValue = 0;

    for (int i = 0; i < input.length; i++) {
      isVps = true;
      leftCnt = 0;
      strLength = input[i].length();
      for (int j = 0; j < strLength; j++) {
        cmprValue = input[i].charAt(j);
        if (cmprValue == '(') {
          leftCnt++;
        } else if (cmprValue == ')') {
          leftCnt--;
        }
        if (leftCnt == -1) {
          isVps = false;
          break;
        }
      }
      if (leftCnt != 0) {
        isVps = false;
      }

      if (isVps) {
        result[i] = successStr;
      } else if (!isVps) {
        result[i] = failStr;
      }
    }

    return result;
  }

  static void print(final String[] input) {
    final StringBuffer sb = new StringBuffer();

    for (int i = 0; i < input.length; i++) {
      sb.append(input[i]);
      sb.append("\n");
    }
    System.out.println(sb.toString());
  }
}

public class Dae-Hwa{}
