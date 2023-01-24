package lenketListe;

//Klassen Node er generisk derfor skriver vi Type i krokodillekjeftene:
public class Node<Type> {
    //objektet som skal settes inn:
    private Type objekt;
    //Referanse til neste Node:
    private Node<Type> neste;

    //Konstruktør:

    public Node(Type objekt) {
        this.objekt = objekt;
        //I intelliJ er neste=null som default, men kan hende at andre språk ikke har det.
        //med andre ord er det ikke nødvendig her å skrive neste = null;
        neste = null;
    }
    //Metode som returnerer innholdet i Noden:
    public Type getInnhold() {
        return objekt;
    }

    //Henter referanse til neste node:
    public Node<Type> getNeste() {
        return neste;
    }

    //Metode for å sette neste node:
    public void setNeste(Node neste) {
        this.neste = neste;
    }
}
