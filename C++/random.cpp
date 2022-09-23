#include <iostream>

int main()
{
    int i = 2;
    int k = 0, j = 0;

    k = ++i;
    std::cout << "k1:" << k << std::endl;
    std::cout << "i1:" << i << std::endl;

    k = i++;
    std::cout << "k2:" << k << std::endl;
    std::cout << "i1:" << i << std::endl;

    k = (i++) * (i--);
    std::cout << "k3:" << k << std::endl;
    std::cout << "i1:" << i << std::endl;
}