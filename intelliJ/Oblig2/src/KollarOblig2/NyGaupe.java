package KollarOblig2;

public class NyGaupe extends Gjenfangst{
    //EGNE VARIABLER FOR GAUPE:
    private Float nyTusselengde;

    //KONSTRUKTØR:
    public NyGaupe(String ID, Float nyLengde, Float nyVekt, String nyDato, String nyttSted, Float nyTusselengde) {
        super(ID, nyLengde, nyVekt, nyDato, nyttSted);
        this.nyTusselengde = nyTusselengde;
    }

    //GETTER OG SETTER:
    public Float getNyTusselengde() {
        return nyTusselengde;
    }

    public void setNyTusselengde(Float nyTusselengde) {
        this.nyTusselengde = nyTusselengde;
    }

    //TOSTRING:
    @Override
    public String toString() {
        return super.toString() +", Tusselengde: "+ nyTusselengde +" cm"+ "\n";
    }

}
