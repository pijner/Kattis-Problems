// https://open.kattis.com/problems/anthonyanddiablo

# include <iostream>
# include <cmath>

using namespace std;

int main(){
    double A, N;

    // for a given area, the perimeter of a circle will be the smallest compared to any other shape
    // so building a circular cage will use the least amount of materials

    cin >> A >> N;
    
    if (2 * sqrt(M_PI * A) <= N)
        cout << "Diablo is happy!\n";
    else
        cout << "Need more materials!\n";

    return(0);
}