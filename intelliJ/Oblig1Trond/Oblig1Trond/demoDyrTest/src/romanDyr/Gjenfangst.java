package romanDyr;

public class Gjenfangst implements Comparable<Gjenfangst>{
    private String id;
    private Float lengde;
    private Float vekt;
    private Float tuss;
    private String dato;
    private String sted;

    public Gjenfangst(String id, Float lengde, Float vekt, Float tuss, String dato, String sted) {
        this.id = id;
        this.lengde = lengde;
        this.vekt = vekt;
        this.tuss = tuss;
        this.dato = dato;
        this.sted = sted;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    @Override
    public String toString() {
        return  "ID: " + id +
                ", lengde:" + lengde +
                ", vekt:" + vekt +
                ", tuss:" + tuss +
                ", dato:" + dato +
                ", sted:" + sted ;
    }

    public int compareTo(Gjenfangst annen) {
        return this.id.compareTo(annen.getId());
    }

    public boolean equals(Gjenfangst annen) {
        return this.id.equals(annen.getId());
    }
}
