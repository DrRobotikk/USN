public class Kvadrat implements Figur{

    private double side;

    //Konstruktør:
    public Kvadrat(double side) {
        super();
        this.side = side;
    }

    public double beregnAreal() {
        return side*side;
    }
}
