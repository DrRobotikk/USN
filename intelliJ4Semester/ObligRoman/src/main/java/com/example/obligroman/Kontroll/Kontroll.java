package com.example.obligroman.Kontroll;

import com.example.obligroman.domeneklasser.Fakturalinje;
import com.example.obligroman.domeneklasser.*;
import com.example.obligroman.hjelpeklasser.Filbehandling;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.util.*;

//Definerer kontroll klassen
public class Kontroll {
    HashMap<String,Kunde> kunder = new HashMap<>();

    TreeMap<String, Vare> varer = new TreeMap<>();

    ArrayList<Kundekontakt> kundekontakter = new ArrayList<>();

    ArrayList<Faktura> fakturar = new ArrayList<>();

    ArrayList<Fakturalinje> fakturalinjer = new ArrayList<>();

    String kundefil = "kundefil.CSV";
    String varefil = "varefil.CSV";
    String kundekontaktfil = "kundekontaktfil.CSV";
    String fakturafil = "fakturafil.CSV";
    String fakutralinjefil = "fakturalinjefil.CSV";

    //Metode for å for å finne en kunde basert på kundenummer
    public Vare finnVare(String varenr){
        return varer.get(varenr);
    }

    public Kunde finnKunde(String kundenr) {
        return kunder.get(kundenr);}

    public ObservableList<Fakturalinje> finnFakturalinje(String fakturanr){
        ObservableList fakturalinjene = FXCollections.observableArrayList();
        for (int i = 0;i<fakturalinjer.size();i++){
            // Henter ut fakturalinje basert på indeks i arraylist
            Fakturalinje fakturalinje = fakturalinjer.get(i);
            // Legger til fakturalinjen om den har likt fakturanummer
            if (fakturalinje.getFakturanr().equals(fakturanr)){
                fakturalinjene.add(fakturalinje);
            }
        }
        return fakturalinjene;
    }

    public String generererkundenr(){
        String kundenr = "" + (kunder.size()+1);
        return kundenr;
    }

// Metode for å finne fakturalinjer basert på fakturanummer
    public void nyFaktura(String kundenr, String fakturadato, String forfallsdato){
        // Ser om kunden finnes
        if (finnKunde(kundenr) != null) {
            String fakturanr = "" + (fakturar.size()+1);
            Faktura faktura = new Faktura(fakturanr,kundenr,fakturadato,forfallsdato);
            fakturar.add(faktura);
        }
        ;



    }


// Legger til nye kunder til hashmapen som inneholder kunder
    public void nyKunde (Kunde kunde) {

        kunder.put(kunde.getKundenr(),kunde);
    }

    // Legger til nye varer i TreeMapen av varer
    public void nyVare(Vare vare) {

        varer.put(vare.getVarenr(),vare);
    }

    // Legger til nye kundekontakter til en arrayliste som inneholder kundekontakter
    public void nyKundekontakt (Kundekontakt kundekontakt) {

        kundekontakter.add(kundekontakt);
    }

    // Legger til nye fakturaer til en arrayliste som inneholder fakturaer
    public void nyFaktura (Faktura faktura) {

        fakturar.add(faktura);
    }

    public boolean rabattKunde(String kundenr){
        boolean rabatt = false;
        if (finnKunde(kundenr) instanceof Firmakunde){
            rabatt = true;
        }
        return rabatt;
    }

    // Legger til nye fakturalinjer til en arrayliste med fakturalinjer

    public void nyFakturalinje(String fakturanr, String varenr, String antall, String rabatt) {
        double varepris = finnVare(varenr).getPris();
        double totalprisUtenRabatt = varepris * Integer.parseInt(antall);
        double rabattpris = totalprisUtenRabatt * (Double.parseDouble(rabatt) / 100);
        double totalpris = totalprisUtenRabatt - rabattpris;

        // Formaterer totalprisen til å ha to desimaler:
        DecimalFormat decimalFormat = new DecimalFormat("#.00");
        String formattedTotalpris = decimalFormat.format(totalpris);

        fakturalinjer.add(new Fakturalinje(fakturanr, varenr, finnVare(varenr).getVarenavn(),
                Integer.parseInt(antall), Double.parseDouble(rabatt), Double.parseDouble(formattedTotalpris)));
    }

    // Lagrer kunder til kundefilen.
    public void lagreKunde(String kundefil){
        // Oppretter et PrintWriter objekt for filen
        PrintWriter utfilKundefil = Filbehandling.lagSkriveforbindelse(kundefil);
        // Går gjennom alle kundene og skriver dem til filen
        for (Kunde kunde : kunder.values()){
            if (kunde instanceof Privatkunde){
                utfilKundefil.println(((Privatkunde) kunde).toFile());
            } else if (kunde instanceof Firmakunde){
                utfilKundefil.println(((Firmakunde) kunde).toFile());
            }
        }
        // lukker PrintWriter objektet for å sørge for at all data er kommet til filen.
        utfilKundefil.close();
    }

// Lagrer alle varene til en varefil
    public void lagreVare(String varefil){
        // Oppretter et PrintWriter objekt for filen
        PrintWriter utfilVarefil = Filbehandling.lagSkriveforbindelse(varefil);
        // Går gjennom alle varene og skriver dem til filen
        for (Vare vare : varer.values()){
            utfilVarefil.println(vare.toFile());
        }
        // lukker PrintWriter objektet for å sørge for at all data er kommet til filen.
        utfilVarefil.close();
    }

// Lagrer alle kundekontakter til en kundekontaktfil
    public void lagreKundekontakt(String kundekontaktfil){
        // Oppretter et PrintWriter objekt for filen
        PrintWriter utfilKundekontaktfil = Filbehandling.lagSkriveforbindelse(kundekontaktfil);
        // Går gjennom alle kundekontaktene og skriver dem til filen
        for (Kundekontakt kundekontakt : kundekontakter){
            utfilKundekontaktfil.println(kundekontakt.toFile());
        }
        // lukker PrintWriter objektet for å sørge for at all data er kommet til filen.
        utfilKundekontaktfil.close();
    }

// Lagrer alle fakturaer til en fakturafil
    public void lagreFaktura(String fakturafil){
        // Oppretter et PrintWriter objekt for filen
        PrintWriter utfilFakturafil = Filbehandling.lagSkriveforbindelse(fakturafil);
        // Går gjennom alle fakturaene og skriver dem til filen
        for (Faktura faktura : fakturar){
            utfilFakturafil.println(faktura.toFile());
        }
        // lukker PrintWriter objektet for å sørge for at all data er kommet til filen.
        utfilFakturafil.close();
    }

// lagrer fakturalinjer til fakturalinjefil
    public void lagreFakturalinje(String fakturalinjefil){
        // Oppretter et PrintWriter objekt for filen
        PrintWriter utfilFakutralinjefil = Filbehandling.lagSkriveforbindelse(fakturalinjefil);
        // Går gjennom alle fakturalinjene og skriver dem til filen
        for (Fakturalinje fakturalinje : fakturalinjer){
            utfilFakutralinjefil.println(fakturalinje.toFile());
        }
        // lukker PrintWriter objektet for å sørge for at all data er kommet til filen.
        utfilFakutralinjefil.close();
    }

// Lagrer all data og parameteret peker mot hvor det skal lagres.
    public void lagre() {
        lagreKunde(kundefil);
        lagreVare(varefil);
        lagreKundekontakt(kundekontaktfil);
        lagreFaktura(fakturafil);
        lagreFakturalinje(fakutralinjefil);
    }


// Tar imot kundedata fra fil ved bruk av BufferedReader og filnavn
    public void lesKunde(String kundefil) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(kundefil);
            // Leser første linje fra filen
            String linje = innfil.readLine();
            while (linje!=null){
                // Bruker stringtokenizer til å skille mellom poster som er adskilt med ","
                StringTokenizer innhold = new StringTokenizer(linje,";");
                // Ser etter om kundetypen er P for Privatkunde eller F for Firmakunde
                String type = innhold.nextToken();
                String kundenr = innhold.nextToken();
                String kundenavn = innhold.nextToken();
                // Ser om typen er Privatkunde, legger den deretter til "kunder" map'en som privatkunde
                if (type.equals("P")){
                    String butikk = innhold.nextToken();
                    kunder.put(kundenr,new Privatkunde(kundenr,kundenavn,butikk));
                    // Ser om typen er Firmakunde, og legger den til Kunder map som Firmakunde
                } else if (type.equals("F")) {
                    double kredittgrense = Double.parseDouble(innhold.nextToken());
                    String telefonnr = innhold.nextToken();
                    kunder.put(kundenr,new Firmakunde(kundenr,kundenavn,kredittgrense,telefonnr));
                }
                // leser neste linje fra filen
                linje = innfil.readLine();
            }
            // lukker filen
            innfil.close();
        }
        catch (Exception e) {
            throw new Exception(e);
        }

    }
// Tar imot varedata fra fil ved bruk av BufferedReader og filnavn
    public void lesVare(String varefil) throws Exception {

        try {
            // åpner varefilen
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(varefil);
            // leser første linje i filen
            String linje = innfil.readLine();
            // fortsetter å lese til det ikke er mer å lese
            while (linje!=null){
                // splitter linjene til tokens med ; som skiller
                StringTokenizer innhold = new StringTokenizer(linje, ";");
                String varenr = innhold.nextToken();
                String varenavn = innhold.nextToken();
                double pris = Double.parseDouble(innhold.nextToken());
                // oppretter et nytt vare objekt og legger det til vare-map'en
                varer.put(varenr,new Vare(varenr,varenavn,pris));
                // leser neste linje
                linje = innfil.readLine();
            }
            // lukker filen
            innfil.close();
        }
        catch (Exception e) {
            throw new Exception(e);
        }
    }
// Tar imot fakturadata fra fil ved bruk av BufferedReader og filnavn
    public void lesFaktura(String fakturafil) throws Exception {

        try {
            // oppretter et buffered reader objekt til å lese fra fakturafilen
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(fakturafil);
            // Leser første linje fra filen
            String linje = innfil.readLine();
            while (linje!=null){
                // splitter linjen til tokens ved bruk av ; som skille
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String fakturanr = innhold.nextToken();
                String kundenr = innhold.nextToken();
                String dato = innhold.nextToken();
                String forfallsdato = innhold.nextToken();
                // Lager nytt Faktura objekt med de nye verdiene og legger det til i fakturalisten
                fakturar.add(new Faktura(fakturanr, kundenr, dato, forfallsdato));
                // Leser neste linje fra fil
                linje = innfil.readLine();
            }
            // Lukker filen
            innfil.close();
        }
        catch (Exception e){
            throw new Exception(e);
        }
    }

// tar imot fakturalinje data fra fil ved bruk av BufferedReader og filnavn
    public void lesFakturalinje(String fakturalinjefil) throws Exception{

        try {
            // oppretter et buffered reader objekt til å lese fra fakturalinjefilen
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(fakturalinjefil);
            // Leser første linje fra fila
            String linje = innfil.readLine();
            // Fortsetter inntil det ikke er flere linjer å lese
            while (linje!=null){
                // splitter linjen til tokens ved bruk av ; som skille
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String fakturanr = innhold.nextToken();
                String varenr = innhold.nextToken();
                String varenavn = innhold.nextToken();
                int antall = Integer.parseInt(innhold.nextToken());
                double rabatt = Double.parseDouble(innhold.nextToken());
                double totalpris = Double.parseDouble(innhold.nextToken());
                // lager nytt fakturalinje objekt
                fakturalinjer.add(new Fakturalinje(fakturanr,varenr,varenavn,antall,rabatt,totalpris));
                // Leser neste linje fra fil
                linje = innfil.readLine();
            }
            //Lukker fil
            innfil.close();
        }
        catch (Exception e){
            throw new Exception(e);
        }

    }
// Tar imot kundekontaktdata fra fil ved bruk av BufferedReader og filnavn
    public void lesKundekontakter(String kundekontaktfil) throws Exception{
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(kundekontaktfil);
            String linje = innfil.readLine();
            while (linje!=null){
                // splitter linjen til tokens ved bruk av ; som skille
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String kundenr = innhold.nextToken();
                String dato = innhold.nextToken();
                String beskrivelse = innhold.nextToken();
                // Lager nytt kundekontakt objekt
                kundekontakter.add(new Kundekontakt(kundenr,dato,beskrivelse));
                // leser neste linje fra fil
                linje = innfil.readLine();
            }
            // Lukker filen
            innfil.close();
        }
        catch (Exception e){
            throw new Exception(e);
        }
    }
    // Kaller metoder for å lese data fra filer
    public void lese() throws Exception{
        try {
            lesKunde(kundefil);
            lesVare(varefil);
            lesFaktura(fakturafil);
            lesFakturalinje(fakutralinjefil);
            lesKundekontakter(kundekontaktfil);
        }
        catch (Exception e){
            throw new Exception(e);
        }

    }




}

