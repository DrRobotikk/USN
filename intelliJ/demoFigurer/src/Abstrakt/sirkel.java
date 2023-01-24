package Abstrakt;

public class sirkel extends Figur{

    //Vi må vite radien.
    //enheten PI henter vi fra klassen Math
    private double radius;

    //konstruktør:
    public sirkel(double radius) {
        super();
        this.radius = radius;
    }

    public double beregnAreal() {
        return Math.PI*radius*radius;
    }
}
