#include<stdio.h>
#include<stdlib.h>

void main (){
int vetor[5];

int cont = 0;

vetor[0] = 2;
vetor[1] = 4;
vetor[2] = 6;
vetor[3] = 8;
vetor[4] = 10;


for (cont; cont < 5;cont++){
    printf("vetor[%d] com valor %d \n",cont,vetor[cont]);

}

}
