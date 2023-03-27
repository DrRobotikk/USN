package domeneklasser;

public class Firmakunde extends Kunde{

    private double kredittgrense;
    private String telefonnummer;

    public Firmakunde(int kundenr, String kundenavn, double kredittgrense, String telefonnummer) {
        super(kundenr, kundenavn);
        this.kredittgrense = kredittgrense;
        this.telefonnummer = telefonnummer;
    }

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

    public String toString() {
        return super.toString() + " Kredittgrense: " + kredittgrense + " Telefonnummer: " + telefonnummer;
    }
}
