package baekjoon.q1260;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;

//4번에서 3번 넘어가는지 확인하기

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] condition = Arrays.stream(br.readLine().split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray();
		int n = condition[0];
		int m = condition[1];
		int index = condition[2];
		int[] vertaxes;
		Graph graph = new Graph(n);

		for (int i = 0; i < m; i++) {
			vertaxes = Arrays.stream(br.readLine().split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray();
			graph.setAdjacent(vertaxes[0], vertaxes[1]);
		}

		for (int i = 0; i < n; i++) {
			graph.sortGraph(i);
		}
		if (graph.dfs(index).isEmpty()) {
			graph.result.add(index);
		}
		graph.printResult();
		if (graph.bfs(index).isEmpty()) {
			graph.result.add(index);
		}
		graph.printResult();

	}
}

class Graph {
	private ArrayList<Integer>[] graph;
	private ArrayDeque<Integer> stack;
	private ArrayDeque<Integer> queue;
	private boolean[] walked;
	public ArrayList<Integer> result;

	@SuppressWarnings("unchecked")
	public Graph(int n) {
		graph = (ArrayList<Integer>[]) Array.newInstance(ArrayList.class, n);

		for (int i = 0; i < n; i++) {
			graph[i] = new ArrayList<Integer>();
		}

	}

	public void setAdjacent(int vertax, int adjacent) {
		graph[vertax - 1].add(adjacent);
		graph[adjacent - 1].add(vertax);
	}

	public void sortGraph(int i) {
		graph[i].sort(null);
	}

	public ArrayList<Integer> dfs(int index) {
		stack = new ArrayDeque<Integer>();
		result = new ArrayList<Integer>();
		walked = new boolean[graph.length];

		executeDfs(index);

		return result;
	}

	public ArrayList<Integer> bfs(Integer index) {
		queue = new ArrayDeque<Integer>();
		result = new ArrayList<Integer>();
		walked = new boolean[graph.length];

		while (index != null) {
			index = executeBfs(index);
		}

		return result;
	}

	public void printResult() {
		StringBuffer sb = new StringBuffer();
		for (int i : result) {
			sb.append(i + " ");
		}
		System.out.println((sb.toString()).trim());
	}

	private void executeDfs(int index) {
		if (!walked[index - 1]) {
			if (graph[index - 1].isEmpty()) {
				return;
			}

			pushAdjacent(stack, graph[index - 1]);
			walked[index - 1] = true;
			result.add(index);
		}

		if (!stack.isEmpty()) {
			executeDfs(stack.pop());
		}
	}

	private Integer executeBfs(int index) {
		if (walked[index - 1]) {
			return queue.poll();
		}

		if (!walked[index - 1] && !graph[index - 1].isEmpty()) {

			enqueueAdjacent(queue, graph[index - 1]);
			walked[index - 1] = true;
			result.add(index);
		}

		return queue.poll();
	}

	private void pushAdjacent(ArrayDeque<Integer> stack, ArrayList<Integer> adjacent) {
		for (int i = adjacent.size() - 1; i >= 0; i--) {
			if (!walked[adjacent.get(i) - 1]) {
				stack.push(adjacent.get(i));
			}
		}
	}

	private void enqueueAdjacent(ArrayDeque<Integer> queue, ArrayList<Integer> adjacent) {
		for (int i = 0; i < adjacent.size(); i++) {
			if (!walked[adjacent.get(i) - 1]) {
				queue.offer(adjacent.get(i));
			}
		}
	}
}
