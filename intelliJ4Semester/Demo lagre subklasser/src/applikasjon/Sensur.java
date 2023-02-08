package applikasjon;

public abstract class Sensur {
    public final int FORBEREDELSE = 3;
    private String fag;
    private String eksamenstype;

    public Sensur(String fag, String eksamenstype) {
        super();
        this.fag = fag;
        this.eksamenstype = eksamenstype;
    }

    public int getFORBEREDELSE() {
        return FORBEREDELSE;
    }

    public String getFag() {
        return fag;
    }

    public void setFag(String fag) {
        this.fag = fag;
    }

    public String getEksamenstype() {
        return eksamenstype;
    }

    public void setEksamenstype(String eksamenstype) {
        this.eksamenstype = eksamenstype;
    }

    //Definerer en abstrakt metode:
    public abstract double finnTimeforbruk();

    @Override
    public String toString() {
        return "Sensur{" +
                "FORBEREDELSE=" + FORBEREDELSE +
                ", fag='" + fag + '\'' +
                ", eksamenstype='" + eksamenstype + '\'' +
                '}';
    }

    public String toFile() {
        return  fag + ";" + eksamenstype;
    }
}
