package com.example.obligroman.domeneklasser;
//Definerer klassen Firmakunde som extender med klassen Kunde
public class Firmakunde extends Kunde{

    private double kredittgrense;
    private String telefonnummer;

    public Firmakunde(String kundenr, String kundenavn, double kredittgrense, String telefonnummer) {
        super(kundenr, kundenavn);
        this.kredittgrense = kredittgrense;
        this.telefonnummer = telefonnummer;
    }
    //Definerer metoder for Firmakunde klassen
    public double getKredittgrense() {
        return kredittgrense;
    }

    public String getTelefonnummer() {
        return telefonnummer;
    }

    public void setKredittgrense(double kredittgrense) {
        this.kredittgrense = kredittgrense;
    }

    public void setTelefonnummer(String telefonnummer) {
        this.telefonnummer = telefonnummer;
    }

    //Definerer en toString metode med informasjon om FirmaKunde
    public String toString() {
        return super.toString() + " Kredittgrense: " + kredittgrense + " Telefonnummer: " + telefonnummer;
    }
    //Definerer en toFile metode med informasjon om FirmaKunde
    public String toFile() { return "F" + ";" + super.getKundenr() + ";" + super.getKundenavn() + ";" + kredittgrense + ";" + telefonnummer; }
}
