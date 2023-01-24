import java.util.ArrayList;

public class Stream {
    public static void main(String[] args) {
        ArrayList<Integer> samling = new ArrayList<>();
        samling.add(5);
        samling.add(7);
        samling.add(4);
        samling.add(12);

        System.out.println("Skriver ut hele samlingen:");

        for (int i = 0; i < samling.size(); i++) {
            System.out.println(samling.get(i));
        }
        System.out.println();
        System.out.println("Skriver ut partall");
        //Lager en stream av arralisten og bruker stream's metoder:
        samling.stream().filter(x -> x%2 == 0).forEach(x -> System.out.println(x));

        System.out.println();
        System.out.println("Skriver ut oddetall:");
        samling.stream().filter(x -> x%2 != 0).forEach(x -> System.out.println(x));
    }
}
