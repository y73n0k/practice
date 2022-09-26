#include <stdio.h>

int main(){
    long long int delta = 0;
    for(int i = 322376503; i > 0; --i){
        delta = 4919 * delta + 1337;
    }
    printf("%llx\n", delta);
    return 0;
}