package TrondTre;

public class Binaertre {
    private Node rot; //roten i treet

    public void settInn(int verdi) {
        //sjekker om det er noe i treet:
        if (rot != null) {
            rot.settInn(verdi);
        }
        else {//Treet er tomt, og vi lager den første noden (som blir roten):
            rot = new Node(verdi);
        }
    }

    public boolean finnVerdi(int verdi) {
        //Sjekker om treet er tomt:
        if (rot == null) return false;
        else return rot.finnVerdi(verdi);
    }

    public String toString() {
        //sjekker om det er noe i treet:
        if (rot != null) {
            return rot.toString();
        }
        else return null;
    }
}
