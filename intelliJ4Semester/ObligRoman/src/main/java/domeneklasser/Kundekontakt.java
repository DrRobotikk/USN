package domeneklasser;

import java.util.Date;

public class Kundekontakt {

    private int kundenr;
    private Date dato;
    private String beskrivelse;

    public Kundekontakt(int kundenr, Date dato, String beskrivelse) {
        this.kundenr = kundenr;
        this.dato = dato;
        this.beskrivelse = beskrivelse;
    }

    public int getKundenr() {
        return kundenr;
    }

    public Date getDato() {
        return dato;
    }

    public String getBeskrivelse() {
        return beskrivelse;
    }

    public void setKundenr(int kundenr) {
        this.kundenr = kundenr;
    }

    public void setDato(Date dato) {
        this.dato = dato;
    }

    public void setBeskrivelse(String beskrivelse) {
        this.beskrivelse = beskrivelse;
    }

    public String toString() {
        return "Kundenr: " + kundenr + " Dato: " + dato + " Beskrivelse: " + beskrivelse;
    }
}
