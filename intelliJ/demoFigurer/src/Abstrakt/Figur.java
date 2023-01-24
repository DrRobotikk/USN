package Abstrakt;

public abstract class Figur {
    //Vi kan ikke lage objekter av en abstrakt klasse.
    //Den kan bare tjene som en superklasse for andre klasser.

    //Metoden beregnAreal skal ha forskjellig implementering i subklassene:
    public abstract double beregnAreal();
}
