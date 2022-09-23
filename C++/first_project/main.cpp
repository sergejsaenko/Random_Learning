#include <iostream>
#include "cat.h"
using namespace std;

int main()
{
    string answer = "";
    CAT cat1;
    cat1.frage();
    cin >> answer;
    cat1.speak();
    cout << "Du bist mit " << answer << " Jahren alt genug, um eine Katze zu besitzen!" << endl;
    return 0;
};