package study;

import java.util.Scanner;
import java.util.Stack;

public class Eun {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		int count=0;
		
		
		for(int i=0;i<num;i++) {
			
			Stack<Character> stack = new Stack<>();
			String alpha = sc.next();
			
			for(int j=0;j<alpha.length();j++) {
				if(!stack.isEmpty()) {
					if(stack.peek()==alpha.charAt(j)) {
						stack.pop();
					}
					else {
						stack.push(alpha.charAt(j));
					}
				}else {
					stack.push(alpha.charAt(j));
				}
			}
			if(stack.isEmpty()) {
				count++;
			}
		}
		System.out.println(count);

	}
}
