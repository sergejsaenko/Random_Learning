#pragma once
#include <string>
using namespace std;

class CAT
{
private:
    string catspeak = "meow";
    string question = "Wie alt bist du?";

public:
    void speak();
    void frage();
};