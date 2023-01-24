package Stakk;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    //En kontrollKlasse skal inneholde de nødvendige datastrukturene.
    //Objekter av subklassene til Kjøretøy er også Kjøretøy:
    private ArrayList<Kjøretøy> kjøretøyliste = new ArrayList<>();

    //Forutsetter at objekt av riktig subklasse (Kjøretøy) opprettes av grensesnittet:
    public void nyttKjøretøy(Kjøretøy kjøretøy) {
        kjøretøyliste.add(Kjøretøy);
    }

    public Kjøretøy finnKjøretøy(String regnr) {
        //Vi må være sikre på at kjøretøyliste er sortert:
        //Arraylist sorteres ved hjelp av Collections.sort(listenavn);
        Collections.sort(kjøretøyliste);

        //For å kunne bruke binærsøk må vi opprette et dummy objekt
        //med det regnr vi skal søke etter:
        //Kjøretøy dummy = new Kjøretøy(regnr, null, null, 0);

        //Bruker i steden den ekstra konstruktøren vi opprettet i KjøretyKlassen:
        Kjøretøy dummy = new Kjøretøy(regnr);

        //Bruker binærsøk, som returnerer indeksen til objektet i kjøretøyliste:
        //Hvis objektet ikke finnes, returnerer den et negativt tall:
        int indeks = Collections.binarySearch(kjøretøyliste, dummy);

        //Kan også skrive if (indeks >=0)...
        if (indeks > -1) return kjøretøyliste.get(indeks);
        else return null;
    }

    //Returnerer kjøretøyliste slik at vi kan skrive ut alle kjøretøy:
    public ArrayList<Kjøretøy> getListe() {
        return kjøretøyliste;
    }
}
