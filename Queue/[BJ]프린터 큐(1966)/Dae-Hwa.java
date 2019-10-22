package baekjoon.q1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int caseNum = Integer.parseInt((br.readLine()));
		Printer printer = new Printer(caseNum);
		for (int seq = 0; seq < caseNum; seq++) {
			String[] scndLine = br.readLine().split(" ");
			printer.initQueue(seq, Integer.parseInt(scndLine[0]));
			printer.setTarget(seq, Integer.parseInt(scndLine[1]));
			printer.setPriority(seq,
					Arrays.stream(br.readLine().split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray());

			System.out.println(printer.executePrint(seq));
		}
	}
}

class Printer {
	ArrayDeque<Integer>[] queue;
	int[][] priorities;
	int[] targets;

	@SuppressWarnings("unchecked")
	public Printer(int n) {
		queue = (ArrayDeque<Integer>[]) Array.newInstance(ArrayDeque.class, n);
		for (int i = 0; i < n; i++) {
			queue[i] = new ArrayDeque<Integer>();
		}
		priorities = new int[n][];
		targets = new int[n];
	}

	public void initQueue(int seq, int length) {
		for (int i = 0; i < length; i++) {
			queue[seq].add(i);
		}
	}

	public void setTarget(int seq, int target) {
		targets[seq] = target;
	}

	public void setPriority(int seq, int[] values) {
		priorities[seq] = new int[values.length];
		for (int i = 0; i < values.length; i++) {
			priorities[seq][i] = values[i];
		}
	}

	public int executePrint(int seq) {
		int cnt = 0;
		int v;
		while (!queue[seq].isEmpty()) {
			v = queue[seq].poll();
			if (isBiggerNum(seq, v)) {
				queue[seq].offer(v);
			} else {
				priorities[seq][v] = 0;
				cnt++;
				if (v == targets[seq]) {
					return cnt;
				}
			}
		}

		return cnt;
	}

	private boolean isBiggerNum(int seq, int v) {
		for (int i = 0; i < priorities[seq].length; i++) {
			if (priorities[seq][v] < priorities[seq][i]) {
				return true;
			}
		}
		return false;
	}
}
