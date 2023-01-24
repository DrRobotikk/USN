public class FakultetTest {
    public static void main(String[] args) {
        int tall = 8;
        System.out.println("Fakultetet av " + tall +" er " + fakultet(tall));
    }

    //En rekursiv metode:
    public static int fakultet(int tall) {
        if (tall==1) return 1;
        else return fakultet(tall -1)*tall;
    }
}
