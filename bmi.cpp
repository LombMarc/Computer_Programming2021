#include <iostream>
#include <cmath>

using namespace std;

class Bodymass{
    float w, h;
public:
    void set_values(float,float);
    float BMI() {return (w/pow(h/100,2.0));}
};

void Bodymass::set_values(float x,float y){
    w=x;
    h=y;
    }

int main()
{
    Bodymass person;
    float ww,hh;
    cout << "Set weight(kg): ";
    cin >> ww;
    cout << endl;
    cout <<"Set height(cm): ";
    cin >> hh ;
    person.set_values(ww,hh);
    std::cout.precision(4);
    cout <<"Your BMI is: "<<person.BMI() <<endl;
    return 0;
}
