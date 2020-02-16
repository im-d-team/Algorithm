package study;

import java.util.Random;
import java.util.Scanner;

public class Algorithm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub


	
		Random rand = new Random();
		Scanner sc = new Scanner(System.in);
		int number = sc.nextInt(); //사람 수
		int[] rNumber = new int[number];
		int[] result = new int[number];
		int count = 0;
		
		for(int i=0;i<number;i++) {
			rNumber[i] = rand.nextInt(number);
		}
		
		for(int i=0;i<number;i++) {
			System.out.print(rNumber[i]);
			System.out.println("");
		}
		
		
		for(int i=0;i<rNumber.length;i++) {	
			int minNum = min(rNumber);
			for(int j=0;j<rNumber.length-i;j++) {
				if(j<minNum) {
					continue;
				}else {
					count++;
				}
				result[i] = count;
				remove(minNum,rNumber);
			}
		}
		
		for(int i=0;i<result.length;i++) {
			System.out.print(i);
		}

	}
	
	public static int min(int Rnumber[]) {
		int min = Rnumber[0];
		
		for(int i=0;i<Rnumber.length;i++) {
			if(min > Rnumber[i]) {
				min = Rnumber[i];
			}
		}
		
		return min;
		
	}
	public static void remove(int minNum,int rNumber[]) {
		
		if(minNum+1!=0) {
			for(int i=minNum;i<rNumber.length;i++) {
				rNumber[i] = rNumber[i+1];
			}
			rNumber.
		}else {
			rNumber.
		}
		
	}

}
