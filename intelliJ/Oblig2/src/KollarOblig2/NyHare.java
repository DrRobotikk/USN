package KollarOblig2;

public class NyHare extends Gjenfangst{
    //EGNE VARIABLER FOR HARE:
    private String nyPels;

    //KONSTRUKTØR:
    public NyHare(String ID, Float nyLengde, Float nyVekt, String nyDato, String nyttSted, String nyPels) {
        super(ID, nyLengde, nyVekt, nyDato, nyttSted);
        this.nyPels = nyPels;
    }

    //GETTER OG SETTER:
    public String getNyPels() {
        return nyPels;
    }

    public void setNyPels(String nyPels) {
        this.nyPels = nyPels;
    }

    //TOSTRING:
    @Override
    public String toString() {
        return super.toString() +", Pels: "+ nyPels +"\n";
    }
}
