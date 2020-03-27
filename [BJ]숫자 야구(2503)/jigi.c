#include <stdio.h>
#include <stdlib.h>

struct trial {
	unsigned short num;
	unsigned char strike, ball;
};

#define hex_formed(num) \
	( (((num)/100) << 8) | (((num)%100/10) << 4) | ((num)%10) )

#define digit_of(num, n) \
	( ((num) >> (n << 2)) & 0xF )

static inline int possible(unsigned short num)
{
	return !!( digit_of(num, 2) && digit_of(num, 1) && digit_of(num, 0)
		&& digit_of(num, 2) != digit_of(num, 1)
		&& digit_of(num, 2) != digit_of(num, 0)
		&& digit_of(num, 1) != digit_of(num, 0) );
}

int wrong(unsigned short num, unsigned short try,
		unsigned char strike, unsigned char ball) {
	int i, j;

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			if (digit_of(num, i) == digit_of(try, j)) {
				if (i == j) --strike;
				else --ball;
			}
		}
	}

	return !!(strike || ball);
}

int main(void)
{
	struct trial *trial;
	unsigned short nr_try;

	int i, j, count = 0;

	scanf("%hu", &nr_try);
	trial = malloc(sizeof(struct trial) * nr_try);

	for (i = 0; i < nr_try; i++) {
		struct trial *t = &trial[i];
		scanf("%hu %hhu %hhu", &t->num, &t->strike, &t->ball);
		t->num = hex_formed(t->num);
	}

	for (i = 0; i < 1000; i++) {
		unsigned short num = hex_formed(i);

		if (!possible(num))
			continue;

		for (j = 0; j < nr_try; j++) {
			struct trial *t = &trial[j];

			if (wrong(num, t->num, t->strike, t->ball))
				break;
		}

		if (j == nr_try)
			++count;
	}

	printf("%d\n", count);

	return 0;
}
