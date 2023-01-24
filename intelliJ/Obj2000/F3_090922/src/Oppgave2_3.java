import javax.swing.*;
import java.util.Formatter;

public class Oppgave2_3 {
    public static void main(String[] args) {
        //Leser radius for en sirkel:
        String lestRadius = JOptionPane.showInputDialog("Skriv sirkelens radius:");
        double radius = Double.parseDouble(lestRadius);

        //Arealet av en sirkel er pi*radius*radius:
        double areal = Math.PI*radius*radius;

        //Formaterer arealet til færre desimaltall:
        Formatter fAreal = new Formatter();
        fAreal.format("%.1f", areal);

        JOptionPane.showMessageDialog(null, "Arealet er " + fAreal.toString());

    }
}
