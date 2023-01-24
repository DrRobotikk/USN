package Stakk;

public class Kjøretøy implements Comparable<Kjøretøy>{
    private String regnr; // Tjener som identifikator
    private String produsent;
    private String modell;
    private int regår;

    //Oppretter konstruktører:
    public Kjøretøy(String regnr, String produsent, String modell, int regår) {
        this.regnr = regnr;
        this.produsent = produsent;
        this.modell = modell;
        this.regår = regår;
    }

    //Ekstra konstruktør for å lage dummy:
    public Kjøretøy(String regnr) {
        this.regnr = regnr;
    }

    //Oppretter gettere og settere:
    public String getRegnr() {
        return regnr;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public String getProdusent() {
        return produsent;
    }

    public void setProdusent(String produsent) {
        this.produsent = produsent;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public int getRegår() {
        return regår;
    }

    public void setRegår(int regår) {
        this.regår = regår;
    }

    //toString metoden:
    @Override
    public String toString() {
        return "Kjøretøy{" +
                "regnr='" + regnr + '\'' +
                ", produsent='" + produsent + '\'' +
                ", modell='" + modell + '\'' +
                ", regår=" + regår +
                '}';
    }

    //Oppretter compareTo-metoden (Implementering):
    @Override
    public int compareTo(Kjøretøy denandre) {
        return this.regnr.compareTo(denandre.getRegnr());
    }

    //Oppretter equals-metoden som sammenligner kjøretøy sitt regnr med objektet:
    @Override
    public boolean equals(Kjøretøy denandre) {
        return this.regnr.equals(denandre.getRegnr());
    }
}
