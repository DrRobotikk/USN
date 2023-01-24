package romanDyr;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    private ArrayList<Gaupe> gauper = new ArrayList<>();

    public void nyGaupe(String kjonn,Float lengde, Float vekt, Float tuss, String dato, String sted) {
        String id = "G" + (gauper.size()+1);
        gauper.add(new Gaupe(id,kjonn,lengde,vekt,tuss,dato,sted));
    }
    public void gjenGaupe(String id,Float lengde, Float vekt, Float tuss, String dato, String sted) {
        for (Gaupe gaupe: gauper) {
            if (gaupe.getId().equals(id)) {
                gaupe.getGjenfangst().add(new Gjenfangst(id,lengde,vekt,tuss,dato,sted));
            }
        }
    }

    public Gaupe finnGaupeBinaert(String id) {
        Collections.sort(gauper);
        Gaupe dummy = new Gaupe(id);
        int indeks = Collections.binarySearch(gauper, dummy);
        if (indeks>=0) return gauper.get(indeks);
        else return null;
    }
    public Gjenfangst gjenfangst(String id) {
        Boolean funnet = false;
        for (Gaupe gaupe : gauper) {
            if (gaupe.getId().equals(id)) {
                funnet = true;
            }
            Collections.sort(gaupe.getGjenfangst());
            Gjenfangst dummy = new Gjenfangst(id);
            int indeks = Collections.binarySearch(gaupe.getGjenfangst(), dummy);
            if (indeks>=0) return gaupe.getGjenfangst().get(indeks);
            else return null;
        }
    }

    public ArrayList<Gaupe> getGauper() {
        return gauper;
    }

}

