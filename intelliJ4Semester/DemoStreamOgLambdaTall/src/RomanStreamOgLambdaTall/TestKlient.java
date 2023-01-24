package RomanStreamOgLambdaTall;

import javax.swing.*;

public class TestKlient {
    public static void main(String[] args) {
        start();
    }

    static Kontroll kontroll = new Kontroll();
    public static final String[] MENY= {"Oppgi tall","Lambda","Stream","Avslutt"};
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
                case 0 : lesTall();
                break;
                case 1 : lambda();
                break;
                case 2 : stream();
                break;
                default: fortsett = false;
            }
        }
    }
    public static int [] lesTall() {
        int [] tall = new int[2];
        int deletall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi deletall: "));
        int makstall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi maks tall: "));
        tall[0] = deletall;
        tall[1] = makstall;

        return tall;
    }
    public static void lambda() {
        System.out.println("Lambda");
    }
    public static void stream() {
        System.out.println("Stream");
    }
}
