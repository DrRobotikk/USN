import java.util.Iterator;

public class testKlient {
    public static void main(String[] args) {
        Kontroll kontroll = new Kontroll();

        Vare vare = new Vare(1, "Eske", 10);
        kontroll.nyVare(1, vare);
        vare = new Vare(2, "Boks", 5);
        kontroll.nyVare(2, vare);
        Iterator<Vare> varene = kontroll.getVarer();
        String uttekst = "";

        while (varene.hasNext()) {
            Vare varen = varene.next();
            uttekst+= varen.toString() + "\n";
        }
        System.out.println(uttekst);

        //Tester finnVare-metoden:
        vare = kontroll.finnVare(2);
        System.out.println(vare.toString());
        System.out.println("");

        //Tester endreBeholdning-metoden:
        kontroll.endreBeholdning(1, 5); //Skal man minske beholdningen, skriver man
        varene = kontroll.getVarer();               //"-" foran tillegstallet
        uttekst = "";

        while (varene.hasNext()) {
            Vare varen = varene.next();
            uttekst+= varen.toString() + "\n";
        }
        System.out.println(uttekst);
    }
}
