// a opphøyd i b (2^3) kalles en potens
//a kalles for grunntall og b kalles for eksponent
public class PotensTest {
    public static void main(String[] args) {
        int grunntall = 2;
        int eksponent = 10;
        System.out.println(grunntall + " opphøyd i " + eksponent + " er lik " + potens(grunntall, eksponent));
    }

    //Rekursive metoden:
    public static int potens(int grunntall, int eksponent) {
        //Vi må alltid sjekke på det vi kaller for stop-casen. I dette tilfelle eksponenten:
        if (eksponent == 1) return grunntall;
        else return potens(grunntall, eksponent - 1)*grunntall;
    }
}
