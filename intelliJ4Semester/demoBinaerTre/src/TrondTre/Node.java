package TrondTre;

public class Node {
    private int verdi;
    private Node venstre;
    private Node hoyre;
    private Node forelder;

    //to konstruktører:
    public Node(int verdi) {
        this.verdi = verdi;
    }

    public Node(int verdi, Node forelder) {
        this.verdi = verdi;
        this.forelder = forelder;
    }

    //Rekursiv metode for å sette inn nye noder (med verdi):
    public void settInn(int nyVerdi) {
        //Hvis verdien i noden er større enn nyVerdi: går vi til venstre!
        if (verdi >= nyVerdi) {//vi skal til venstre
            //Sjekker først om det er node til venstre:
            if (venstre != null) {//det er en node til venstre, og vi gjør rekursivt kall på settInn
                venstre.settInn(nyVerdi);
            } else {//det er ikke en node til venstre:
                venstre = new Node(nyVerdi, this);
            }
        } else {//nyVerdi skal til høyre
            if (hoyre != null) {
                hoyre.settInn(nyVerdi);
            } else {
                hoyre = new Node(nyVerdi);
            }
        }
    }
    public boolean finnVerdi(int finnVerdi) {
        if (finnVerdi == verdi) return true;
        if (verdi >= finnVerdi) {//søker til venstre
            if (venstre != null) {
                return venstre.finnVerdi(finnVerdi);
            } else return false;
        }
        //vi skal til høyre
        else {
            if (hoyre != null) {
                return hoyre.finnVerdi(finnVerdi);
            }
            else return false; //ikke funnet
        }
    }

    //rekursiv toString():
    public String toString() {
        //Lager en tom streng
        String returstreng = "";
        if (venstre != null) {
            returstreng = returstreng + venstre.toString();
        }
        //legger til verdien i den aktuelle noden:
        returstreng = returstreng + verdi;
        if (hoyre != null) {
            returstreng = returstreng + hoyre.toString();
        }
        return returstreng;
    }
}
