package TrondMetoder;

//Klassen Poststed skal implementere interfaceet Comparable:
public class Poststed implements Comparable<Poststed>{
    private int postnr;
    private String stedsnavn;
    public Poststed(int postnr, String stedsnavn) {
        super();
        this.postnr = postnr;
        this.stedsnavn = stedsnavn;
    }
    public int getPostnr() {
        return postnr;
    }

    public void setPostnr(int postnr) {
        this.postnr = postnr;
    }

    public String getStedsnavn() {
        return stedsnavn;
    }

    public void setStedsnavn(String stedsnavn) {
        this.stedsnavn = stedsnavn;
    }

    //Overstyrer metoden equals, som er definert i klassen Object:
    public boolean equals(Poststed denAndre) {
        return this.postnr == denAndre.getPostnr();
    }

    //Implementerer metoden comparedTo fra interfacet Comparable:
    public int compareTo(Poststed denAndre) {
        //returnerer 0 hvis postnumrene er like:
        if (this.postnr == denAndre.getPostnr()) return 0;
        //hvis dette objektets postnr er mindre enn det
        //andre objektets postnr, returneres et negativt tall:
        else if(this.postnr < denAndre.getPostnr()) return -1;
        //Ellers så må dette postnummeret være større enn det
        //andre, og da returneres et positivt tall:
        else return 1;
    }

    @Override
    public String toString() {
        return "Poststed{" + "postnr=" + postnr + ", stedsnavn='" + stedsnavn + '\'' + '}';
    }
}
