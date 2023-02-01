package LagreDemo;

import java.util.Objects;

public class Person {
    private String navn;
    private String adresse;
    private int fodselsar;

    public Person(String navn, String adresse, int fodselsar) {
        this.navn = navn;
        this.adresse = adresse;
        this.fodselsar = fodselsar;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public int getFodselsar() {
        return fodselsar;
    }

    public void setFodselsar(int fodselsar) {
        this.fodselsar = fodselsar;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return fodselsar == person.fodselsar && Objects.equals(navn, person.navn) && Objects.equals(adresse, person.adresse);
    }

    @Override
    public int hashCode() {
        return Objects.hash(navn, adresse, fodselsar);
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", fodselsar=" + fodselsar +
                '}';
    }

    public String toFile() {
        return navn + ";"+adresse+";"+fodselsar;
    }
}
