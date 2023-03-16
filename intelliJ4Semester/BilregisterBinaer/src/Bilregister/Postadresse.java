package Bilregister;

import java.io.Serializable;
import java.text.Collator;

public class Postadresse implements Serializable, Comparable<Postadresse> {
    private String postnr, poststed;
    //Kollator:
    private final static Collator KOLLATOR = Collator.getInstance();

    public Postadresse(String postnr, String poststed) {
        this.postnr = postnr;
        this.poststed = poststed;
    }

    public String getPostnr() {
        return postnr;
    }

    public void setPostnr(String postnr) {
        this.postnr = postnr;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    public static Collator getKollator() {
        return KOLLATOR;
    }

    @Override
    public String toString() {
        return "Postadresse{" +
                "postnr='" + postnr + '\'' +
                ", poststed='" + poststed + '\'' +
                '}';
    }

    public String toFile() {
        return postnr + ";" + poststed;
    }

    public int compareTo(Postadresse p) {
        //Bruker KOLLATOR's metode compare():
        return KOLLATOR.compare(this.postnr, p.getPostnr());
    }

    public boolean equals(Postadresse p) {
        //Bruker KOLLATOR's metode equals():
        return KOLLATOR.equals(this.postnr,p.getPostnr());
    }
}
