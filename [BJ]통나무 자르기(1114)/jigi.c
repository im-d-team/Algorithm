#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
	int va = *(int *) a, vb = *(int *) b;
	return va > vb ? 1 : (va < vb ? -1 : 0);
}

static inline int cut_into(int *log, int mark, int chance, int *len, int *first)
{
	int longest = 0, chunk = 0, i;

	for (i = mark-1; i >= 0; --i) {
		chunk = log[mark] - log[i];

		if (chunk > (*len)) {
			if (mark == i+1) {
				return 0;
			}

			chunk = log[mark] - log[++i];
			longest = chunk > longest ? chunk : longest;
			mark = i;
			--chance;
		}
	}

	*len = chunk > longest ? chunk : longest;
	*first = chance > 0 ? 1 : mark;

	return (chance >= 0);
}

int main(void)
{
	int len, mark, chance, *log;
	int longest, the_first, first, i;

	scanf("%d %d %d\n", &len, &mark, &chance);

	log = malloc(sizeof(int) * ((++mark)+1));
	log[0] = 0;
	log[mark] = len;

	for (i = 1; i < mark; i++) {
		scanf("%d", &log[i]);
	}

	qsort(log+1, mark-1, sizeof(int), compare);

	while (cut_into(log, mark, chance, &len, &first)) {
		longest = len--;
		the_first = first;
	}

	printf("%d %d\n", longest, log[the_first]);

	return 0;
}
