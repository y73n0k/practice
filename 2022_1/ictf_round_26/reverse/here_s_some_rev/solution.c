#include <stdio.h>

int x = 0xFF, a = 0x5316E2, b = 0x1EEECFE, m = 0x7F;

unsigned int invmod(int a1, int a2)
{
    int v3, v5, v7;
    unsigned int v6, v8, v9;

    v3 = a2;
    v9 = 0;
    v8 = 1;
    if ( a2 == 1 )
        return 0;
    while ( a1 > 1 )
    {
        v7 = a1 / v3;
        v5 = v3;
        v3 = a1 % v3;
        a1 = v5;
        v6 = v9;
        v9 = v8 - v9 * v7;
        v8 = v6;
    }
    return v8;
}

int gen()
{
    x = (a * invmod(x, m) + b) % m;
    return x;
}

int main()
{
    int v4 = 0, v5 = 0, v4s[74], v5s[74];
    for (int i = 0; i < 74; i++)
    {
        v5 = gen();
        v4 = i * v5 % 74;
        v4s[i] = v4;
        v5s[i] = v5;
    }
    printf("v4s = [");
    for (int i = 0; i < 73; i++)
        printf("0x%x, ", v4s[i]);
    printf("0x%x]\nv5s = [", v4s[73]);
    for (int i = 0; i < 73; i++)
        printf("0x%x, ", v5s[i]);
    printf("0x%x]\n", v5s[73]);
    return 0;
}
