package romanDyr;

import java.util.ArrayList;

public class Gaupe implements Comparable<Gaupe>{
    private String id;
    private String kjonn;
    private Float lengde;
    private Float vekt;
    private Float tuss;
    private String dato;
    private String sted;
    private ArrayList<Gjenfangst> gjenfangst = new ArrayList<>();

    public Gaupe(String id, String kjonn, Float lengde, Float vekt, Float tuss, String dato, String sted) {
        this.id = id;
        this.kjonn = kjonn;
        this.lengde = lengde;
        this.vekt = vekt;
        this.tuss = tuss;
        this.dato = dato;
        this.sted = sted;
        this.gjenfangst = gjenfangst;
    }

    public Gaupe(String id) {
        this.id=id;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getKjonn() {
        return kjonn;
    }

    public void setKjonn(String kjonn) {
        this.kjonn = kjonn;
    }

    public Float getLengde() {
        return lengde;
    }

    public void setLengde(Float lengde) {
        this.lengde = lengde;
    }

    public Float getVekt() {
        return vekt;
    }

    public void setVekt(Float vekt) {
        this.vekt = vekt;
    }

    public Float getTuss() {
        return tuss;
    }

    public void setTuss(Float tuss) {
        this.tuss = tuss;
    }

    public String getDato() {
        return dato;
    }

    public void setDato(String dato) {
        this.dato = dato;
    }

    public String getSted() {
        return sted;
    }

    public void setSted(String sted) {
        this.sted = sted;
    }

    public ArrayList<Gjenfangst> getGjenfangst() {
        return gjenfangst;
    }

    public void setGjenfangst(ArrayList<Gjenfangst> gjenfangst) {
        this.gjenfangst = gjenfangst;
    }

    @Override
    public String toString() {
        return "Første registrering:" +"\n"+
                id +
                ", kjønn: " + kjonn+
                ", lengde: " + lengde +
                ", vekt: " + vekt +
                ", tusselengde: " + tuss +
                ", dato: " + dato +
                ", sted: " + sted + "\n"+
                "Gjenfangstdata:" + "\n" + gjenfangst;
    }

    public int compareTo(Gaupe denAndre) {
        return this.id.compareTo(denAndre.getId());
    }


    public boolean equals(Gaupe denAndre) {
        return this.id.equals(denAndre.getId());
    }
}
