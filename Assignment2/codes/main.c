#include<stdio.h>

int main(){
 
  int a[3][3];
  int x,y,z;
  int determinant,result;
  scanf("%d %d %d",&x,&y,&z);
  a[0][0]=x;
  a[1][0]=y;
  a[2][0]=z;
  a[0][1]=x*(x*x+1);
  a[1][1]=y*(y*y+1);
  a[2][1]=z*(z*z+1);
  a[0][2]=x+1;
  a[1][2]=y+1;
  a[2][2]=z+1;

  result=(x-y)*(y-z)*(z-x)*(x+y+z);
  /* formula for finding determinant of a 3*3 MAtrix */
  determinant = a[0][0] * ((a[1][1]*a[2][2]) - (a[2][1]*a[1][2])) -a[0][1] * (a[1][0]
   * a[2][2] - a[2][0] * a[1][2]) + a[0][2] * (a[1][0] * a[2][1] - a[2][0] * a[1][1]);
  
  printf("LHS of given equation: %d\n", determinant);
  printf("RHS of given equation: %d\n", result); 
  if (determinant==result)
  {
    printf("LHS=RHS\n");
    printf("Hence proved!\n");
  }
  
   return 0;
}