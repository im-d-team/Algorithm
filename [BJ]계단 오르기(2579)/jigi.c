#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int main(void)
{
	unsigned int *stair, *score;
	unsigned short level, i;

	scanf("%hu", &level);

	stair = malloc((sizeof(unsigned int) * level) << 1);
	score = &stair[level];

	for (i = 0; i < level; i++) {
		scanf("%u", &stair[i]);
	}

	memcpy(score, stair, sizeof(unsigned int) * level);

	score[1] += stair[0];
	score[2] += max(stair[1], stair[0]);

	for (i = 3; i < level; i++) {
		score[i] += max(score[i-2], stair[i-1] + score[i-3]);
	}

	printf("%u\n", score[level-1]);

	return 0;
}
