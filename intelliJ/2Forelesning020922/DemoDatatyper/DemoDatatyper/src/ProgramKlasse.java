import javax.swing.JOptionPane;

public class ProgramKlasse {

	public static void main(String[] args) {
		//Bruker JOptionPane til � lese inn verdier:
		String varenavn = JOptionPane.showInputDialog("Varens navn:");
		String lestAntall = JOptionPane.showInputDialog("Antall p� lager:");
		//Vi konverterer til heltall:
		int antall = Integer.parseInt(lestAntall);
		//Leser pris:
		String lestPris = JOptionPane.showInputDialog("Skriv pris:");
		double pris = Double.parseDouble(lestPris);
		//Oppretter et objekt av klassen Vare:
		Vare vare = new Vare(varenavn, antall, pris);
		JOptionPane.showMessageDialog(null, vare.toString());

	}

}
