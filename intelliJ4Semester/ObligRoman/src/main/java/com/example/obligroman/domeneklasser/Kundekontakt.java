package com.example.obligroman.domeneklasser;

//Definerer klassen Kundekontakt, med tre variabler
//Vi legger også til en konstruktør som tar tre variabler
public class Kundekontakt {

    private String kundenr;
    private String dato;
    private String beskrivelse;

    public Kundekontakt(String kundenr, String dato, String beskrivelse) {
        this.kundenr = kundenr;
        this.dato = dato;
        this.beskrivelse = beskrivelse;
    }

    //Definerer metoder for Kundekontakt klassen
    public String getKundenr() {
        return kundenr;
    }

    public String getDato() {
        return dato;
    }

    public String getBeskrivelse() {
        return beskrivelse;
    }

    public void setKundenr(String kundenr) {
        this.kundenr = kundenr;
    }

    public void setDato(String dato) {
        this.dato = dato;
    }

    public void setBeskrivelse(String beskrivelse) {
        this.beskrivelse = beskrivelse;
    }

    //Definerer en toString metode med informasjon om kunde
    public String toString() {
        return "Kundenr: " + kundenr + " Dato: " + dato + " Beskrivelse: " + beskrivelse;
    }
    //Definerer en toFile metode med informasjon om kunde
    public String toFile() { return kundenr + ";" + dato + ";" + beskrivelse; }
}
