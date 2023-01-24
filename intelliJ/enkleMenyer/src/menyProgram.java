import javax.swing.*;

public class menyProgram {
    //Definerer knappene i menyen
    private static final String[] ALTERNATIVER = {"Gjør ditt", "Gjør datt", "Avslutt"};

    //class main
    public static void main(String[] args) {
        //starter alt tydeligvis
        start();
    }

    // Metode for å lage meny og returnere menyvalget:
    public static int lesValg() {
        //Lager menyen og leser valget:
        int valg = JOptionPane.showOptionDialog(
                null, //Vi gjør ikke noe med den
                "Velg hva som skal gjøres", //Ledetekst
                null, //Gjør ikke noe med den
                JOptionPane.DEFAULT_OPTION, //Bruker default
                JOptionPane.PLAIN_MESSAGE, //Bruker default
                null, //Bryr oss ikke om denne
                ALTERNATIVER, //Listen med menyvalg
                ALTERNATIVER[0]); //Default menyvalg
        return valg;
    }

    //Metode for å lese menyvalg helt til vi velger Avslutt:
    public static void start() {
        //Definerer en boolsk for å kontrollere en løkke:
        boolean fortsett = true;

        //Starter en løkke:
        while (fortsett) {
            //Kaller menyvalgmetoden lesValg():
            int valg = lesValg();

            //Bruker en case-blokk til å bestemme handling:
            switch (valg) {
                case 0 : System.out.println("Du valgte å gjøre ditt");
                break;
                case 1 : System.out.println("Du valgte å gjøre datt");
                break;
                default : fortsett= false;
            }
        }

    }
}
