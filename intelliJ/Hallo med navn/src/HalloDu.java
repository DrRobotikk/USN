import java.util.Scanner;

public class HalloDu {
    public static void main(String[] args) {
        System.out.println ("Hva heter du?");
        Scanner kbd = new Scanner(System.in);
        String navn = kbd.next();
        System.out.println("Hallo, "+navn);
    }
}
