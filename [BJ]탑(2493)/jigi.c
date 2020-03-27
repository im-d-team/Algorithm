#include <stdio.h>
#include <stdlib.h>

struct tower {
	unsigned int id, height;
	struct tower *next;
};

int main(void)
{
	struct tower tallest = { 0, 100000000, NULL };
	struct tower *head = &tallest;
	unsigned int nr_tower, i;

	scanf("%u", &nr_tower);

	for (i = 0; i < nr_tower; i++) {
		struct tower *new = malloc(sizeof(struct tower));

		new->id = i+1;
		scanf("%u", &new->height);

		while (head->height < new->height) {
			struct tower *shortest = head;

			head = shortest->next;
			free(shortest);
		}

		printf("%u ", head->id);

		new->next = head;
		head = new;
	}

	return 0;
}
