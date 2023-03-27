package Treaddemo;

public class Testklient {
    public static void main(String[] args) {
        //Oppretter 5 objekter av klassen Tallskriver/ Trådobjekter:
        Tallskriver skriver1 = new Tallskriver(1);
        Tallskriver skriver2 = new Tallskriver(2);
        Tallskriver skriver3 = new Tallskriver(3);
        Tallskriver skriver4 = new Tallskriver(4);
        Tallskriver skriver5 = new Tallskriver(5);
        //Starter trådene:
        skriver1.start();
        skriver2.start();
        skriver3.start();
        skriver4.start();
        skriver5.start();
    }
}
