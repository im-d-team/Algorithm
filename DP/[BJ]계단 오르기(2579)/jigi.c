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

	/*
	 * Create `score` copied from `stair`. `score` is for saving the
	 * accumulated maximum score of current level of stair.
	 */
	memcpy(score, stair, sizeof(unsigned int) * level);

	score[1] += stair[0];
	score[2] += max(stair[1], stair[0]);

	/*
	 * The accumulated score of level n is the score of level n + either, 
	 * - the accumulated score of level n-2,
	 * - or the score of level n-1 + the accumulated score of level n-3
	 *   (because for the 2nd case, we cannot step on stair level n-2)
	 */
	for (i = 3; i < level; i++) {
		score[i] += max(score[i-2], stair[i-1] + score[i-3]);
	}

	printf("%u\n", score[level-1]);

	return 0;
}
