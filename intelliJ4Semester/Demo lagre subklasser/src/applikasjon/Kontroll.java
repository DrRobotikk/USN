package applikasjon;

import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Kontroll {
    private ArrayList<Sensur> sensurering = new ArrayList<>();

    public void nySensur(Sensur sensur) {
        sensurering.add(sensur);
    }

    public ArrayList<Sensur> getSensur() {
        return sensurering;
    }

    public void lagre(String filnavn) {
        try{
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (Sensur s : sensurering) {
                utfil.println(s.toFile());
            }
            utfil.close();
        }catch (Exception e) {

        }
    }
    //Innlesingsmetoden må identifisere hva slags subklasse en linje representerer:
    public void lese(String filnavn) {
        sensurering.clear();
        try {
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);
            String linje = innfil.readLine();
            while (linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                //Leser første tegn, som identifiserer subklassen:
                String type = innhold.nextToken();
                if (type.equals("M")) lesMuntlig(innhold);
                else if (type.equals("S")) lesSkriftlig(innhold);
                else lesProsjekt(innhold);
                linje = innfil.readLine();
            }
            innfil.close();
        }catch (Exception e) {

        }
    }

    public void lesMuntlig(StringTokenizer innhold) {
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        double antalltimer = Double.parseDouble(innhold.nextToken());
        sensurering.add(new MuntligSensur(fag, eksamenstype, antalltimer));
    }
    public void lesSkriftlig(StringTokenizer innhold) {

    }

    public void lesProsjekt(StringTokenizer innhold) {

    }
}
