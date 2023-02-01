package LagreDemo;

import java.util.ArrayList;

public class Testklient {
    public static void main(String[] args) {
        String filnavn = "personer.csv";
        Kontroll kontroll = new Kontroll();
        //Legger til personer:
        kontroll.nyPerson(new Person("Ole", "Gate 1", 2001));
        kontroll.nyPerson(new Person("Lise", "Gate 2", 2011));

        //Sjekker innholdet:
        System.out.println("Innholdet i datastrukturen:");
        ArrayList<Person> personer = kontroll.getPersoner();
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }
        //Lagrer:
        kontroll.skrivData(filnavn);
        //Tømmer Arraylisten i kontroll:
        kontroll.empty();
        //Sjekker at den er tom:
        personer = kontroll.getPersoner();
        System.out.println("");
        System.out.println("Personer i datastrukturen etter tømming:");
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }
        //Leser fra fil:
        kontroll.lesData(filnavn);
        System.out.println("");
        System.out.println("Sjekker at objektene er gjenopprettet:");
        personer = kontroll.getPersoner();
        System.out.println("");
        System.out.println("Personer i datastrukturen etter gjenoppretting:");
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }
    }
}
