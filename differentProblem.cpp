// https://open.kattis.com/problems/different

# include <iostream>

using namespace std;

int main(){
    long long a, b;
    while(cin >> a >> b)
        cout << abs(a-b) << endl;
    return 0;
}