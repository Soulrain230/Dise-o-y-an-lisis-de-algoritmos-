/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package caballo;

/**
 *
 * @author cuaut
 */
public class Caballo {
    // Movimientos posibles del caballo en el tablero de ajedrez

    static final int[] movimiento_Y = {-1, -2, -2, -1, 1, 2, 2, 1};
    static final int[] movimiento_X = {-2, -1, 1, 2, 2, 1, -1, -2};
    
   // Devuelve 'true' si la casilla está disponible (es decir, no ha sido visitada antes) y 'false' en caso contrario.
   // También maneja excepciones en caso de que las coordenadas dadas estén fuera del tablero.
    static boolean casillaDisponible(int[][] tablero, int x, int y) {
        try {
            return tablero[x][y] == 0;
        } catch (ArrayIndexOutOfBoundsException ex) {
            return false;
        }
    }

    // Imprime el tablero de ajedrez actual
    // Un valor de '0' indica que la casilla no ha sido visitada, mientras que cualquier otro número indica el orden en el que fue visitada.
    static void HacerTablero(int[][] tablero) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print("[" + tablero[i][j] + "]  ");
            }
            System.out.println("");
        }
        System.out.println("\n\n");
    }
    // Implementa el algoritmo de backtracking para resolver el problema del recorrido del caballo
    // Comienza con un movimiento dado y continúa con los siguientes movimientos posibles.
    // Si no se encuentra ningún movimiento posible, retrocede y prueba con el siguiente movimiento.
    static boolean Recorrido(int[][] tablero, int x, int y, int cantMovimientos) {
        if (cantMovimientos == 65) {
            return true;
        }
        if (casillaDisponible(tablero, x, y)) {
            tablero[x][y] = cantMovimientos;
            for (int i = 0; i < 8; i++) {
                int sigX = x + movimiento_X[i];
                int sigY = y + movimiento_Y[i];
                if (Recorrido(tablero, sigX, sigY, cantMovimientos + 1)) {
                    return true;
                }
            }
            tablero[x][y] = 0;
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] casillas = new int[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                casillas[i][j] = 0;
            }
        }
        if (Recorrido(casillas, 0, 0, 1)) {

        }
        HacerTablero(casillas);
    }
}
