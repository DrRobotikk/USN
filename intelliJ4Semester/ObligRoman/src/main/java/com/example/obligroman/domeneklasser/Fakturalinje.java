package com.example.obligroman.domeneklasser;

//Definerer klassen Fakturalinje og legger til 5 variabler
public class Fakturalinje {

    private String fakturanr;
    private String varenr;
    private String varenavn;
    private int antall;
    private double rabatt;
    private double totalPris;

    //Bruker parametrene for å initialisere variabler med samme navn
    public Fakturalinje(String fakturanr, String varenr, String varenavn, int antall, double rabatt, double totalPris) {
        this.fakturanr = fakturanr;
        this.varenr = varenr;
        this.varenavn = varenavn;
        this.antall = antall;
        this.rabatt = rabatt;
        this.totalPris = totalPris;
    }
    //Definerer metoder for Fakturalinje klassen
    public String getFakturanr() {return fakturanr;}

    public void setFakturanr(String fakturanr) {this.fakturanr = fakturanr;}

    public String getVarenr() {
        return varenr;
    }

    public void setVarenr(String varenr) {
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
    //Definerer en toString metode med informasjon om fakturalinje
    public String toString() {
        return "Fakturalinje{" +
                "fakturanr=" + fakturanr +
                ", varenr=" + varenr +
                ", varenavn='" + varenavn + '\'' +
                ", antall=" + antall +
                ", rabatt=" + rabatt +
                ", totalPris=" + totalPris +
                '}';
    }

    public String toFile() {
        return fakturanr + ";" + varenr + ";" + varenavn + ";" + antall + ";" + rabatt + ";" + totalPris;
    }
}
