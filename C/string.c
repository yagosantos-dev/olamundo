#include<stdio.h>
#include<stdlib.h>


void main (){

    char palavra [10];


    printf("Digite uma palavra");

    setbuf(stdin,0);


    fgets(palavra, 255, stdin);
    //nesse parametro é onde pegamos o valor da estring

    palavra[strlen(palavra)-1] = "\0";
    // para não ocupar espaço desnecessario na memoria a ram com o espaço de 9 espaços no final é colocada /0 nessa função a gente força  o 0/ para ele ficar
    // na ultima posição da palavra exemplo se a palavra for ovo depois do ultimo o do ovo ele colcoa /0 fazendo economizar memoria

    printf("%s",palavra);



}
