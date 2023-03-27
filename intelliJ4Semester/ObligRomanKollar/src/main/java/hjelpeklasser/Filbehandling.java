package hjelpeklasser;

import java.io.*;

public class Filbehandling {
    //Metode for å lage en skriveforbindelse
    //til en tekstfil:

    //Lager metodene som klassemetoder:
    public static PrintWriter lagSkriveforbindelse(String filnavn) {
        try {
            FileWriter filforbindelse = new FileWriter(filnavn);
            BufferedWriter skrivebuffer = new BufferedWriter(filforbindelse);
            PrintWriter skriver =  new PrintWriter(skrivebuffer);
            return skriver;
        }catch (Exception e) {
            return null;
        }
    }
    //Slutt metode:
    public static BufferedReader lagLeseforbindelse(String filnavn) {
        try {
            FileReader filforbindelse = new FileReader(filnavn);
            BufferedReader leser = new BufferedReader(filforbindelse);
            return leser;
        } catch (Exception e) {
            return null;
        }
    }
}
