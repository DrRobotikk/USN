package TrondAssosiassjoner;

public class TestKlient {
    public static void main(String[] args) {
        Kontroll kontroll = new Kontroll();

        kontroll.nyPostadresse(3518, "Hønefoss");
        kontroll.nyPostadresse(1000, "Drammen");
        kontroll.nyPostadresse(3514, "Hønefoss");


    }
}
