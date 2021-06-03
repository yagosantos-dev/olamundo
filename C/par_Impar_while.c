#include<stdio.h>
#include<stdlib.h>

void main (){
    int cont = 9;

    int res;
   printf(" numeros pares e impares da sequencia de 10 a 20 \n");

   while(cont < 20){
    cont++;
    res = cont;

    if(res % 2 == 0){

        printf("%d par\n",res);

    }else{

        printf("%d impar \n",res);
    }

   }


}
