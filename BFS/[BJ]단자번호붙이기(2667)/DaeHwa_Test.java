package baekjoon.bfs.proplem_2667;

import java.util.ArrayList;
import java.util.Arrays;

public class DaeHwa_Test {
	public static void main(String[] args) {
		String str = "0110100\r\n" + "0110101\r\n" + "1110101\r\n" + "0000111\r\n" + "0100000\r\n" + "0111110\r\n"
				+ "0111000";

		int n = 7;
		int[][] map = new int[n][];

		String[] slicedStr = str.split("\n");

		for (int i = 0; i < 7; i++) {
			map[i] = Arrays.stream(slicedStr[i].replaceAll("\\s", "").split("")).mapToInt(x -> Integer.parseInt(x))
					.toArray();
		}

		Vertex index = new Vertex(0, 0);

		ArrayList<Integer> resultList = DaeHwa.bfs(map, index);
		resultList.sort(null);

		System.out.println(resultList.size());

		for (int i : resultList) {
			System.out.println(i);
		}
	}
}
