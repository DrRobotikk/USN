package KollarOblig2;
//SUBKLASSE (DYR) GAUPE

public class Gaupe extends Dyr{
    //EGNE VARIABLER FOR DYRET GAUPE:
    private Float tusseLengde;

    //KONSTRUKTØR:
    public Gaupe(String ID, String kjonn, Float lende, Float vekt, String dato, String sted, Float tusseLengde) {
        super(ID, kjonn, lende, vekt, dato, sted);
        this.tusseLengde = tusseLengde;
    }

    //GETTERE OG SETTERE
    public Float getTusseLengde() {
        return tusseLengde;
    }
    public void setTusseLengde(Float tusseLengde) {
        this.tusseLengde = tusseLengde;
    }

    //TOSTRING
    @Override
    public String toString() {
        return super.toString() +", Tusselengde: "+ tusseLengde +" cm";
    }
}
