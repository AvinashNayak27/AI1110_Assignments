#include <stdio.h>
int main(){
    int i,p,n,r;
    i=441;
    n=20;
    r=9;
    p=(2400*i)/(n*(n+1)*r);
    printf("Rekha deposited ₹%d each month to get ₹%d as interest at the end of maturity period\n",p,i);
}