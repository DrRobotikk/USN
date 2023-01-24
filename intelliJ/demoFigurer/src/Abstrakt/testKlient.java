package Abstrakt;

import javax.swing.*;

public class testKlient {

    public static void main(String[] args) {
        sirkel Sirkel = new sirkel(10);
        trekant Trekant = new trekant(5,6);
        kvadrat Kvadrat = new kvadrat(4);
        System.out.println("Arealet av Sirkelen: "+ Sirkel.beregnAreal());
        System.out.println("Arealet av Trekanten: "+ Trekant.beregnAreal());
        System.out.println("Arealet av Kvadraten: "+ Kvadrat.beregnAreal());
    }
}
