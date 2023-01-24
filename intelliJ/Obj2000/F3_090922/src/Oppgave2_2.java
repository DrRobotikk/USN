import javax.swing.*;

public class Oppgave2_2 {

    public static void main(String[] args) {
        //Leser lengde og bredde på et rektangel:
        //først lengden:
        String lestLengde = JOptionPane.showInputDialog("Skriv lengden:");

        //Konverterer til desimaltall:
        double lengde = Double.parseDouble(lestLengde);

        //Leser bredden til rektangelet i en setning:
        double bredde = Double.parseDouble(JOptionPane.showInputDialog("Skriv bredde:"));
        JOptionPane.showMessageDialog(null, "Areal: " + lengde*bredde);
    }
}
