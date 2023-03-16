public class Ansatt {
    private String navn;
    private Ansettelsesforhold status;

    public Ansatt(String navn, Ansettelsesforhold status) {
        this.navn = navn;
        this.status = status;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public Ansettelsesforhold getStatus() {
        return status;
    }

    public void setStatus(Ansettelsesforhold status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Ansatt{" +
                "navn='" + navn + '\'' +
                ", status=" + status +
                '}';
    }
}
