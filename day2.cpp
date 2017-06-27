#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   
    string tem;
    getline(cin,tem);
    double mealprice=stod(tem);
    
    getline(cin,tem);
    int tip=stoi(tem);
    
    getline(cin,tem);
    int tax=stoi(tem);
    
    int totalcost = round(mealprice+(((mealprice)*(tip+tax))/100));
    printf("The total meal cost is %i dollars.", totalcost);

    return 0;   
}
