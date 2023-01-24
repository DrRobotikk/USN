public class testKlient {

    public static void main(String[] args) {

        //Oppretter et objekt av klassen:
        GeneriskStack<String> stakken = new GeneriskStack<>();
        //Setter inn noen bynavn for eksempel:
        stakken.push("Kongsberg");
        stakken.push("Drammen");
        stakken.push("Hønefoss");
        //Tester på hva som ligger øverst i stakken:
        System.out.println("Øverst i stakken: "+ stakken.peep());
        //Skriver ut hele stakken:
        Object[] byListe = stakken.getInnhold();
        for (int i = byListe.length-1; i > -1; i--) {
            System.out.println(byListe[i]);
        }
        //Fjerner øverste objekt (siste):
        System.out.println("Fjerner øverste by: " + stakken.pop());
        //Skriver ut stakken på nytt:
        System.out.println("Stakken ser nå slik ut:");
        byListe = stakken.getInnhold();
        for (int i = byListe.length -1; i > -1; i--) {
            System.out.println(byListe[i]);
        }
    }
}
