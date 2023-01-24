package lambdaDemo;

public class TestLambda {

    public static void main(String[] args) {
        //Lager et kalkulatorobjekt for addisjon:
        Kalkulator addisjon = (a, b) -> a + b;

        //Subtraksjon:
        Kalkulator subtraksjon = (a, b) -> a - b;

        //Multiplikajson:
        Kalkulator multi = (a, b) -> a * b;

        //Divisjon:
        Kalkulator divi = (a, b) -> a / b;

        //Det vi har gjort nå er å definere innholdet i metoden operasjon
        //for fire kalkulatorer

        //Vi kan nå bruke kalkulatorene:
        System.out.println("Addisjon: " + addisjon.operasjon(7,2));
        System.out.println("Subtraksjon: " + subtraksjon.operasjon(7,2));
        System.out.println("Multiplikajson: " + multi.operasjon(7,2));
        System.out.println("Divisjon: " + divi.operasjon(7,2));
    }
}
