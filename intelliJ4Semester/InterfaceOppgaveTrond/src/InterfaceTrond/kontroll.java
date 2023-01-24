package InterfaceTrond;

import java.util.ArrayList;

public class kontroll implements Filtrering{
    private ArrayList<Integer> talliste = new ArrayList<>();

    @Override
    public boolean filtrer(int tall, int deletall) {
        if (tall%deletall == 0) return true;
        else return false;
    }


    //Metode for å fylle tallisten med ønskede tall:
    public void fyllListe(int makstall) {
        talliste.clear();
        for (int i = 1; i <= makstall; i++) {
            talliste.add(i);
        }
    }

    //Metode som bruker lambda-programmering:
    public void lambdaBruk(int makstall, int deletall) {
        fyllListe(makstall);
        System.out.println("Med lambda:");
        talliste.stream().filter(x -> x%deletall == 0).forEach(x -> System.out.println(x));
    }

    //Metode som bruker løkke i stedet for lambda-programmering:
    public void loopBruk(int makstall, int deletall) {
        fyllListe(makstall);
        //Lager en String for utskrift med JOptionPane:
        String uttekst = "";
        //Starter løkka:
        for (int j = 0; j < makstall; j++) {
            int tall = talliste.get(j);
            //Bruker metoden filtrer(). Hvis delelig, så legges tallet til utteksten:
            if (filtrer(tall, deletall)) {
                uttekst+=tall;
                uttekst+= "\n";
            }
        }
        System.out.println("Med løkke:");
        System.out.println(uttekst);
    }
}
