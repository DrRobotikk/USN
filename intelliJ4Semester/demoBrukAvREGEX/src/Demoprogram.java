import javax.swing.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demoprogram {

    private static final String EMAIL_PATTERN = "^[a-zA-Z0-9_+&*-]+(?:\\."+
            "[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-z" +
            "A-Z]{2,7}$";
    private static Pattern monster = Pattern.compile(EMAIL_PATTERN);
    private static Matcher matcher;
    public static void main(String[] args) {
        String epost = "trond@usn.no";
        sjekkEpost(epost);
        epost = "trond@usn,no";
        sjekkEpost(epost);
        epost = "trond#usn";
        sjekkEpost(epost);
    }

    public static boolean validate(final String post) {
        matcher = monster.matcher(post);
        return matcher.matches();
    }

    public static void sjekkEpost(String epost) {
        boolean gyldig = validate(epost);
        if (gyldig) {
            JOptionPane.showMessageDialog(null, "Eposten " + epost +" er en gyldig adresse");
        } else {
            JOptionPane.showMessageDialog(null, "Eposten " + epost +" er ikke en gyldig adresse");
        }
    }

}
