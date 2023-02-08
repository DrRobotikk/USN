package applikasjon;

import java.util.Objects;

public class Vare {
    private int varenr;
    private String varenavn;
    private int beholdning = 0; //Ikke nødvendig å sette til 0

    //Konstruktør:
    public Vare(int varenr, String varenavn, int beholdning) {
        this.varenr = varenr;
        this.varenavn = varenavn;
        this.beholdning = beholdning;
    }

    //Gettere og settere:
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

    public int getBeholdning() {
        return beholdning;
    }

    public void setBeholdning(int beholdning) {
        this.beholdning = beholdning;
    }

    @Override
    public String toString() {
        return "Vare{" +
                "varenr=" + varenr +
                ", varenavn='" + varenavn + '\'' +
                ", beholdning=" + beholdning +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vare vare = (Vare) o;
        return varenr == vare.varenr && beholdning == vare.beholdning && Objects.equals(varenavn, vare.varenavn);
    }

    @Override
    public int hashCode() {
        return Objects.hash(varenr, varenavn, beholdning);
    }

    public String toFile() {
        return varenr + ";" + varenavn + ";" + beholdning;
    }
}
