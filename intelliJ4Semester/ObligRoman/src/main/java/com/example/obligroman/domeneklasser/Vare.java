package com.example.obligroman.domeneklasser;
//Definerer klassen Vare, med tre variabler
//Vi legger også til en konstruktør som tar tre variabler
public class Vare {

    private String varenr;
    private String varenavn;
    private double pris;

    public Vare(String varenr, String varenavn, double pris) {
        this.varenr = varenr;
        this.varenavn = varenavn;
        this.pris = pris;
    }

    //Definerer metoder for Vare klassen
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

    public double getPris() {
        return pris;
    }

    public void setPris(double pris) {
        this.pris = pris;
    }

    //Definerer en toString metode med informasjon om vare
    public String toString() {
        return "Varenr: " + varenr + " Varenavn: " + varenavn + " Pris: " + pris;
    }
    //Definerer en toFile metode med informasjon om vare
    public String toFile() { return varenr + ";" + varenavn + ";" + pris; }
}
