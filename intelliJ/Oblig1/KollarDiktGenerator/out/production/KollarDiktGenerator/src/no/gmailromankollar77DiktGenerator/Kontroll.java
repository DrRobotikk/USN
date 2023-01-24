package no.gmailromankollar77DiktGenerator;

//Oppretter Class for håndtering av programmet:
public class Kontroll {

    //Oppretter arrays (lister) med ord til dikt:
    public String[] artikkel = {"Den","Det"};
    public String[] adjektiv = {"Grønne","trøtte","Snille"};
    public String[] substantiv = {"Gutten","Mannen","Jenta"};
    public String[] verb = {"Kjører","Jobber","Sitter"};

    //Oppretter objekter til de forskjellige ordene i diktet
    Arrays alleOrd = new Arrays();
    Arrays lesinnArtikkel = new Arrays();
    Arrays lesinnAdjektiv = new Arrays();
    Arrays lesinnSubstantiv = new Arrays();
    Arrays lesinnVerb = new Arrays();

    //Oppretter metoder for å lese de statiske listene til objektlistene:
    public void lesinnLister() {
        for(int i = 0; i<artikkel.length;i++) {
            lesinnArtikkel.nyttObjekt(artikkel[i]);
        }

        for(int i = 0; i<adjektiv.length;i++) {
            lesinnAdjektiv.nyttObjekt(adjektiv[i]);
            alleOrd.nyttObjekt(adjektiv[i]);
        }

        for(int i = 0; i<substantiv.length;i++) {
            lesinnSubstantiv.nyttObjekt(substantiv[i]);
            alleOrd.nyttObjekt(substantiv[i]);
        }

        for(int i = 0; i<verb.length;i++) {
            lesinnVerb.nyttObjekt(verb[i]);
            alleOrd.nyttObjekt(verb[i]);
        }
    }

    //Metode for å generere enkelt dikt:
    public String enkelDikt() {

        //Henter inn listen som inneholder alle ord
        String[] listeAlleOrd= alleOrd.getListe();
        String dikt ="";

        //For-løkke som deler diktet i 4 linjer bestående av 4 ord tilfeldiggjort.
        //i= antall linjer i løkka; altså en teller
        for (int i = 0; i<16; i++) {
            int randomEnkel = (int) (Math.random()* listeAlleOrd.length);

            //Unngår null-merker i diktet
            if (listeAlleOrd[randomEnkel]==null) {
                randomEnkel= (int)(Math.random()*listeAlleOrd.length/2);
            }

            //Legger inn ord i diktet med et mellomrom
            dikt+= listeAlleOrd[randomEnkel]+" ";

            //Legges til linjeskift ved hvert fjerde ord
            if (i==3 || i==7 || i==11) {
                dikt+= "\n";
            }
        }
        return dikt;
    }

    //Genererer avansert dikt:
    public String avansertDikt() {

        String[] listeArtikkel = lesinnArtikkel.getListe();
        String[] listeAdjektiv = lesinnAdjektiv.getListe();
        String[] listeSubstantiv = lesinnSubstantiv.getListe();
        String[] listeVerb = lesinnVerb.getListe();
        String dikt ="";
        int randomArtikkel = (int)(Math.random()*listeArtikkel.length);

        //forløkke som genererer diktet
        for(int i = 0; i<4; i++){
            int randomAdjektiv = (int)(Math.random()*listeAdjektiv.length);
            int randomSubstantiv = (int)(Math.random()*listeSubstantiv.length);
            int randomVerb = (int)(Math.random()*listeVerb.length);

            if (listeArtikkel[randomArtikkel]==null) {
                randomArtikkel = (int)(Math.random()*2);
            }

            if (listeAdjektiv[randomAdjektiv]==null) {
                randomAdjektiv = (int)(Math.random()*3);
            }

            if (listeSubstantiv[randomSubstantiv]==null) {
                randomSubstantiv = (int)(Math.random()*3);
            }

            if (listeVerb[randomVerb]==null) {
                randomVerb = (int)(Math.random()*3);
            }
            //Siste linje i diktet som har annen rekkefølge:
            if (i==3){
                dikt+=listeVerb[randomVerb]+" ";
                dikt+=listeArtikkel[randomArtikkel]+" ";
                dikt+=listeAdjektiv[randomAdjektiv]+" ";
                dikt+=listeSubstantiv[randomSubstantiv]+"?";
                break;
            }

            //De tre første linjene i diktet som har samme rekkefølge:
            dikt+= listeArtikkel[randomArtikkel]+" ";
            dikt+= listeAdjektiv[randomAdjektiv]+" ";
            dikt+= listeSubstantiv[randomSubstantiv]+" ";
            dikt+= listeVerb[randomVerb]+"\n";
        }
        return dikt;
    }

    public void registrerArtikkel(String nyArtikkel) {
        lesinnArtikkel.nyttObjekt(nyArtikkel);
    }

    public void registrerAdjektiv(String nyttAdjektiv) {
        lesinnAdjektiv.nyttObjekt(nyttAdjektiv);
    }

    public void registrerSubstantiv(String nyttSubstantiv) {
        lesinnSubstantiv.nyttObjekt(nyttSubstantiv);
    }

    public void registrerVerb(String nyttVerb) {
        lesinnVerb.nyttObjekt(nyttVerb);
    }

    public void registrerAlleOrd(String nyeAlleOrd) {
        alleOrd.nyttObjekt(nyeAlleOrd);
    }

}
