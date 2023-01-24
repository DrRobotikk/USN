package no.gmailromankollar77DiktGenerator;

//Egen Class for å opprette og håndtere array(liste):
public class Arrays {

    //bestemmer lengden på lista
    public int lengde = 10;

    //Oppretter selve array
    private String[] tabell = new String[lengde];

    //I starten inneholder lista 0 elementer, altså er den tom
    private int antall = 0;

    //Lager metoden nyttObjekt som legger til nye ord i tabellen samt kaller funksjonen...
    //utvidTabell om ordene i tabellen overstiger 10 ord
    public void nyttObjekt(String nyttOrd) {
        if(antall == tabell.length) utvidTabell();
        tabell[antall] = nyttOrd;
        antall++;
    }


    //Lager metoden som utvider selve lista
    private void utvidTabell() {
        String[] nyTabell = new String[lengde+1];
        lengde = nyTabell.length;
        for(int i = 0; i < tabell.length; i++) {
            nyTabell[i] = tabell[i];
        }
        tabell = nyTabell;
    }

    //Lager metoden for parameteroverføring av selve lista
    public String [] getListe() {

        return tabell;
    }

}
