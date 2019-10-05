package baekjoon.bfs.proplem_2667;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class DaeHwa {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] map = new int[n][];
		for (int i = 0; i < n; i++) {
			map[i] = Arrays.stream(br.readLine().split("")).mapToInt(x -> Integer.parseInt(x)).toArray();
		}

		Vertex index = new Vertex(0, 0);

		ArrayList<Integer> resultList = bfs(map, index);
		resultList.sort(null);

		System.out.println(resultList.size());

		for (int i : resultList) {
			System.out.println(i);
		}
	}

	public static ArrayList<Integer> bfs(int[][] map, Vertex index) {
		Queue<Vertex> queue = new LinkedList<Vertex>();
		Vertex current = null;
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < map.length; i++) {
			current = findCur(map, index);
			if (current != null && current.y != map.length) {
				map[index.y][index.x] = 2;
			}
			if (current.y == map.length) {
				return list;
			}
			int cnt = 0;
			queue.offer(current);

			while (queue.size() != 0) {
				if ((current = queue.poll()) != null) {
					cnt++;
				}
				findAdjcent(map, current, queue);
			}
			list.add(cnt);
		}
		return list;

	}

	public static Vertex findCur(int[][] map, Vertex index) {
		if (index.x >= map.length) {
			index.x = 0;
			index.y++;
		}
		if (index.y >= map.length) {
			index = null;
			return index;
		}
		if (map[index.y][index.x] != 1) {
			index.x++;
			findCur(map, index);
		}
		return index;
	}

	public static void findAdjcent(int[][] map, Vertex index, Queue<Vertex> queue) {
		if (index.x != map.length - 1 && map[index.y][index.x + 1] == 1) {
			queue.offer(new Vertex(index.y, index.x + 1));
			map[index.y][index.x + 1] = 2;
		}
		if (index.x != 0 && map[index.y][index.x - 1] == 1) {
			queue.offer(new Vertex(index.y, index.x - 1));
			map[index.y][index.x - 1] = 2;
		}
		if (index.y != map.length - 1 && map[index.y + 1][index.x] == 1) {
			queue.offer(new Vertex(index.y + 1, index.x));
			map[index.y + 1][index.x] = 2;
		}
		if (index.y != 0 && map[index.y - 1][index.x] == 1) {
			queue.offer(new Vertex(index.y - 1, index.x));
			map[index.y - 1][index.x] = 2;
		}
	}
}

class Vertex {
	Integer y;
	Integer x;

	public Vertex(int y, int x) {
		this.y = y;
		this.x = x;
	}
}
