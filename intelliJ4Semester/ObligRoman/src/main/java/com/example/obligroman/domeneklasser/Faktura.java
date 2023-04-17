package com.example.obligroman.domeneklasser;

import java.util.ArrayList;

//Definerer klassen Faktura, og legger til 4 variabler
public class Faktura {

    private String fakturanr;
    //referanse til kunde:
    private String kundenr;
    private String dato;
    private String forfallsdato;
   // private ArrayList<Fakturalinje> fakturalinjer;     // Erik test



    public Faktura(String fakturanr, String kundenr, String dato, String forfallsdato) {
        this.fakturanr = fakturanr;
        this.kundenr = kundenr;
        this.dato = dato;
        this.forfallsdato = forfallsdato;
      //   fakturalinjer = new ArrayList<Fakturalinje>();        // Erik test

    }

    public String getFakturanr() {
        return fakturanr;
    }

    public void setFakturanr(String fakturanr) {
        this.fakturanr = fakturanr;
    }

    public String getKundenr() {
        return kundenr;
    }

    public void setkundenr(String kundenr) {
        this.kundenr = kundenr;
    }

    public String getDato() {
        return dato;
    }

    public void setDato(String dato) {
        this.dato = dato;
    }

    public String getForfallsdato() {
        return forfallsdato;
    }

    public void setForfallsdato(String forfallsdato) {
        this.forfallsdato = forfallsdato;
    }



  @Override
    //Oppretter en toString som returnerer informasjon om faktura
    public String toString() {
        return "Faktura{" +
                "fakturanr=" + fakturanr +
                ", fakturaKunde=" + kundenr +
                ", dato=" + dato +
                ", forfallsdato=" + forfallsdato +
                '}';
    }
    //Oppretter en toFile som returnerer informasjon om faktura
    public String toFile() {
        return fakturanr + ";" + kundenr + ";" + dato + ";" + forfallsdato;
    }
}
