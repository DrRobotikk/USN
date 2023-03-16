package Bilregister;

import Hjelpeklasser.Filbehandling;
import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Bilregister {
    List<Person> personer = new ArrayList<>();
    List<Bil> biler = new ArrayList<>();
    List<Postadresse> postadresser = new ArrayList<>();
    //String bilfil = "bilfil.csv";
    //String personfil = "personfil.csv";
    //String postadressefil = "postadressefil.csv";

    String bilfil = "bilfil.dat";
    String personfil = "personfil.dat";
    String postadressefil = "postadressefil.dat";


    public void regBil(Bil bil) {
        biler.add(bil);
    }

    public void regPerson(Person person) {
        personer.add(person);
    }

    public void regPostadresse(Postadresse postadresse) {
        postadresser.add(postadresse);
    }

    //Søkemetoder:
    public Postadresse finnPostadresse(String postnr) {
        for (int i = 0; i < postadresser.size(); i++) {
            Postadresse p = postadresser.get(i);
            if (p.getPostnr().equals(postnr)) {
                return p;
            }
        }
        return null;
    }

    public Person finnPerson(String enavn) {
        for (int i = 0; i < personer.size(); i++) {
            Person p = personer.get(i);
            if (p.getEnavn().equals(enavn)) {
                return p;
            }
        }
        return null;
    }

    public Bil finnBil(String regnr) {
        for (int i = 0; i < biler.size(); i++) {
            Bil b = biler.get(i);
            if (b.getRegnr().equals(regnr)) {
                return b;
            }
        }
        return null;
    }

    /*
    //Lagringsmetoder:
    public void skrivPersoner(String filnavn) throws Exception {
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i = 0; i < personer.size(); i++) {
                utfil.println(personer.get(i).toFile());
            }//Løkke
            utfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lagre personer");
        }
    }

    public void skrivPostadresse(String filnavn) throws Exception {
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i = 0; i < postadresser.size(); i++) {
                utfil.println(postadresser.get(i).toFile());
            }//Løkke
            utfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lagre postadresser");
        }
    }

    public void skrivBiler(String filnavn) throws Exception {
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i = 0; i < biler.size(); i++) {
                utfil.println(biler.get(i).toFile());
            }//Løkke
            utfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lagre biler");
        }
    }

    //Innlesing:
    public void lesPostadresser(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            //Leser første linje:
            String linje = innfil.readLine();
            while (linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                String postnr = innhold.nextToken();
                String poststed = innhold.nextToken();
                postadresser.add(new Postadresse(postnr, poststed));
                //Leser neste linje
                linje = innfil.readLine();
            }//Løkka
            innfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lese postadressefil");
        }
    }

    public void lesPersoner(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            //Leser første linje:
            String linje = innfil.readLine();
            while (linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                String enavn = innhold.nextToken();
                String fnavn = innhold.nextToken();
                String gateadresse = innhold.nextToken();
                //Leser postnr fra fil, der den opptrer som en fremmednøkkel:
                String postnr = innhold.nextToken();
                //Finner referanse til postadresseobjektet:
                Postadresse postadresse = finnPostadresse(postnr);
                personer.add(new Person(enavn, fnavn, gateadresse, postadresse));
                //Leser neste linje:
                linje = innfil.readLine();
            }//Løkka
            innfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lese personfil");
        }
    }

    public void lesBiler(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            //Leser første linje:
            String linje = innfil.readLine();
            while (linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                String regnr = innhold.nextToken();
                String merke = innhold.nextToken();
                String modell = innhold.nextToken();
                //Eierens etternavn som fungere som fremmednøkkel:
                String enavn = innhold.nextToken();
                //Vi bruker denne til å finne referansen til eierobjektet:
                Person eier = finnPerson(enavn);
                Bil bil = new Bil(regnr, merke, modell, eier);
                biler.add(bil);
                //Legger bilen inn i eierobjektet:
                eier.regBil(bil);
                //Leser neste linje:
                linje = innfil.readLine();
            }//Løkkeslutt
            innfil.close();
        } catch (Exception e) {
            throw new Exception("Kan ikke lese bilfil");
        }
    }//Metodeslutt
     */

    public void lesAlleFiler() throws Exception {
        try {
            lesPostadresser("postadressefil.csv");
            lesPersoner("personfil.csv");
            lesBiler("bilfil.csv");
        } catch (Exception e) {
            throw e;
        }
    }

    public void skrivAlleFiler() throws Exception {
        try {
            skrivPostadresser(postadressefil);
            skrivPersoner(personfil);
            skrivBiler(bilfil);
        }catch (Exception e) {
            throw e;
        }
    }



    //FORTSETTELSE 22.03.23
    public void skrivPostadresser() {
        try {
            ObjectOutputStream utfil = Filbehandling.lagSkriveforbindelseBin(postadressefil
            utfil.writeObject(postadresser);
            utfil.close();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void lesPostadresser() {
        postadresser.clear();
        try {
            ObjectInputStream innfil = Filbehandling.lagLeseforbindelseBin(postadressefil);
            postadresser = (ArrayList<Postadresse>) innfil.readObject();
            innfil.close();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void skrivBiler() {

    }

    public void lesBiler() {

    }

    public void skrivPersoner() {

    }

    public void lesPersoner() {

    }
}
