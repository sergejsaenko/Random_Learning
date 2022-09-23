//Question with following code:
//What will happen with the code?
//a. infinite loop
//b. no output
//c. "Hello" printed

#include <stdio.h>

int main(){
    for(;;)printf("Hello");
}