import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.TreeMap;

public class Kontroll {
    //private HashMap<Integer, Vare> vareliste = new HashMap<>();
    private TreeMap<Integer, Vare> vareliste = new TreeMap<>();

    public void nyVare(int varenr, Vare vare) {
        vareliste.put(varenr, vare);
    }

    public Vare finnVare(int varenr) {
        Vare vare = vareliste.get(varenr);
        if (vare!= null) return vare;
        else return null;
        //eller bare return vareliste.get(varenr)
    }

    public void slettVare(int varenr) {
        vareliste.remove(varenr);
    }

    public Iterator<Vare> getVarer() {
        Collection<Vare> innhold = vareliste.values();
        Iterator<Vare> oppramser = innhold.iterator();
        return oppramser;
    }

    public void endreBeholdning(int varenr, int tillegg) {
        Vare vare = finnVare(varenr);
        if (vare != null) vare.endreBeholdning(tillegg);
    }
}
