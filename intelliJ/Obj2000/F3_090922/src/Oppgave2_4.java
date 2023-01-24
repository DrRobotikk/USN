import javax.swing.*;
import java.util.Formatter;

public class Oppgave2_4 {

    public static void main(String[] args) {
        //dagens kurs
        double kurs = 8.89;

        // Leser inn dollars $$$$$$$$$$$:
        double usd = Double.parseDouble(JOptionPane.showInputDialog("Oppgi usd: "));

        //regner om til nok:
        double nok = usd*kurs;

        //formaterer til 2 desimaler:
        Formatter fNok = new Formatter();
        fNok.format("%.2f", nok);

        //utskrift:
        JOptionPane.showMessageDialog(null, fNok.toString());



    }
}
