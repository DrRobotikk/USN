import javax.swing.*;

public class Tower {

    public static void main(String[] args) {
        //Spør etter antall skiver:
        int antall = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall skiver:"));
        System.out.println("Flyttingene er:");
        flytt(antall, 'A', 'B', 'C');
    }

    public static void flytt(int n, char fraTower, char tilTower, char ekstraTower) {
        if (n == 1) { //Stop-case
            System.out.println("Flytt skive " + n + " fra " + fraTower + " til " + tilTower);
        }
        else {
            flytt(n - 1, fraTower,ekstraTower,tilTower);
            System.out.println("Flytt skive " + n + " fra " + fraTower + " til " + tilTower);
            flytt(n-1, ekstraTower, tilTower, fraTower);
        }
    }
}
