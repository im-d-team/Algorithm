#include <stdio.h>

int main(void)
{
	char string[102], *str, *bracket = string;

	while ((str = fgets(string, 102, stdin)) && *str != '.') {
		int head = 0;

		for ( ; *str; str++) {
			switch (*str) {
			case '(':
			case '[':
				bracket[head++] = *str;
				break;
			case ']':
				--(*str);
			case ')':
				if (!head || bracket[--head] != --(*str))
					head = 51;
			}

			if (head > 50)
				break;
		}

		printf("%s\n", head ? "no" : "yes");
	}

	return 0;
}
