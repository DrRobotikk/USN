package com.example.obligroman.domeneklasser;

public class Privatkunde extends Kunde{

    private String butikk;

    public Privatkunde(String kundenr, String kundenavn, String butikk) {
        super(kundenr, kundenavn);
        this.butikk = butikk;
    }

    public String getButikk() {
        return butikk;
    }

    public void setButikk(String butikk) {
        this.butikk = butikk;
    }

    public String toString() {
        return super.toString() + " Butikk: " + butikk;
    }
    public String toFile() {return "P" +";" + super.getKundenr() + ";" + super.getKundenavn() + ";" + butikk;}



}
