package domeneklasser;

public class Faktura {

    private int fakturanr;
    private Kunde fakturaKunde;
    private long dato;
    private long forfallsdato;

    public Faktura(int fakturanr, Kunde fakturaKunde, long dato, long forfallsdato) {
        this.fakturanr = fakturanr;
        this.fakturaKunde = fakturaKunde;
        this.dato = dato;
        this.forfallsdato = forfallsdato;
    }

    public int getFakturanr() {
        return fakturanr;
    }

    public void setFakturanr(int fakturanr) {
        this.fakturanr = fakturanr;
    }

    public Kunde getFakturaKunde() {
        return fakturaKunde;
    }

    public void setFakturaKunde(Kunde fakturaKunde) {
        this.fakturaKunde = fakturaKunde;
    }

    public long getDato() {
        return dato;
    }

    public void setDato(long dato) {
        this.dato = dato;
    }

    public long getForfallsdato() {
        return forfallsdato;
    }

    public void setForfallsdato(long forfallsdato) {
        this.forfallsdato = forfallsdato;
    }

    @Override
    public String toString() {
        return "Faktura{" +
                "fakturanr=" + fakturanr +
                ", fakturaKunde=" + fakturaKunde +
                ", dato=" + dato +
                ", forfallsdato=" + forfallsdato +
                '}';
    }
}
