package domeneklasser;

public class Kunde {
    private int kundenr;
    private String kundenavn;

    public Kunde(int kundenr, String kundenavn) {
        this.kundenr = kundenr;
        this.kundenavn = kundenavn;
    }

    public int getKundenr() {
        return kundenr;
    }

    public String getKundenavn() {
        return kundenavn;
    }

    public void setKundenr(int kundenr) {
        this.kundenr = kundenr;
    }

    public void setKundenavn(String kundenavn) {
        this.kundenavn = kundenavn;
    }

    public String toString() {
        return "Kundenr: " + kundenr + " Kunde: " + kundenavn;
    }
}
