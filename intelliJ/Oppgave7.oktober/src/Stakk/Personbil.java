package Stakk;

public class Personbil extends Kjøretøy{

    private int antallPlasser;

    public Personbil(String regnr, String produsent, String modell, int regår, int antallPlasser) {
        super(regnr, produsent, modell, regår);
        this.antallPlasser = antallPlasser;
    }

    public int getAntallPlasser() {
        return antallPlasser;
    }

    public void setAntallPlasser(int antallPlasser) {
        this.antallPlasser = antallPlasser;
    }

    @Override
    public String toString() {
        return "Personbil{" +
                "antallPlasser=" + antallPlasser +
                "} " + super.toString();
    }
}
