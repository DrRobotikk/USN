package StjerneTegning.StjerneTegning.src.no.usn.trond.stjerner;

import javax.swing.JOptionPane;

public class Grensesnitt {
	TegneKontroll kontroll = new TegneKontroll();
	private final String[] ALTERNATIVER = {"Trekant", "Pyramide", "Avslutt"};
	
	public int lesValg() {
		//Denne metoden setter opp menyen, leser valget og returnerer dette:
		//Vi bruker JOptionPane-metoden showOptionDialog som returnerer en int:
		int valg = JOptionPane.showOptionDialog(
				null, //Gjør ikke noe med denne
				"Gjør et valg:", //Ledetekst
				"Tegneprogram", //Tittel på menyen
				JOptionPane.DEFAULT_OPTION, //Klassekonstant 
				JOptionPane.PLAIN_MESSAGE, //Klassekonstant 
				null, //Lar stå
				ALTERNATIVER, //Valgene
				ALTERNATIVER[0]); //Default valg		
		return valg; //Posisjonen i ALTERNATIVER
	}
	
	public void meny() {
		//Bruker en løkke styrt av en boolean:
		boolean fortsett = true;
		while(fortsett) {
			//Setter opp menyen og leser valg:
			int valg = lesValg();
			//Bruker en case-blokk for å behandle valget:
			switch(valg) {
			case 0 : tegnTrekant();
			break;
			case 1 : tegnPyramide();
			break;
			default : fortsett = false;
			}
		}
	}
	
	public void tegnTrekant() {
		//Ber brukeren skrive antall linjer:
		int antall = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer:"));
		//Kaller metoden tegnTrekant i TegneKontroll:
		String tegning = kontroll.tegnTrekant(antall);
		JOptionPane.showMessageDialog(null, tegning);
		
	}
	
	public void tegnPyramide() {
		//Ber brukeren skrive antall linjer:
				int antall = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer:"));
				//Kaller metoden tegnTrekant i TegneKontroll:
				String tegning = kontroll.tegnPyramide(antall);
				JOptionPane.showMessageDialog(null, tegning);
	}

}
