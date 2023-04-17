package com.example.obligroman.domeneklasser;

//Definerer klassen Kunde, med to variabler
//Vi legger også til en konstruktør som tar to variabler
public class Kunde {
    private String kundenr;
    private String kundenavn;

    public Kunde(String kundenr, String kundenavn) {
        this.kundenr = kundenr;
        this.kundenavn = kundenavn;
    }
    //Legger til metoder for Klassen Kunde
    public String getKundenr() {
        return kundenr;
    }

    public String getKundenavn() {
        return kundenavn;
    }

    public void setKundenr(String kundenr) {
        this.kundenr = kundenr;
    }

    public void setKundenavn(String kundenavn) {
        this.kundenavn = kundenavn;
    }

    //Definerer en toString metode med informasjon om kunde
    public String toString() {
        return "Kundenr: " + kundenr + " Kunde: " + kundenavn;
    }
}
