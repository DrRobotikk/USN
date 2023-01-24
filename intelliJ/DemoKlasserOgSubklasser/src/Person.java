public class Person {
    private String navn;
    private String adresse;
    private int fodselsaar;

    //Konstruktører:
    public Person(String navn, String adresse, int fodselsaar) {
        this.navn = navn;
        this.adresse = adresse;
        this.fodselsaar = fodselsaar;
    }
    //Gettere:
    public String getNavn() {
        return navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public int getFodselsaar() {
        return fodselsaar;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public void setFodselsaar(int fodselsaar) {
        this.fodselsaar = fodselsaar;
    }

    @Override     //Vår egen versjon av toString(), som er definert i Object:
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", fodselsaar=" + fodselsaar +
                '}';
    }
}
