package applikasjon;

public class ProsjektSensur extends Sensur {
    private int antallBesvarelser;
    private final double PROSJEKTSENSUR = 8;

    //Implementerer metoden finnTimeforbruk
    @Override
    public double finnTimeforbruk() {
        return antallBesvarelser*PROSJEKTSENSUR;
    }

    public ProsjektSensur(String fag, String eksamenstype, int antallBesvarelser) {
        super(fag, eksamenstype);
        this.antallBesvarelser = antallBesvarelser;
    }

    @Override
    public String toString() {
        return "ProsjektSensur{" +
                "antallBesvarelser=" + antallBesvarelser +
                ", PROSJEKTSENSUR=" + PROSJEKTSENSUR +
                '}';
    }

    //toFile skal legge til et attributt som identifiserer klassen:
    public String toFile() {
        return "P;" + super.toFile() + ";" + antallBesvarelser;
    }
}
