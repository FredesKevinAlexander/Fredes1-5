public class ComparacionCadenas {

    public static void main (String[] args){
    
        String texto1 = "kevin";
String texto2 = "Kevin";

boolean iguales = texto1.equals(texto2);
boolean ignoraMayus = texto1.equalsIgnoreCase(texto2);

System.out.println(iguales);  
System.out.println(ignoraMayus);  
    }
}