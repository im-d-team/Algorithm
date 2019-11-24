#include <stdio.h>

int main(void)
{
	char string[102], *str, *bracket = string;

	while ((str = fgets(string, 102, stdin)) && *str != '.') {
		int head = 0;

		for ( ; *str; str++) {
			switch (*str) {
			/*
			 * The `bracket` is a stack for the opening brackets,
			 * and 'head' is a pointer for latest entry.
			 */
			case '(':
			case '[':
				bracket[head++] = *str;
				break;
			/*
			 * Pop out an opening bracket if it pairs with inputted
			 * closing bracket. If not, the string is not balenced.
			 */
			case ']':
				--(*str);
			case ')':
				if (!head || bracket[--head] != --(*str))
					head = 51;
			}

			/*
			 * If the number of stacked opening bracket is over 50,
			 * the number of closing brackets is below 50. It means,
			 * in such case, the string cannot be balenced.
			 */
			if (head > 50)
				break;
		}

		printf("%s\n", head ? "no" : "yes");
	}

	return 0;
}
