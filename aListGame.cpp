// https://open.kattis.com/problems/listgame

# include <iostream>
# include <vector>

using namespace std;

int getK(unsigned long number, int k);

int main(){
    unsigned long x, factor;
    cin >> x;
    cout << getK(x, 1) << endl;

    return(0);
}

int getK(unsigned long number, int k){
    for(unsigned long i=2; i<=number/i; i++){
        if (number%i == 0)
            return getK(number/i, ++k);
    }
    return k;
}
