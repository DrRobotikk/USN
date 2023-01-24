package no.gmailromankollar77DiktGenerator;

import no.gmailromankollar77DiktGenerator.Kontroll;

import javax.swing.*;

public class Grensesnitt {

    Kontroll kontroll = new Kontroll();
    //Definerer knappene i menyene:
    private static final String[] HOVEDMENY = {"Enkle dikt","Avanserte dikt","Avslutt"};
    private static final String[] ENKLE = {"Registrer ord","Skriv dikt","Tilbake"};
    private static final String[] AVANSERTE = {"Registrer ord","Skriv dikt","Tilbake"};
    private static final String[] ORD = {"Artikkel", "Adjektiv", "Substantiv", "Verb","Tilbake"};


    //Genererer menyene:
    public int lesValg() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres",null,JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
        return valg;
    }
    public int lesValgEnkel() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres",null,JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,ENKLE,ENKLE[0]);
        return valg;
    }
    public int lesValgAvansert() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres",null,JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,AVANSERTE,AVANSERTE[0]);
        return valg;
    }
    public int lesOrd() {
        int valg = JOptionPane.showOptionDialog(null,"Velg ord som skal lagres",null,JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,ORD,ORD[0]);
        return valg;
    }

    //Leser hovedmenyvalget frem til man trykker avslutt:
    public void start() {
        //leser inn listene med ord som finnes som default i starten av programmet:
        kontroll.lesinnLister();

        //oppretter en boolsk variabel for kontroll av løkka:
        boolean fortsett = true;

        while (fortsett) {
            int valg = lesValg();

            switch (valg) {
                case 0 : enkelMeny();
                break;
                case 1 : avansertMeny();
                break;
                default: fortsett= false;
            }
        }
    }

    //Leser enkelMenyen frem til man trykker tilbake:
    public void enkelMeny() {
        boolean fortsett = true;

        while (fortsett) {
            int valg = lesValgEnkel();

            switch (valg) {
                case 0 : oppgiNyeAlleOrd();
                break;
                case 1 : lagDikt();
                break;
                default: fortsett= false;
            }
        }
    }

    //Leser avansertMenyen frem til man trykker tilbake:
    public void avansertMeny() {
        boolean fortsett = true;

        while (fortsett) {
            int valg = lesValgAvansert();

            switch (valg) {
                case 0 : ordMeny();
                break;
                case 1 : lagAvansertDikt();
                break;
                default: fortsett= false;
            }
        }
    }

    //Leser ordMenyen frem til man trykker tilbake:
    public void ordMeny() {
        boolean fortsett = true;

        while (fortsett) {
            int valg = lesOrd();

            switch (valg) {
                case 0 : oppgiArtikkel();
                    break;
                case 1 : oppgiAdjektiv();
                    break;
                case 2 : oppgiSubstantiv();
                    break;
                case 3 : oppgiVerb();
                    break;
                default: fortsett= false;
            }
        }
    }

    //
    public void lagDikt() {
        String dikt = kontroll.enkelDikt();
        JOptionPane.showMessageDialog(null,dikt);
    }

    public void lagAvansertDikt() {
        String dikt = kontroll.avansertDikt();
        JOptionPane.showMessageDialog(null,dikt);
    }

    public void oppgiArtikkel() {

        String nyArtikkel = JOptionPane.showInputDialog("Oppgi artikkel:");
        kontroll.registrerArtikkel(nyArtikkel);
    }

    public void oppgiAdjektiv() {
        String nyttAdjektiv = JOptionPane.showInputDialog("Oppgi adjektiv:");
        kontroll.registrerAdjektiv(nyttAdjektiv);
    }

    public void oppgiSubstantiv() {
        String nyttSubstantiv = JOptionPane.showInputDialog("Oppgi substantiv:");
        kontroll.registrerSubstantiv(nyttSubstantiv);
    }

    public void oppgiVerb() {
        String nyttVerb = JOptionPane.showInputDialog("Oppgi verb:");
        kontroll.registrerVerb(nyttVerb);
    }

    public void oppgiNyeAlleOrd() {
        String nyeAlleOrd = JOptionPane.showInputDialog("Oppgi valgfrie ord:");
        kontroll.registrerAlleOrd(nyeAlleOrd);
    }
}
