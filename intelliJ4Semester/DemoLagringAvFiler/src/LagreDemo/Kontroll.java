package LagreDemo;

import Hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Kontroll {
    //Datastruktur:
    private ArrayList<Person> personer = new ArrayList<>();

    //Metode for å legge til person:
    public void nyPerson(Person person) {
        personer.add(person);
    }

    //Metode for å lagre objektene:
    public void skrivData(String filnavn) {
        try {
            //Lager en skriveforbindelse:
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            //Går gjennom datastrukturen:
            for (Person p : personer) {
                utfil.println(p.toFile());
            }
            utfil.close();
        } catch (Exception e) {
        }
    }

    public ArrayList<Person> getPersoner() {
        return personer;
    }

    public void empty() {
        personer.clear();
    }

    //Metode for å lese filen og gjennopprettet objektet:
    public void lesData(String filnavn) {
        //Tømmer personer-lista:
        empty();
        //Innlesing:
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            //Leser inn en linje:
            String linje = innfil.readLine();
            //Starter en løkke:
            while (linje != null) {
                //Opprette et StringTokenizer-objekt:
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                //Leser ut attributtverdiene:
                String navn = innhold.nextToken();
                String adresse = innhold.nextToken();
                int fodselsar = Integer.parseInt(innhold.nextToken());
                //Lager et personobjekt og legger inn i Arraylisten:
                personer.add(new Person(navn, adresse, fodselsar));
                //Leser så neste linje i fila:
                linje = innfil.readLine();
            }//Ferdig med løkka
            innfil.close();
        } catch (Exception e) {
        }
    }
}
