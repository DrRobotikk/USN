package no.usn.trond.verdier;

import javax.swing.JOptionPane;

public class VerdiProgram {

	public static void main(String[] args) {
		//Oppretter et objekt av klassen TegnKontroll:
		TegnKontroll kontroll = new TegnKontroll();
		//Leser f�rste tegn:
		String lestTegn = JOptionPane.showInputDialog("Skriv f�rste tegn:");
		//I en String ligger teksten som en String[].
		//Vi henter ut det f�rste tegnet i teksten:
		char start = lestTegn.charAt(0);
		//Leser siste tegn:
		lestTegn = JOptionPane.showInputDialog("Skriv siste tegn:");
		char slutt = lestTegn.charAt(0);
		//Kaller metoden lagVerdier i TegnKontroll:
		String uttekst = kontroll.lagVerdier(start, slutt);
		JOptionPane.showMessageDialog(null, uttekst);
	}

}
