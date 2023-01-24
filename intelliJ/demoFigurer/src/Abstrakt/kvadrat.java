package Abstrakt;

public class kvadrat extends Figur{
    //I et kvadrat er alle sidene like lange
    //Derfor trenger vi bare å vite en av dem:
    private double side;

    //konstruktør:
    public kvadrat(double side) {
        super();
        this.side = side;
    }

    public double beregnAreal() {
        return side*side;
    }
}
