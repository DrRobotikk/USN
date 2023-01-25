package TrondHASH;

import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.TreeMap;

public class Kontroll {
    private HashMap<String, Person> personer = new HashMap<>();
    //For å gå fra HashMap til TreeMap, gjør man følgende:
    //private TreeMap<String, Person> personer = new TreeMap<>();

    public void settInn(Person person) {
        //Henter ut navn:
        String navn = person.getNavn();
        //Legger navn inn i HashMap():
        personer.put(navn, person);
    }

    public Person finnPerson(String nokkel) {
        return personer.get(nokkel);
    }

    public Iterator<Person> getPersoner() {
        Collection<Person> verdier = personer.values();
        return verdier.iterator();
    }
}
