import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashMap;
import java.util.Map;

class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private final static String BLANK = " ";

  public static void main(String[] args) throws IOException {
    String input1 = br.readLine();
    String[] cardList = br.readLine().split(" ");
    String input3 = br.readLine();
    String[] matchingCardList = br.readLine().split(" ");

    Map<String, Integer> cardCountMap = new LinkedHashMap<>();

    for (String card : cardList) {
      cardCountMap.putIfAbsent(card, 0);
      cardCountMap.computeIfPresent(card, (key, val) -> ++val);
    }

    StringBuilder sb = new StringBuilder();

    for (String matchingCard : matchingCardList) {
      Integer cnt = cardCountMap.get(matchingCard);

      sb.append(cnt == null ? 0 : cnt).append(BLANK);
    }

    System.out.println(sb);
  }
}
