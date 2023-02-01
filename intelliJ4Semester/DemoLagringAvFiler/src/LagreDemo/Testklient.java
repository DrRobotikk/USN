package LagreDemo;

public class Testklient {
    public static void main(String[] args) {
        String filnavn = "personer.csv";
        Kontroll kontroll = new Kontroll();
        //Legger til personer:
        kontroll.nyPerson(new Person("Ole", "Gate 1", 2001));
        kontroll.nyPerson(new Person("Lise", "Gate 2", 2011));
        kontroll.skrivData(filnavn);
    }
}
