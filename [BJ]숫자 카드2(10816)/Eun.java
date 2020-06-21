package study;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class AL {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("EE");
		
		int N = sc.nextInt();
		
		int[] Scard = new int[N];
		
		
		for (int i = 0; i < N; i++) {
			 int num = sc.nextInt();
			 Scard[i]=num;
		}
		int M = sc.nextInt();

		int[] card = new int[M];
		int[] result = new int[M];

		
		for(int i=0;i<M;i++) {
			 int num = sc.nextInt();
			 card[i]=num;
		}
		
		for (int i = 0; i < card.length; i++) {
			int cnt = 0;

			for(int j=0;j<Scard.length;j++) {
				
				if(card[i]==Scard[j]) {
					 cnt++;
				}
				result[i]=cnt;
			}
		}
		
		for(int i=0;i<result.length;i++) {
			System.out.print(result[i] + " ");
		}
	}
}
