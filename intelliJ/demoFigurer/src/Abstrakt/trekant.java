package Abstrakt;

public class trekant extends Figur {

    //Vi trenger to attributter:
    private double høyde;
    private double lengde;

    //Konstruktør:
    public trekant(double høyde, double lengde) {
        super();
        this.høyde = høyde;
        this.lengde = lengde;
    }

    public double beregnAreal() {

        return lengde*høyde/2;
    }
}
