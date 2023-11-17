/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tourreinas;

/**
 *
 * @author cuaut
 */
public class TourReinas {
    
    static void imprimirTablero(int[][] tablero) {
        for (int fila = 0; fila < 8; fila++) {
            for (int columna = 0; columna < 8; columna++) {
                System.out.print("[" + tablero[fila][columna] + "]  ");
            }
            System.out.println("");
        }
        System.out.println("\n\n");
    }    
    
    static boolean explorar_Tablero(int[] posiciones, int filaActual) {
        if (filaActual == posiciones.length) {
            return true;
        }
        for (int columna = 0; columna < posiciones.length; columna++) {
            if (es_Seguro(posiciones, filaActual, columna)) {
                posiciones[filaActual] = columna;
                if (explorar_Tablero(posiciones, filaActual + 1)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    static boolean es_Seguro(int[] posiciones, int fila_Ocupada, int columna_Ocupada) {
        for (int fila_Actual = 0; fila_Actual < fila_Ocupada; fila_Actual++) {
            if (posiciones[fila_Actual] == columna_Ocupada || 
                posiciones[fila_Actual] - fila_Actual == columna_Ocupada - fila_Ocupada || 
                posiciones[fila_Actual] + fila_Actual == fila_Ocupada + columna_Ocupada) {
                return false;
            }
        }
        return true;
    }
    
    
    public static void main(String[] args) {
        int[] posiciones = new int[8];
        int[][] tablero = new int[8][8];
        for (int fila = 0; fila < 8; fila++) {
            for (int columna = 0; columna < 8; columna++) {
                tablero[fila][columna] = 0;
            }
        }
        explorar_Tablero(posiciones, 0);
        for (int fila = 0; fila < 8; fila++) {
            for (int columna = 0; columna < 8; columna++) {
                if (posiciones[fila] == columna) {
                    tablero[fila][columna] = 1;
                }
            }
        }
        imprimirTablero(tablero);
    }
}               