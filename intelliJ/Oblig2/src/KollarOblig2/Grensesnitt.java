package KollarOblig2;
//GRENSESNITTKLASSE:

import javax.swing.*;
import java.util.ArrayList;

public class Grensesnitt {

    Kontroll kontroll = new Kontroll();

    // EN ARRAY MED MENYKNAPPER
    private static final String[] HOVEDMENY = {"Registrer gaupe","Registrer hare",
            "Registrer gaupegjenfangst","Registrer haregjenfangst",
            "Finn dyr","List ut dyr","Dyr med fangst","Avslutt"};

    //FUNKSJON - VISER MENYEN OG BER BRUKEREN OPPGI HVA SOM SKAL GJØRES:
    public int lesValg() {
        int valg = JOptionPane.showOptionDialog(null,"Velg hva som skal gjøres",
                "Registrering av dyr",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,
                null,HOVEDMENY,HOVEDMENY[0]);
        return valg;
    }

    //FUNKSJON - BRUKEREN OPPGIR DATA SOM SKAL SETTES I GAUPELISTE
    public void lesGaupe() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn").toUpperCase();
        Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Oppgi lende"));
        Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Oppgi vekt"));
        Float tuss = Float.parseFloat(JOptionPane.showInputDialog("Oppgi tuss"));
        String dato = JOptionPane.showInputDialog("Oppgi dato");
        String sted = JOptionPane.showInputDialog("Oppgi sted").toUpperCase();
        kontroll.regGaupe(kjonn,lengde,vekt,dato,sted,tuss);
    }

    //FUNKSJON - BRUKEREN OPPGIR DATA SOM SKAL SETTES I HARELISTE
    public void lesHare() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn").toUpperCase();
        Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Oppgi lende"));
        Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Oppgi vekt"));
        String type = JOptionPane.showInputDialog("Oppgi type").toUpperCase();
        String pels= JOptionPane.showInputDialog("Oppgi pels").toUpperCase();
        String dato = JOptionPane.showInputDialog("Oppgi dato");
        String sted = JOptionPane.showInputDialog("Oppgi sted").toUpperCase();
        kontroll.regHare(kjonn,lengde,vekt,dato,sted,type,pels);
    }

    //FUNKSJON - BRUKEREN OPPGIR DATA SOM SKAL SETTES I GJENFANGST-GAUPELISTE
    //SJEKKER OGSÅ OM DYRET FINNES FRA FØR
    public void lesGjenfangstGaupe() {
        String id = JOptionPane.showInputDialog("Oppgi id").toUpperCase();
        Gaupe gaupe = kontroll.finnGaupeBinaert(id);
        if (gaupe != null) {
            Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Oppgi lengde"));
            Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Oppgi vekt"));
            Float tuss = Float.parseFloat(JOptionPane.showInputDialog("Oppgi tusselengde"));
            String dato = JOptionPane.showInputDialog("Oppgi dato");
            String sted = JOptionPane.showInputDialog("Oppgi sted").toUpperCase();
            kontroll.regGjenGaupe(id, lengde, vekt, dato, sted, tuss);
        }else JOptionPane.showMessageDialog(null, "Finner ikke gaupen med denne ID'en");
    }

    //FUNKSJON - BRUKEREN OPPGIR DATA SOM SKAL SETTES I GJENFANGST-HARELISTE
    //SJEKKER OGSÅ OM DYRET FINNES FRA FØR
    public void lesGjenfangstHare() {
        String id = JOptionPane.showInputDialog("Oppgi id").toUpperCase();
        Hare hare = kontroll.finnHareBinaert(id);
        if (hare != null) {
            Float lengde = Float.parseFloat(JOptionPane.showInputDialog("Oppgi lende"));
            Float vekt = Float.parseFloat(JOptionPane.showInputDialog("Oppgi vekt"));
            String pels= JOptionPane.showInputDialog("Oppgi pels").toUpperCase();
            String dato = JOptionPane.showInputDialog("Oppgi dato");
            String sted = JOptionPane.showInputDialog("Oppgi sted").toUpperCase();
            kontroll.regGjenHare(id, lengde, vekt, dato, sted, pels);
        } else JOptionPane.showMessageDialog(null,"Finner ikke haren med denne ID'en");
    }

    //FUNKSJON - OPPGI DYRETS ID, PROGRAMMET SKRIVER UT DYRETS DATA OG GJENFANGSTDATA
    public void lesFinnDyr() {
        String id = JOptionPane.showInputDialog("Oppgi ID").toUpperCase();
        Gaupe gaupe= kontroll.finnGaupeBinaert(id);
        String gaupe1 = kontroll.finnGjenGaupeLinjaert(id);
        Hare hare = kontroll.finnHareBinaert(id);
        String hare1 = kontroll.finnGjenHareLinjaert(id);

        if (gaupe !=null) System.out.println("Første registrering av gaupe:"+"\n"+gaupe.toString());

        if (gaupe1 !=null) System.out.println("Gjenfangst data for gaupe:"+"\n"+gaupe1.toString());

        if (hare !=null) System.out.println("Første registrering av hare:"+"\n"+hare.toString());

        if (hare1 !=null) System.out.println("Gjenfangst data for hare:"+"\n"+hare1.toString());
    }

    //FUNKSJON - LIST DYR MED DATA OG GJENFANGSTDATA:
    public void lesListDyr() {
        ArrayList<Gaupe> gauper = kontroll.getGauper();
        ArrayList<NyGaupe> nyeGauper = kontroll.getNyeGauper();
        ArrayList<Hare> harer = kontroll.getHarer();
        ArrayList<NyHare> nyeHarer = kontroll.getNyeHarer();
        String gaupe = "";
        String gaupe1 = "";
        String hare = "";
        String hare1 = "";
        for (Gaupe g : gauper) {
            gaupe+= g.toString() + "\n";
        }
        for (NyGaupe ng : nyeGauper) {
            gaupe1+= ng.toString();
        }
        for (Hare h : harer) {
            hare+= h.toString() + "\n";
        }
        for (NyHare nh : nyeHarer) {
            hare1+= nh.toString();
        }
        System.out.println("Første registrering av gaupe:" + "\n" + gaupe + "Gjenfangst:" + "\n" + gaupe1 + "\n" +
                "Første registrering av hare:" + "\n" + hare + "Gjenfangst:" + "\n" + hare1);
    }


    //FUNKSJON - GJENFANGSTDATA FOR ALLE DYR
    //TILBAKEMELDING DERSOM DYRET IKKE HAR GJENFANGST:
    public void lesDyrMedFangst() {
       ArrayList<NyGaupe> gaupeGjenfangst = kontroll.getNyeGauper();
       ArrayList<NyHare> hareGjenfangst = kontroll.getNyeHarer();
       String utGjenGaupe = "";
       String utGjenHare = "";
       for (NyGaupe nyGaupe : gaupeGjenfangst) {
           utGjenGaupe+=nyGaupe.toString();
       }
       for (NyHare nyHare : hareGjenfangst) {
           utGjenHare+=nyHare.toString();
       }
       if (utGjenGaupe.isEmpty()) System.out.println("Ingen gjenfangstdata registrert for Gaupe");
        else System.out.println("Gjenfangstdata for Gaupe:"+"\n"+utGjenGaupe);
        if (utGjenHare.isEmpty()) System.out.println("Ingen gjenfangstdata for Hare");
        else System.out.println("Gjenfangstdata for Hare:"+"\n"+utGjenHare);
    }

    //FUNKSJON - MENYEN KJØRES SÅ LENGE MAN IKKE TRYKKER AVSLUTT:
    public void start() {

        boolean fortsett = true;

        while (fortsett) {
            int valg = lesValg();

            switch (valg) {
                case 0 :
                    lesGaupe();
                    break;
                case 1 :
                    lesHare();
                    break;
                case 2 :
                    lesGjenfangstGaupe();
                    break;
                case 3 :
                    lesGjenfangstHare();
                    break;
                case 4 :
                    lesFinnDyr();
                    break;
                case 5 :
                    lesListDyr();
                    break;
                case 6 :
                    lesDyrMedFangst();
                    break;
                default: fortsett = false;
            }
        }
    }
}
