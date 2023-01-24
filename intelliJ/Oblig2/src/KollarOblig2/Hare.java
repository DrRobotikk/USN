package KollarOblig2;
//SUBKLASSE (DYR) HARE:

public class Hare extends Dyr{
    //EGNE VARIABLER FOR HARE
    private String hareType;
    private String harePels;

    //KONSTRUKTØR:
    public Hare(String ID, String kjonn, Float lende, Float vekt, String dato, String sted, String hareType, String harePels) {
        super(ID, kjonn, lende, vekt, dato, sted);
        this.hareType = hareType;
        this.harePels = harePels;
    }

    //GETTER OG SETTERE:
    public String getHareType() {
        return hareType;
    }
    public void setHareType(String hareType) {
        this.hareType = hareType;
    }
    public String getHarePels() {
        return harePels;
    }
    public void setHarePels(String harePels) {
        this.harePels = harePels;
    }

    //toString
    @Override
    public String toString() {
        return super.toString() + ", Type: "+ hareType + ", Pels: "+ harePels;
    }
}
