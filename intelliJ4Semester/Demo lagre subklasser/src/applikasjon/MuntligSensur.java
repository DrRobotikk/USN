package applikasjon;

public class MuntligSensur extends Sensur{

    double lengde;

    public MuntligSensur(String fag, String eksamenstype, double lengde) {
        super(fag, eksamenstype);
        this.lengde = lengde;
    }

    @Override
    public double finnTimeforbruk() {
        return lengde + FORBEREDELSE;
    }

    @Override
    public String toString() {
        return "MuntligSensur{" +
                "lengde=" + lengde +
                '}';
    }

    public String toFile() {
        return "M;" + super.toFile() + ";" + lengde;
    }
}
