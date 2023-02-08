package applikasjon;

import hjelpeklasser.Filbehandling;

import java.io.*;
import java.util.HashMap;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Kontroll {
    HashMap<Integer, Vare> vareliste = new HashMap<>();
    private String filnavn = "varer.csv";

    public void nyVare(Integer nokkel,Vare vare) {
        vareliste.put(nokkel, vare);
    }

    public void empty(){
        vareliste.clear();
    }

    //Metode for å lage en iterator
    public Iterator<Vare> getIterator() {
        return vareliste.values().iterator();
    }

    //søkemetode
    public Vare finnVare(int varenr) {
        return vareliste.get(varenr);
    }

    //Metode for å lagre på fil:
    public void lagreVarer(String filnavn){
        try{

            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            Iterator<Vare> it = getIterator();
            while(it.hasNext()){
                Vare v = it.next();
                utfil.println(v.toFile());

            }
            utfil.close();
        }catch(Exception e){}

    }

    public void lesVarer(String filnavn){
        String innlinje;
        StringTokenizer inndata;
        try{
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);
            while(innfil.ready()){
                innlinje = innfil.readLine();
                inndata = new StringTokenizer(innlinje, ";");
                int varenr = Integer.parseInt(inndata.nextToken());
                String varenavn = inndata.nextToken();
                int beholdning = Integer.parseInt(inndata.nextToken());
                vareliste.put(varenr, new Vare(varenr, varenavn, beholdning));

            }//
            innfil.close();

        }catch(Exception e){}
    }

}
