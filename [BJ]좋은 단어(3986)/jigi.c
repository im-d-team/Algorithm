#include <stdio.h>

int main(void)
{
	unsigned int nr_str, nice = 0;

	scanf("%u\n", &nr_str);

	do {
		int latest, new = getchar();
		unsigned int head = 0;

		for (latest = !(new & 1); new != '\n'; latest = !latest) {
			new &= 1;
			head += ((new ^ latest) << 1) - 1;
			new = getchar();
		}

		nice += !(head);
	} while(--nr_str);

	printf("%u\n", nice);

	return 0;
}
