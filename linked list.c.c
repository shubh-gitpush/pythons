/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
    struct node{
    int data;
    struct node*next;
};
void Linkedlisttraversal(struct node*ptr)
{
    while (ptr!=NULL)
    {
        printf("%d\n",ptr->data);
        ptr=ptr->next;
    }
}
//to insert in the beginning
struct node*insert(struct node*head,int data){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    ptr->next=head;
    ptr->data=data;
    return ptr;
}
//to insert in between
struct node *insertindex(struct node *head,int data,int index){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p=head;
    int i=0;
    
    while(i!=index-1)
    {
        p=p->next;
        i++;
    }
        ptr->next=p->next;
        p->next=ptr;
        ptr->data=data;
        return head;
        
}
//to insert at the end
struct node*insertend(struct node*head,int data){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p=head;//pointing to the head of node (first box)
    ptr->data=data;
    while (p->next!=NULL)
    {
        p=p->next;
    }
    p->next=ptr;
    ptr->next=NULL;
    return head;
}
//insert after a node
struct node *insertafternode(struct node *head,struct node *prevnode,int data){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
        ptr->next=prevnode->next;
        prevnode->next=ptr;
        ptr->data=data;
        return head;
}
//to delete the node in the beginning
    struct node *delete(struct node *head){
        struct node *q=head;
        head=head->next;
        free(q);
        return head;
    }//to delete in between
struct node *deleteinbetween(struct node *head,int index){
    struct node *ptr=head;
    struct node*q=ptr->next;
    int i;
    for (i=0;i<index-1;i++){
        ptr=ptr->next;
        q=q->next;
    }
    ptr->next=q->next;
    free(q);
    return head;
    
    
}
struct node *deleteend(struct node *head){
    struct node *p=head;
    struct node *q=head->next;
    while(q->next!=NULL)
    {
        p=p->next;
        q=q->next;
    }
    p->next=NULL;
    free(q);
    return head;
}


int main (){
    struct node*head;
    struct node*second;
    struct node*third;
     struct node*four;
    head=(struct node*)malloc(sizeof(struct node));
    second=(struct node*)malloc(sizeof(struct node));
    third=(struct node*)malloc(sizeof(struct node));
    four=(struct node*)malloc(sizeof(struct node));
    head->data=7;
    head->next=second;
    second->data=10;
    second->next=third;
    third->data=13;
    third->next=four;
    four->data=15;
    four->next=NULL;
    //Linkedlisttraversal(head);
    //head=insert(head,44);
    //head=insertindex(head,44,1);
    //head=insertend(head,9);
    //head=insertafternode(head,head,67);
    //head=delete(head);
    head=deleteinbetween(head,3);
    //head=deleteend(head);
    Linkedlisttraversal(head);
    

    return 0;
}




