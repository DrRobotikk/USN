package com.example.demoenkeltabell;

public class Person {
    private String navn;
    private String adresse;
    private String telefon;

    public Person(String navn, String adresse, String telefon) {
        this.navn = navn;
        this.adresse = adresse;
        this.telefon = telefon;
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

    public String getTelefon() {
        return telefon;
    }

    public void setTelefon(String telefon) {
        this.telefon = telefon;
    }

}
