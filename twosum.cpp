#include<stdio.h>
int main(){
    int a[]={2,7,11,15};
    int target=9;
    for(int i=0;i<3;i++){
        for(int j=i+1;j<3;j++){
            printf("%d %d",i,j);
        }
    }

}