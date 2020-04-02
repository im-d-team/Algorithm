#include <stdio.h>

int is_nice(void)
{
	char buffer[50001] = {'\0'};
	char letter, *head = buffer;

	while ((letter = (char) getchar()) ^ '\n') {
		if (letter ^ (*head)) {
			*(++head) = letter;
		} else {
			--head;
		}
	}

	return (head == buffer);
}

int main(void)
{
	unsigned int nr_str, nice = 0;

	scanf("%u\n", &nr_str);

	while (nr_str--) {
		nice += is_nice();
	}

	printf("%u\n", nice);

	return 0;
}
