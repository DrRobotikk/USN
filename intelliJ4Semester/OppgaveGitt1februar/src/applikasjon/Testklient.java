package applikasjon;

import java.util.Iterator;

public class Testklient {
    public static void main(String[] args) {
        String filnavn = "varer.csv";
        Kontroll kontroll = new Kontroll();
        Vare vare = new Vare(1, "Eske", 5);
        kontroll.nyVare(1, vare);
        vare = new Vare(2, "Boks", 7);
        kontroll.nyVare(2, vare);
        //Sjekker at det gikk bra:
        Iterator<Vare> varer = kontroll.getIterator();
        while (varer.hasNext()) {
            vare = varer.next();
            System.out.println(vare.toString());
        }
        //Lagrer:
        kontroll.lagreVarer(filnavn);
        //Tømmer vareliste:
        kontroll.empty();
        //Sjekker at den er blitt tømt:
        System.out.println("Nå skal vareliste være tom");
        System.out.println();
        varer = kontroll.getIterator();
        while (varer.hasNext()) {
            vare = varer.next();
            System.out.println(vare.toString());
        }
        //Leser inn:
        kontroll.lesVarer(filnavn);
        System.out.println("Nå skal den være fylt igjen");
        varer = kontroll.getIterator();
        while (varer.hasNext()) {
            vare = varer.next();
            System.out.println(vare.toString());
        }
    }
}
