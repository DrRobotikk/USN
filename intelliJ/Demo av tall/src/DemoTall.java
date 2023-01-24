import javax.swing.*;
import java.util.Formatter;

public class DemoTall {
    public static void main(String[] args) {
        String lestTall = JOptionPane.showInputDialog("Skriv et tall:");
        int tall1 = Integer.parseInt(lestTall);
        lestTall = JOptionPane.showInputDialog("Skriv et tall til:");
        int tall2 = Integer.parseInt(lestTall);
        //Foretar heltallsdivisjon:
        int svar = tall1/tall2;

        //Så presenterer vi svaret:
        JOptionPane.showMessageDialog(null, "En heltallsdivisjon av " + tall1 + " og" + tall2 + " gir resultatet " + svar);

        //Utfører en vanlig divisjon:
        double svar2 = (double)tall1/tall2;
        JOptionPane.showMessageDialog(null, "Vanlig divisjon gir svaret " + svar2);

        //Bruker modulus (restdivisjon):
        int rest = tall1%tall2;
        JOptionPane.showMessageDialog(null, "Restdivisjonen blir " + rest);

        //Tester formatering i konsollet:
        System.out.printf("%.2f", svar2);

        //Vi skal så formatere utskrift i meldingsnboks:
        //Oppretter et objekt av klassen formatter:
        Formatter f = new Formatter();
        //formatterer desimaltallet:
        f.format("%.2f", svar2);
        JOptionPane.showMessageDialog(null, f.toString());

    }
}
