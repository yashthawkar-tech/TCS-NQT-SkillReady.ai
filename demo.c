#include<stdio.h>
#include<stdlib.h>

struct Node{
    int value;
    struct Node *address;
};

struct Node *starting_node=NULL;
struct Node *createnode(){
    struct Node *n;
    n=(struct Node*)malloc(sizeof(struct Node));

}
void insertnode(){
    struct Node *temp;
    temp=createnode();
    printf("enter any number:")
    scanf("%d",&temp->value);
    temp->address=NULL;
    if(starting_node==NULL){
        starting_node=temp;
    }
}