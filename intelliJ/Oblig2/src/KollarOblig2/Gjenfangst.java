package KollarOblig2;
//SUPERKLASSE GJENFANGST:

public class Gjenfangst implements Comparable<Gjenfangst>{
    //FELLES VARIABLER FOR DYRENE:
    private String ID;
    private Float nyLengde;
    private Float nyVekt;
    private String nyDato;
    private String nyttSted;

    //KONSTRUKTØR:
    public Gjenfangst(String ID, Float nyLengde, Float nyVekt, String nyDato, String nyttSted) {
        this.ID = ID;
        this.nyLengde = nyLengde;
        this.nyVekt = nyVekt;
        this.nyDato = nyDato;
        this.nyttSted = nyttSted;
    }

    //GETTERE OG SETTERE:
    public String getID() {
        return ID;
    }

    public void setID(String ID) { this.ID = ID; }

    //TOSTRING:
    @Override
    public String toString() {
        return "ID: "+ ID +
                ", Lengde: "+ nyLengde +" cm"+
                ", Vekt: "+ nyVekt +" kg"+
                ", Dato: "+ nyDato +
                ", Sted: "+ nyttSted;
    }

    //COMPARETO OG EQUALS:
    public int compareTo(Gjenfangst annenGjenfangst) {
        return this.ID.compareTo(annenGjenfangst.getID());
    }

    public boolean equals(Gjenfangst annenGjenfangst) {
        return this.ID.equals(annenGjenfangst.getID());
    }
}
