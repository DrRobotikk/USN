package TrondAssosiassjoner;

import java.util.ArrayList;
import java.util.Collections;

//Denne klassen skal kontrollere alle objektene til de tre klassene:
public class Kontroll {
    //Vi trenger en arraylist for hver type objekt:
    private ArrayList<Person> personer = new ArrayList<>();
    private ArrayList<Postadresse> postadresser = new ArrayList<>();
    private ArrayList<Kjøretøy> kjøretøy = new ArrayList<>();

    //Metoder for å operere på datastrukturene:
    public void nyPerson(Person person) {
        personer.add(person);
    }

    public void nyttKjøretøy(Kjøretøy k) {
        kjøretøy.add(k);
    }

    public void nyPostadresse(int postnr, String poststed) {
        postadresser.add(new Postadresse(postnr, poststed));
    }

    //Vi trenger også søkemetoder:
    public Person finnPerson(String navn) {

        Collections.sort(personer);
        Person dummy = new Person(navn, null, null);
        int indeks = Collections.binarySearch(personer, dummy);

        if (indeks >=0) return personer.get(indeks);
        else return null;

    }

    public Kjøretøy finnKjøretøy(String regnr) {

        Collections.sort(kjøretøy);
        Kjøretøy dummy = new Kjøretøy(regnr, null, null);
        int indeks = Collections.binarySearch(kjøretøy, dummy);

        if (indeks >=0) return kjøretøy.get(indeks);
        else return null;
    }

    public Postadresse finnPostadresse(int postnr) {

        Collections.sort(postadresser);
        Postadresse dummy = new Postadresse(postnr, null);
        int indeks = Collections.binarySearch(postadresser, dummy);

        if (indeks >= 0) return postadresser.get(indeks);
        else return null;

    }

    //Nyttig med metoder for å returnere referanser til datastrukturene:
    public ArrayList<Person> getPersoner() {
        return personer;
    }

    public ArrayList<Kjøretøy> getKjøretøy() {
        return kjøretøy;
    }

    public ArrayList<Postadresse> getPostadresser() {
        return postadresser;
    }

}
