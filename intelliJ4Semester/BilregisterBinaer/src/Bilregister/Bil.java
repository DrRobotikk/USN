package Bilregister;

import java.io.Serializable;
import java.text.Collator;

public class Bil implements Serializable, Comparable<Bil> {
    private String regnr, merke, modell;
    //Referanse til eieren:
    private Person eier;
    //Lager et kollator-objekt for å kunne sortere med æ, ø, å:
    private final static Collator KOLLATOR = Collator.getInstance();

    public Bil(String regnr, String merke, String modell, Person eier) {
        this.regnr = regnr;
        this.merke = merke;
        this.modell = modell;
        this.eier = eier;
    }

    public String getRegnr() {
        return regnr;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public String getMerke() {
        return merke;
    }

    public void setMerke(String merke) {
        this.merke = merke;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public Person getEier() {
        return eier;
    }

    public void setEier(Person eier) {
        this.eier = eier;
    }


    @Override
    public String toString() {
        return "Bil{" +
                "regnr='" + regnr + '\'' +
                ", merke='" + merke + '\'' +
                ", modell='" + modell + '\'' +
                ", eier=" + eier +
                '}';
    }
    @Override
    public int compareTo(Bil bil) {
        //Sorterer på regnr:
        return KOLLATOR.compare(this.regnr, bil.getRegnr());
    }

    public String toFile() {
        return regnr + ";" + merke + ";" + modell + ";" + eier.getEnavn();
    }
}
