package applikasjon;

import java.text.Collator;
import java.util.ArrayList;
import java.util.List;

public class Person implements Comparable<Person> {
    private String enavn, fnavn, gateadresse;
    //Referanse til postadresseobjektet:
    private Postadresse postadresse;
    //Liste med referanser til bilene en person eier:
    List<Bil> biler = new ArrayList<>();

    //Kollator:
    private final static Collator KOLLATOR = Collator.getInstance();

    public Person(String fnavn, String enavn, String gateadresse, Postadresse postadresse) {
        this.fnavn = fnavn;
        this.enavn = enavn;
        this.gateadresse = gateadresse;
        this.postadresse = postadresse;
    }

    public String getFnavn() {
        return fnavn;
    }

    public void setFnavn(String fnavn) {
        fnavn = fnavn;
    }

    public String getEnavn() {
        return enavn;
    }

    public void setEnavn(String enavn) {
        enavn = enavn;
    }

    public String getGateadresse() {
        return gateadresse;
    }

    public void setGateadresse(String gateadresse) {
        this.gateadresse = gateadresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public void setPostadresse(Postadresse postadresse) {
        this.postadresse = postadresse;
    }

    public List<Bil> getBiler() {
        return biler;
    }

    public void regBil(Bil bil) {
        biler.add(bil);
    }

    @Override
    public String toString() {
        return "Person{" +
                "Fnavn='" + fnavn + '\'' +
                ", Enavn='" + enavn + '\'' +
                ", gateadresse='" + gateadresse + '\'' +
                ", postadresse=" + postadresse +
                ", biler=" + biler +
                '}';
    }

    public String toFile() {
        return enavn + ";" + fnavn + ";" + gateadresse + ";" + postadresse.getPostnr();
    }

    public int compareTo(Person pers) {
        return KOLLATOR.compare(this.enavn, pers.getEnavn());
    }

    public String alleBiler() {
        String bilut = "";
        for (int i = 0; i < biler.size(); i++) {
            bilut += biler.get(i).toString();
            bilut += "\n";
    }
}
