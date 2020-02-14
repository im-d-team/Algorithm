#include <stdio.h>

#define MAX_PERSON 10

int main(void)
{
	unsigned short pos[MAX_PERSON] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	unsigned short nr_person;
	int order, left, i = 0;

	scanf("%hu", &nr_person);

	while (i < nr_person) {
		scanf("%d", &left);

		for (order = 0; pos[order] || left; ++order) {
			if (!pos[order])
				--left;
		}

		pos[order] = ++i;
	}

	for (i = 0; i < nr_person; i++) {
		printf("%hu ", pos[i]);
	}

	return 0;
}
