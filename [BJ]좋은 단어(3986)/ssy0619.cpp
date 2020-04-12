#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void)

{
	int num = 0;
	int count = 0;
	string str;

	// 단어 개수 받기
	cin >> num;

	for (int i = 0; i < num; i++)

	{
		// 단어를 문자열로 받기
		cin >> str;

		stack<char> temp;

		for (int j = 0; j < str.length(); j++)

		{
			// stack이 비어있지 않고, 스택의 top이 str[j]와 같다면 stack에서 문자 제거
			if (!temp.empty() && temp.top() == str[j])

				temp.pop();

			else
				temp.push(str[j]);
		}

		// 스택이 비어있다면 좋은단어
		if (temp.empty())

			count++;

	}

	cout << count << "\n";

	return 0;

}