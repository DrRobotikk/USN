package com.example.obligroman.hjelpeklasser;

import java.io.*;

public class Filbehandling {
    //Tar imot filnavn og oppretter eller overskriver filen med filnavnet
    public static PrintWriter lagSkriveforbindelse(String filnavn) {
        try {
            // oppretter eller overskriver filen med filnavnet
            FileWriter filforbindelse = new FileWriter(filnavn);
            // oppretter et bufferedwriter objekt gjennom FileWriter objektet
            BufferedWriter skrivebuffer = new BufferedWriter(filforbindelse);
            // Skriver den formaterte teksten til fil
            PrintWriter skriver =  new PrintWriter(skrivebuffer);
            return skriver;
        }catch (Exception e) {
            return null;
        }
    }
    // Leser spesifiserte filer og returnerer et BufferedReader objekt
    public static BufferedReader lagLeseforbindelse(String filnavn) {
        try {
            // åpner filleser til den spesifiserte filen
            FileReader filforbindelse = new FileReader(filnavn);
            // oppretter bufferedreader for å lese innholdet i filen
            BufferedReader leser = new BufferedReader(filforbindelse);
            // returnerer BufferedReader objektet
            return leser;
        } catch (Exception e) {
            return null;
        }
    }
}
