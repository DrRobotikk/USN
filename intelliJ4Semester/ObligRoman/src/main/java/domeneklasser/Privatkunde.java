package domeneklasser;

public class Privatkunde extends Kunde{

    private String butikk;

    public Privatkunde(int kundenr, String kundenavn, String butikk) {
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
}
