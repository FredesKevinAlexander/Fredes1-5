import javax.swing.JOptionPane;
import java.util.Random;

public class PiedraPapelTijera {
    public static void main(String[] args) {
        Random random = new Random();
        String[] opciones = {"Piedra(0)", "Papel(1)", "Tijera(2)"};

        int victoriasJugador = 0;
        int victoriasComputadora = 0;

        JOptionPane.showMessageDialog(null, "¡Vamos a jugar al mejor de 3!");

        while (victoriasJugador < 2 && victoriasComputadora < 2) {
            // Elección del el jugador
            int eleccionJugador = JOptionPane.showOptionDialog(
                null,
                "Elige tu opción:",
                "Piedra, Papel o Tijera",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.QUESTION_MESSAGE,
                null,
                opciones,
                opciones[0]
            );

            // Cancelar si el usuario cierra la ventana
            if (eleccionJugador == -1) {
                JOptionPane.showMessageDialog(null, "Juego cancelado.");
                return;
            }

            // Elección de la computadora
            int eleccionComputadora = random.nextInt(3);

            String mensaje = "Jugador elige: " + opciones[eleccionJugador] + "\n";
            mensaje += "Computadora elige: " + opciones[eleccionComputadora] + "\n";

            //resultado de la ronda
            if (eleccionJugador == eleccionComputadora) {
                mensaje += "Resultado: ¡Empate!";
            } else if (
                (eleccionJugador == 0 && eleccionComputadora == 2) || // Piedra gana
                (eleccionJugador == 1 && eleccionComputadora == 0) || // Papel gana
                (eleccionJugador == 2 && eleccionComputadora == 1)    // Tijera gana
            ) {
                mensaje += "Resultado: ¡Ganaste esta ronda!";
                victoriasJugador++;
            } else {
                mensaje += "Resultado: ¡Computadora gana esta ronda!";
                victoriasComputadora++;
            }

            mensaje += "\n\nMarcador:\nJugador: " + victoriasJugador + " - Computadora: " + victoriasComputadora;

            JOptionPane.showMessageDialog(null, mensaje);
        }

        // Mostrar elrersultado final
        String resultadoFinal = (victoriasJugador == 2) ? "¡Felicidades! Ganaste la partida." : "La computadora ganó la partida.";
        JOptionPane.showMessageDialog(null, resultadoFinal + "\nResultado final:\nJugador: " + victoriasJugador + " - Computadora: " + victoriasComputadora);
    }
}
