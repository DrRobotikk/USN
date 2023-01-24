package KollarOblig2;
//KONTROLLKLASSE:

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    //OPPRETTER LISTER FOR DYRENE
    private ArrayList<Gaupe> gauper = new ArrayList<>();
    private ArrayList<Hare> harer = new ArrayList<>();
    private ArrayList<NyGaupe> nyeGauper = new ArrayList<>();
    private ArrayList<NyHare> nyeHarer = new ArrayList<>();

    //FUNKSJON - AUTOGENERERING AV ID OG REGISTRERING AV GAUPE:
    public void regGaupe(String kjonn, Float lengde, Float vekt, String dato, String sted, Float tuss) {
        String id = "G" +(gauper.size() + 1);
        gauper.add(new Gaupe(id,kjonn,lengde,vekt,dato,sted,tuss));
        //ALT OK
    }

    //FUNKSJON - AUTOGENERERING AV ID OG REGISTRERING AV HARE:
    public void regHare(String kjonn,Float lengde,Float vekt,String dato,String sted,String type,String pels) {
        String id = "H" +(harer.size() + 1);
        harer.add(new Hare(id,kjonn,lengde,vekt,type,pels,dato,sted));
        //ALT OK
    }
    //FUNKSJON - REGISTRERING AV GAUPEGJENFANGST:
    public void regGjenGaupe(String ID, Float lengde, Float vekt, String dato, String sted, Float tuss) {
        nyeGauper.add(new NyGaupe(ID,lengde,vekt,dato,sted,tuss));

    }

    //FUNKSJON - REGISTRERING AV HAREGJENFANGST:
    public void regGjenHare(String ID, Float lengde, Float vekt, String dato, String sted, String pels) {
            nyeHarer.add(new NyHare(ID,lengde,vekt,dato,sted,pels));
        //ALT OK
    }

    //FUNKSJON - BINÆRT SØK I GAUPELISTE:
    public Gaupe finnGaupeBinaert(String ID) {
        Collections.sort(gauper);
        Gaupe dummy = new Gaupe(ID,null,null,null,null,null,null);
        int indeks = Collections.binarySearch(gauper, dummy);
        if (indeks>=0) return gauper.get(indeks);
        else return null;
        //ALT OK
    }

    //FUNKSJON - BINÆRT SØK I HARELISTE:
    public Hare finnHareBinaert(String ID) {
        Collections.sort(harer);
        Hare dummy = new Hare(ID,null,null,null,null,null,null,null);
        int indeks = Collections.binarySearch(harer, dummy);
        if (indeks>=0) return harer.get(indeks);
        else return null;
        //ALT OK
    }

    //FUNKSJON - LINJÆRT SØK FOR GJENFANGST AV GAUPE
    public String finnGjenGaupeLinjaert(String ID) {
        Boolean funnetGaupe = false;
        String gaupeListe = "";
        for (int i = 0; i< nyeGauper.size(); i++) {
            NyGaupe id = nyeGauper.get(i);
            if (id.getID().equals(ID)) {
                funnetGaupe = true;
                gaupeListe += nyeGauper.get(i);
            }
        }
        if (funnetGaupe.equals(true)) return gaupeListe;
        else return null;
    }

    //FUNKSJON - LINJÆRT SØK FOR GJENFANGST AV HARE:
    public String finnGjenHareLinjaert(String ID) {
        Boolean funnetHare = false;
        String hareListe = "";
        for (int i = 0; i< nyeHarer.size(); i++) {
            NyHare id = nyeHarer.get(i);
            if (id.getID().equals(ID)) {
                funnetHare = true;
                hareListe += nyeHarer.get(i);
            }
        }
        if (funnetHare.equals(true)) return hareListe;
        else return null;
    }

    //GETTER FOR ALLE LISTER:
    public ArrayList<Gaupe> getGauper() {
        return gauper;
    }
    public ArrayList<Hare> getHarer() {
        return harer;
    }
    public ArrayList<NyGaupe> getNyeGauper() {
        return nyeGauper;
    }
    public ArrayList<NyHare> getNyeHarer() {
        return nyeHarer;
    }
}
