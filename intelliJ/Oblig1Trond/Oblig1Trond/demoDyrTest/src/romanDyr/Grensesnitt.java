package romanDyr;

import javax.swing.*;
import java.util.ArrayList;

public class Grensesnitt {
    Kontroll kontroll = new Kontroll();

    private final String[] KNAPPER = {"Gaupe","Finn gaupe","Skriv gaupe","Gjenfangst","Avslutt"};

    public int lesValg() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres","Registrering av ny Gaupe",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,KNAPPER,KNAPPER[0]);
        return valg;
    }

    public void start() {
        boolean fortsett = true;
        while(fortsett) {
            int valg = lesValg();
            switch(valg) {
                case 0 : nyGaupe();
                break;
                case 1 : finnGaupe();
                break;
                case 2 : skrivGaupe();
                break;
                case 3 : gjenGaupe();
                break;
                default: fortsett = false;
            } //switch
        } //while
    }

    public void nyGaupe() {
        //Id'en blir autogenerert i kontroll så trenger den ikke her!!!
        //String id = JOptionPane.showInputDialog("ID");
        String kjonn = JOptionPane.showInputDialog("Kjønn");
        Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Lengde"));
        Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Vekt"));
        Float tuss = Float.parseFloat(JOptionPane.showInputDialog("Tusselengde"));
        String dato = JOptionPane.showInputDialog("Dato");
        String sted = JOptionPane.showInputDialog("Sted");

        kontroll.nyGaupe(kjonn,lengde,vekt,tuss,dato,sted);
    }
    public void gjenGaupe() {
        //Id'en blir autogenerert i kontroll så trenger den ikke her!!!
        String id = JOptionPane.showInputDialog("ID");
        Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Lengde"));
        Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Vekt"));
        Float tuss = Float.parseFloat(JOptionPane.showInputDialog("Tusselengde"));
        String dato = JOptionPane.showInputDialog("Dato");
        String sted = JOptionPane.showInputDialog("Sted");

        kontroll.gjenGaupe(id,lengde,vekt,tuss,dato,sted);
    }
    public void finnGaupe() {
        String id = JOptionPane.showInputDialog("Oppgi ID");
        Gaupe gaupe = kontroll.finnGaupeBinaert(id);
        if (gaupe !=null) JOptionPane.showMessageDialog(null,gaupe.toString());
        else JOptionPane.showMessageDialog(null,"Finner ikke gaupa.");
    }
    public void skrivGaupe() {
        ArrayList<Gaupe> gauper = kontroll.getGauper();
        String tekst = "";
        for (Gaupe g : gauper) {
            tekst+=g.toString() + "\n";
        }
        JOptionPane.showMessageDialog(null, tekst);

    }
}
