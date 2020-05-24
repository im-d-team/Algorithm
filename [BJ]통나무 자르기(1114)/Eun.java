package study;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class AL {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int L = sc.nextInt();
		int K = sc.nextInt();
		int C = sc.nextInt();
		
		int[] num = new int[K];
		Integer[] result = new Integer[K]; 
		
		
		for(int i=0;i<K;i++) {
			num[i] = sc.nextInt();		
		}
		
		for(int j=0;j<K;j++) {
			result[j]=L-num[j];			
		}
		
		Arrays.sort(result,Comparator.reverseOrder());
		
		for(int i=0;i<K;i++) {
			System.out.print(result[i]+" ");
		}
		
	}
}
