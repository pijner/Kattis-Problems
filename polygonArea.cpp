// https://open.kattis.com/problems/polygonarea

# include <iostream>

using namespace std;

int main(){

    int n;
    cin >> n;
    while(n){
        int poly[n][2];
        for(int j=0; j<n; j++){
            cin >> poly[j][0] >> poly[j][1];
        }

        double area = 0;
        for(int i=0; i<n-1; i++)
            area += ( (poly[i][0] * poly[i+1][1]) - (poly[i][1] * poly[i+1][0]));
    
        area += ( (poly[n-1][0] * poly[0][1]) - (poly[n-1][1] * poly[0][0]) );

        if(area > 0)
            printf("CCW %.1f\n", area/2);
        else
            printf("CW %.1f\n", -1*area/2);

        cin >> n;
    }
    return 0;
}