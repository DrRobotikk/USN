package TrondMetoder;

import java.util.Arrays;

public class testKlient {
    public static void main(String[] args) {
        //Oppretter en array for Poststeder:
        Poststed[] poststeder = new Poststed[3];
        poststeder[0] = new Poststed(3518, "Hønefoss");
        poststeder[1] = new Poststed(3000, "Drammen");
        poststeder[2] = new Poststed(3511, "Hønefoss");

        //Skriver ut den usorterte arrayen:
        for(int i = 0; i<poststeder.length; i++) {
            System.out.println(poststeder[i].toString());
        }

        Arrays.sort(poststeder);
        System.out.println();
        System.out.println("Sortert array:");
        for(int j = 0; j<poststeder.length;j++) {
            System.out.println(poststeder[j].toString());
        }

        //Vi skal bruke binærsøk:
        //Vi søker først etter postnr 3000, som vi vet finnes
        Poststed søkeobjekt = new Poststed(3000, null);

        int indeks = Arrays.binarySearch(poststeder, søkeobjekt);
        System.out.println("Søker etter postnummer 3000:");
        if(indeks >=0) {
            System.out.println("indeks: "+ indeks);
            System.out.println(poststeder[indeks].toString());
        }
        else System.out.println("Postnummeret finnes ikke.");

        //Lager et søkeobjekt med et postnr som ikke finnes
        søkeobjekt = new Poststed(4000, null);

        indeks = Arrays.binarySearch(poststeder, søkeobjekt);
        System.out.println("Søker etter postnummer 4000:");
        if(indeks >=0) {
            System.out.println("indeks: "+ indeks);
            System.out.println(poststeder[indeks].toString());
        }
        else System.out.println("Postnummeret finnes ikke.");
    }
}
