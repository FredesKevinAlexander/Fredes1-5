import java.util.Scanner;

public class LongitudCadena {
    public static void main(String[] args) {

        System.out.print("Escriba una palabra: ");
        Scanner scanner = new Scanner(System.in); 

        String texto = scanner.nextLine(); 
        int longitud = texto.length();
        
        System.out.println("Longitud: " + longitud);

        scanner.close(); 
    }
}
