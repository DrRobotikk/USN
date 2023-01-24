package lenketListe;

public class LenketListe<Type> {
    //Starter med å deklarere starten på en liste som består va Noder:
    private Node<Type> hode;

    //Metode for å sette inn en ny node:
    public void settInn(Type objekt) {
        //Vi må alltid sjekke om det er noe i listen:
        if(hode == null) hode = new Node<Type>(objekt);
        //Ellers settes noden inn først:
        else {
            //Oppretter en ny node:
            Node<Type> nyNode = new Node<Type>(objekt);
            //Setter inn ny node først:
            nyNode.setNeste(hode);
            //Setter hode til å peke på ny node:
            hode = nyNode;
        }
        {
            //Definerer Node for å "huske" hodet:
            Node<Type> husk = hode;
            //Lager en ny Node:
            hode = new Node<Type>(objekt);
            hode.setNeste(husk);
        }
    }

    //Metoden for å slette første Node:
    public void slettFørste() {
        if(hode !=null) hode = hode.getNeste();
    }

}
