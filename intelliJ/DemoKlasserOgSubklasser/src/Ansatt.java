public class Ansatt extends Person {
    private int lonnstrinn;

    public Ansatt(String navn, String adresse, int fodselsaar, int lonnstrinn) {
        super(navn, adresse, fodselsaar);
        this.lonnstrinn = lonnstrinn;
    }

    public int getLonnstrinn() {
        return lonnstrinn;
    }

    public void setLonnstrinn(int lonnstrinn) {
        this.lonnstrinn = lonnstrinn;
    }

    @Override
    public String toString() {
        return "Ansatt{" +
                "lonnstrinn=" + lonnstrinn +
                "} " + super.toString();
    }
}
