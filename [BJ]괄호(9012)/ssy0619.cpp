#include<iostream>
#include<string>
#include<stack>

using namespace std;

int main(void){

int num;
string parenthesis;
int result =0;

cin >> num;

for(int i=0;i<num;i++){
    cin >> parenthesis;
    stack<char> s;

    for(int j=0;j<parenthesis.length();j++){
        if(parenthesis[j] == '(')
            s.push(parenthesis[j]);
        else if(parenthesis[j] == ')' && s.top()=='(')
            s.pop();
    }

    if (s.empty())
        cout << "YES" << "\n";
    else
        cout << "NO" << "\n";
}

   

    return 0;
}
