# include <iostream>
# include <string>

using namespace std;

int main(){
    int num;
    string t, verdict;
    bool possible[10] = {true, true, true, true, true, true, true, true, true, true};
    while(cin >> num && num){
        cin >> t >> verdict;

        if (verdict == "low"){
            for(int i=0; i<=num; i++)
                possible[i] = false;
        }
        else if(verdict == "high"){
            for(int i=num; i<=10 && verdict[i]; i++)
                possible[i] = false;
        }
        else{
            if (possible[num])
                cout << "Stan may be honest\n";
            else
                cout << "Stan is dishonest\n";
            for(int i=0; i<10; i++)
                possible[i] = true;
        }
    }
    return 0;
}