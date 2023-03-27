package domeneklasser;

public class Fakturalinje {

    private int varenr;
    private String varenavn;
    private int antall;
    private double rabatt;
    private double totalPris;

    public Fakturalinje(int varenr, String varenavn, int antall, double rabatt, double totalPris) {
        this.varenr = varenr;
        this.varenavn = varenavn;
        this.antall = antall;
        this.rabatt = rabatt;
        this.totalPris = totalPris;
    }

    public int getVarenr() {
        return varenr;
    }

    public void setVarenr(int varenr) {
        this.varenr = varenr;
    }

    public String getVarenavn() {
        return varenavn;
    }

    public void setVarenavn(String varenavn) {
        this.varenavn = varenavn;
    }

    public int getAntall() {
        return antall;
    }

    public void setAntall(int antall) {
        this.antall = antall;
    }

    public double getRabatt() {
        return rabatt;
    }

    public void setRabatt(double rabatt) {
        this.rabatt = rabatt;
    }

    public double getTotalPris() {
        return totalPris;
    }

    public void setTotalPris(double totalPris) {
        this.totalPris = totalPris;
    }

    @Override
    public String toString() {
        return "Fakturalinje{" +
                "varenr=" + varenr +
                ", varenavn='" + varenavn + '\'' +
                ", antall=" + antall +
                ", rabatt=" + rabatt +
                ", totalPris=" + totalPris +
                '}';
    }

    public String toFile() {
        return varenr + ";" + varenavn + ";" + antall + ";" + rabatt + ";" + totalPris;
    }
}
