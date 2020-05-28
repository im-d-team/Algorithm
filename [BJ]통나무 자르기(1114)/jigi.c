#include <stdio.h>
#include <stdlib.h>

static int compare(const void *a, const void *b)
{
	return *(int *) a - *(int *) b;
}

static inline int cut_into(int *log, int mark, int chance, int len)
{
	int i;

	for (i = mark-1; i >= 0; i--) {
		if (log[mark] - log[i] > len) {
			if (mark == ++i) {
				return 0;
			}

			mark = i;
			--chance;
		}
	}

	return (chance < 0) ? 0 : (chance ? 1 : mark);
}

int main(void)
{
	int len, mark, chance, *log;
	int first, min = 0, i;

	scanf("%d %d %d\n", &len, &mark, &chance);

	log = malloc(sizeof(int) * ((++mark) + 1));
	log[0] = 0;
	log[mark] = len;

	for (i = 1; i < mark; i++) {
		scanf("%d", &log[i]);
	}

	qsort(log+1, mark-1, sizeof(int), compare);

	while (min <= len) {
		int try = (min + len) >> 1;
		int ret = cut_into(log, mark, chance, try);

		if (ret) {
			len = try - 1;
			first = ret;
		} else {
			min = try + 1;
		}
	}

	printf("%d %d\n", len + 1, log[first]);

	return 0;
}
