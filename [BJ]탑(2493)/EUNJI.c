#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>  

void main() {

	int size;
	int isThere = 0; // 0 is false

	scanf("%d", &size);

	int *inArr = malloc(sizeof(int) * (size+1));
	int *outArr = malloc(sizeof(int) * (size+1));

	for (int i = 1; i < size+1; i++)    
	{
		scanf("%d", &inArr[i]);                
	}

	for (int i = size; i > 0; i--) {
		isThere = 0;
		for (int j = i - 1; j > 0; j--) {
			if (inArr[j] > inArr[i]) {
			
				outArr[i] = j;
				isThere = 1;
				break;
			}
		}
		if (isThere == 0) {
			outArr[i] = 0;
		}
	}

	for (int j = 1; j < size + 1; j++) {
		printf("%d ", outArr[j]);
	}


}
