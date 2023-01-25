package TrondTre;

public class TestKlient {
    public static void main(String[] args) {
        Binaertre tre = new Binaertre();
        //Setter inn verdier i treet:
        tre.settInn(5);
        tre.settInn(3);
        tre.settInn(1);
        tre.settInn(4);
        tre.settInn(7);

        //Skriver ut med toString:
        System.out.println("Skriver ut innholdet i treet:");
        System.out.println(tre.toString());
        //Sjekker søkemetoden:
        System.out.println("Finnes 2 i treet? " + tre.finnVerdi(2));
        System.out.println("Finner 5 i treet? " + tre.finnVerdi(5));
    }
}
