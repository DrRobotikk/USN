package InterfaceTrond;

import javax.swing.*;

public class Main {

    public static void main(String[] args) {
        start();
        /*
        kontroll kontrollen = new kontroll();
        kontrollen.lambdaBruk(50, 7);
        kontrollen.loopBruk(50,7);

         */
    }
    //static kontroll kontrollen = new kontroll();

    public static final String[] MENY = {"Lambda","Løkke","Avslutt"};

    public static int lesValg() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres",
                "Sjekk om tall er delelig",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,
                null,MENY,MENY[0]);
        return valg;
    }

    public static void start() {

        boolean fortsett = true;

        while (fortsett) {
            int valg = lesValg();

            switch (valg) {
                case 0 : testLambda();
                    break;
                case 1 : testLoop();
                    break;
                default: fortsett = false;
            }
        }
    }

    public static int makstall() {
        int tall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi makstall:"));
        return tall;
    }

    public static int deletall() {
        int deletall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi deletall:"));
        return deletall;
    }

    public static void testLambda() {
        kontroll kontrollen = new kontroll();
        kontrollen.lambdaBruk(makstall(),deletall());
    }

    public static void testLoop() {
        kontroll kontrollen = new kontroll();
        kontrollen.loopBruk(makstall(),deletall());
    }
}
