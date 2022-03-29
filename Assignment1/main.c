#include <stdio.h>
int main(){
    int i,p,n,r;
    i=441; //Total interest recieved at the end
    n=20;//no.of months recursively deposited principle amount
    r=9;//rate of interest per annum
    /*
    As total interest is sum of each month's interest i.e
    i=i1+i2+i3+-----in
    i=(p*r*1)/(12*100)+(p*r*2)/(12*100)+(p*r*3)/(12*100)+_ _ _ _ + (p*r*n)/(12*100)
    i=(p.r/1200)*(1+2+3+_ _ _ n)
    i=(p.r/1200)*((n)(n+1)2)
    i=p.r.n.(n+1)/2400
    */
    p=(2400*i)/(n*(n+1)*r);
    printf("Rekha deposited ₹%d each month to get ₹%d as interest at the end of maturity period\n",p,i);
}
