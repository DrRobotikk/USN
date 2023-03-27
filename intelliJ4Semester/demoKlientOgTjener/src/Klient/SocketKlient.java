package Klient;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class SocketKlient {
    public static void main(String[] args) {
        //Definerer et portnummer:
        final int PORTNR = 1250;
        //Bruker en scanner for å lese fra tastaturet:
        Scanner leser = new Scanner(System.in);
        System.out.println("Oppgi navnet på tjeneren: ");
        String tjenerNavn = leser.nextLine();
        //Setter opp en forbindelse:
        try {
            //Oppretter en klient-objekt:
            Socket forbindelse = new Socket(tjenerNavn, PORTNR);
            System.out.println("Nå er forbindelsen opprettet");
            //Åpner leseforbindelse:
            InputStreamReader leseforbindelse = new InputStreamReader(forbindelse.getInputStream());
            BufferedReader leseren = new BufferedReader(leseforbindelse);
            //Åpner skriveforbindelse:
            PrintWriter skriveren = new PrintWriter(forbindelse.getOutputStream(), true);
            //Leser fra tjeneren og skriver til konsollet:
            String inn1 = leseren.readLine();
            String inn2 = leseren.readLine();
            //Skriver ut som en kontroll:
            System.out.println(inn1 + "\n" + inn2);
            String enlinje = leser.nextLine();
            //Lager en løkke:
            while (!enlinje.equals("")) {
                //Sender enlinje til tjeneren:
                skriveren.println(enlinje);
                //Leser responsen fra tjeneren:
                String respons = leseren.readLine();
                //Skriver ut responsen:
                System.out.println("Fra tjeneren: " + respons);
                //Leser en ny linje fra konsollet:
                enlinje = leser.nextLine();
            }//Løkke
            //Lukker forbindelsen:
            leseren.close();
            skriveren.close();
            forbindelse.close();
        }catch (Exception e) {}
    }
}
