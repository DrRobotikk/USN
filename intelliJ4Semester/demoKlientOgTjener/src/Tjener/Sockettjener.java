package Tjener;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Sockettjener {
    public static void main(String[] args) {
        //Definerer et portnummer:
        final int PORTNR = 1250;
        try {
            //Oppretter en tjener-objekt:
            ServerSocket tjener = new ServerSocket(PORTNR);
            System.out.println("Beskjed fra tjeneren: Nå venter vi");
            //Oppretter en forbindelse:
            Socket forbindelse = tjener.accept();
            //Åpner en strøm for kommunikasjon:
            InputStreamReader leseforbindelse = new InputStreamReader(forbindelse.getInputStream());
            BufferedReader leseren = new BufferedReader(leseforbindelse);
            //Lager en skriver:
            PrintWriter skriveren = new PrintWriter(forbindelse.getOutputStream(), true);
            skriveren.println("Hei, du er nå koblet til tjeneren");
            skriveren.println("Skriv inn hva du vil, så skal jeg gjenta det: ");
            //Leser input fra klienten:
            String linje = leseren.readLine();
            //Starter en løkke som gjentar det klienten skriver:
            while (linje != null) {
                skriveren.println("Du skrev: " + linje);
                linje = leseren.readLine();
            }//Løkke
            //Lukker forbindelsen:
            leseren.close();
            skriveren.close();
            forbindelse.close();
        }catch(Exception e) {

        }
    }

}
