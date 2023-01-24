package streamDemo;

import java.util.ArrayList;

public class Stream {
    public static void main(String[] args) {
        //Lager en Arraylist med heltall:
        ArrayList<Integer> samling = new ArrayList<>();
        samling.add(5);
        samling.add(7);
        samling.add(4);
        samling.add(12);

        //Skriver ut:
        for (int i = 0; i<samling.size(); i++) {
            System.out.println(samling.get(i));
        }

        //Lager en strøm og bruker den til å sortere tallene:
        System.out.println("Sortert tallrekke:");
        samling.stream().sorted().forEach(x -> System.out.println(x));

        //Plukker ut partall fra tallrekka:
        System.out.println("Partallene i tallrekken:");
        samling.stream().filter(x -> x%2 == 0).forEach(x -> System.out.println(x));

        //UTVIDELSE/ HJEMMELEKSE
        //Plukker ut oddetall fra tallrekka:
        System.out.println("Oddetallene i tallrekken:");
        samling.stream().filter(x -> x%2 ==1).forEach(x -> System.out.println(x));

        //TROND SIN VERSJON:

    }
}
