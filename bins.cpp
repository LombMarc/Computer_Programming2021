#include <iostream>

using namespace std;

#define pi 3.14159


int* bins()
{


    int n, c;
    int bn[10];
    cout <<"number to convert in binary: ";
    cin >> n;
    for (c=0; n>0;c++){
        bn[c]=n %2;
        n =n /2;
    }
    for (c=c-1;c>=0;c--){
        cout << bn[c];
    }
    return bn;
}


int main()
{
    char ans;
    int i;
    for (i=0;i<=1;i=0){
        bins();
        cout << ""<< endl;
        cout << "There are other number to convert (y/n): ";
        cin >> ans;
        if (ans=='n'){
            return 0;
        }
    }
}

