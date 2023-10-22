/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package burbuja;

/**
 *
 * @author cuaut
 */
public class Burbuja {

    public static void main(String[] args) {
        int[] Lista = {1,2,5,6,7,3,4,8,9};
        int t= Lista.length;
        Ordenamiento_burbuja(Lista, t);
        for(int i = 0; i < t; i++){
            System.out.print(Lista[i] + " ");
        }
    }
    
    private static void Ordenamiento_burbuja(int[] Lista, int t){
       for(int i = 0; i < t; i++){
            for(int j = 0; j < t-i-1; j++){ 
                if(Lista[j+1] < Lista[j]){
                    int aux = Lista[j+1];
                    Lista[j+1] = Lista[j];
                    Lista[j] = aux;
                }
            }
        }
    }
}
