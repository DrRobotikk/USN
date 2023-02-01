package LagreDemo;

import Hjelpeklasser.Filbehandling;

import java.io.PrintWriter;
import java.util.ArrayList;

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
}
