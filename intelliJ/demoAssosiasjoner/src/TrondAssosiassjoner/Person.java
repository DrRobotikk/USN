package TrondAssosiassjoner;

import java.util.ArrayList;

public class Person implements Comparable<Person>{
    private String navn; //Vi later som at navn er unikt og bruker det som identifikator
    private String adresse;
    //Referanse til klassen Postadresse:
    Postadresse postadresse;

    private ArrayList<Kjøretøy> kjøretøyliste = new ArrayList<>();

    public Person(String navn, String adresse, Postadresse postadresse) {
        this.navn = navn;
        this.adresse = adresse;
        this.postadresse = postadresse;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public void setPostadresse(Postadresse postadresse) {
        this.postadresse = postadresse;
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", postadresse=" + postadresse.toString() +
                '}';
    }

    //compareTo og equals skal nå sammenligne strenger:

    public int compareTo(Person person) {
        return this.navn.compareTo(person.getNavn());
    }

    public boolean equals(Person person) {
        return this.navn.equals(person.getNavn());
    }
}
