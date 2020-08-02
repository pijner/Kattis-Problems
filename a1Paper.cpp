# include <stdio.h>
# include <math.h>
# include <iostream>


void rotateSheet(double *length, double *width);

using namespace std;

int main(){
    double length = pow(0.5, 3.0/4.0), width = pow(0.5, 5.0/4.0);
    // The first line of input contains a single integer 2 ≤ n ≤ 30, the A-size of the smallest papers Björn has
    int n;
    cin >> n;

    // The second line contains n−1 integers giving the number of sheets he has of each paper size starting with A2 and ending with An
    long long nSheets[--n];
    for(int i=0; i<n; i++)
        cin >> nSheets[i];

    // Björn doesn’t have more than 10^9 sheets of any paper size
    // Assuming the system performs 10^8 operations/second, we would want to limit our solution to O(n)
    
    // Start with the smallest sheet and work up
    long long need = 2;
    double tape = 0.0;
    bool complete = false;
    for(int i=0; i<n; i++){
        int numPairs = (nSheets[i]/2);

        tape += length*need/2;
        // If we have enough sheets to join, we're done
        if (nSheets[i] >= need)
            complete = true;
        
        // Add as many sheets of this size as possible (greedy approach to minimize tape consumption)
        else
            need -= nSheets[i];
        
        if(complete)
            break;

        // Set-up for next size
        length /= 2.0;
        need *= 2;
        rotateSheet(&length, &width);
    }

    if(complete)
        printf("%.10f\n", tape);
    else
        printf("impossible\n");


    return 0;
}

void rotateSheet(double *length, double *width){
    // Function to rotate a given sheet (swap length and width)
    *length += *width;
    *width = *length - *width;
    *length -= *width;
}