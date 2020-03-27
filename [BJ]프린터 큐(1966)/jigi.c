#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b)
{
	unsigned char __a = *(unsigned char*) a;
	unsigned char __b = *(unsigned char*) b;

	return __a < __b ? 1 : -1;
}

void print_documents(void)
{
	unsigned char *print_queue, *sorted_queue;
	unsigned char nr_doc, nth, head, order = 0;
	unsigned char i;

	scanf("%hhu %hhu", &nr_doc, &nth);

	print_queue = malloc((sizeof(unsigned char) * nr_doc) << 1);
	sorted_queue = &print_queue[nr_doc];

	for (i = 0; i < nr_doc; i++)  {
		scanf("%hhu", &print_queue[i]);
	}

	memcpy(sorted_queue, print_queue, sizeof(unsigned char) * nr_doc);
	qsort(sorted_queue, nr_doc, sizeof(unsigned char), compare);

	for (head = 0; order < nr_doc; head = (head+1) % nr_doc) {
		if (sorted_queue[order] == print_queue[head]) {
			print_queue[head] = 0;
			++order;

			if (head == nth)
				break;
		}
	}

	free(print_queue);

	printf("%hhu\n", order);
}

int main(void)
{
	unsigned int nr_case;

	scanf("%u", &nr_case);

	for ( ; nr_case; --nr_case) {
		print_documents();
	}

	return 0;
}
