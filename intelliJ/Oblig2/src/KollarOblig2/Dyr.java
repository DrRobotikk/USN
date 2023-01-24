package KollarOblig2;
//SUPERKLASSEN DYR

public class Dyr implements Comparable<Dyr>{
    //OPPRETTER VARIABLER FOR DET DYRENE HAR FELLES:
    private String ID;
    private String kjonn;
    private Float lengde;
    private Float vekt;
    private String dato;
    private String sted;

    //OPPRETTER KONSTRUKTØRENE:
    public Dyr(String ID, String kjonn, Float lengde, Float vekt, String dato, String sted) {
        this.ID = ID;
        this.kjonn = kjonn;
        this.lengde = lengde;
        this.vekt = vekt;
        this.dato = dato;
        this.sted = sted;
    }

    //GETTER OG SETTER FOR ID
    public String getID() {
        return ID;
    }
    public void setID(String ID) {
        this.ID = ID;
    }

    //GETTER OG SETTER FOR FLOAT (EKSEMPEL)
    public Float getLengde() {
        return lengde;
    }
    public void setLengde(Float lengde) {
        this.lengde = lengde;
    }

    //OPPRETTER TOSTRING-METODE:
    @Override
    public String toString() {
        return  "ID: "+ ID +
                ", Kjønn: "+ kjonn +
                ", Lengde: "+ lengde +" cm"+
                ", Vekt: "+ vekt +" kg"+
                ", Dato: "+ dato +
                ", Sted: " + sted;
    }

    //OPPRETTER COMPARETO-METODEN:
    public int compareTo(Dyr annetDyr) {
        return this.ID.compareTo(annetDyr.getID());
    }
    //OPPRETTER EQUALS-METODEN:
    public boolean equals(Dyr annetDyr) {
        return this.ID.equals(annetDyr.getID());
    }
}
