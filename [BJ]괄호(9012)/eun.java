package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class Eun {
	
	public static void main(String[] args) throws Exception, Exception {
		// TODO Auto-generated method stub
		

		char[] st = new char[50];
		
		int count=0;
		Scanner sc = new Scanner(System.in);

		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		
		//int num = sc.nextInt();		//맨처음 입력 받는 숫자
		
		for(int i=1;i<=testCase;i++) {
			count = 0;
			//String inputStr = sc.next();
			String str = br.readLine();
			for(int j=0;j<str.length();j++) {
				st[j] = str.charAt(j);
				if(st[j] == '(') {
					count++;
				}
				else {
					count--;
				}
			}
			if(count==0) {
				System.out.println("YES");
			}else {
				System.out.println("NO");
			}
		}

	}
}
