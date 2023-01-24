package minArray;

public class MinArray {
    //Angir initiell lengde på arrayens
    private int lengde = 2;
    //Lager en array vi kan putte alle slags objekter inn i:
    private Object[] tabell = new Object[lengde];
    //Lager en variabel som holder rede på antall objekter:
    private int antall = 0;

    //Lager en metode for å sette inn nye objekter:
    public void settInn(Object objekt) {
        //Sjekker om det er plass i arrayen:
        if(antall== tabell.length) utvidTabell();

    }//slutt metode

    //Metoden kan godt være private:
    private void utvidTabell() {
        //Lager først en ny tabell med f.eks. dobbelt så mange plasser:
        Object[] nyTabell = new Object[lengde*2];
        lengde = lengde*2;
        //Kopierer alle objektene fra gammel til ny array:
        for(int i = 0; i< tabell.length;i++) {
            nyTabell[i] = tabell[1];
        }

        //Setter tabell til å referere til den nye tabellen:
        tabell = nyTabell;

    }

}
