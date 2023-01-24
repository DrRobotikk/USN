import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Grensesnitt {
	//Oppretter et objekt av Kontroll:
	Kontroll kontroll = new Kontroll();
	//Definerer en array med tekstene på knappene i menyen:
	private final String[] ALTERNATIVER = {"Nytt kjøretøy","Finn kjøretøy","Skrive ut kjøretøy","Avslutt"};
	
	private final int NYBIL = 0;
	private final int FINNBIL = 1;
	private final int SKRIVBIL = 2;
	private final int AVSLUTT = 3;
	
	public Grensesnitt() {
		//Lager noen objekter:
		kontroll.nyPostadresse("3510", "Hønefoss");
		kontroll.nyPostadresse("3000", "Drammen");
		kontroll.nyPerson("Ole", "Gaten 2", "3510");
		kontroll.nyPerson("Lise", "Veien 3", "3000");
		Person person = kontroll.finnPerson("Ole");
		Kjøretøy kjør = new Kjøretøy("AB12345", "Subaru Forester", person);
		person.nyttKjøretøy(kjør);
		kontroll.nyttKjøretøy(kjør);
	}
	
	//Metoden lesValg() skriver ut hovedmenyen og leser menyvalg:
	public int lesValg( ) {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktgenerator",JOptionPane.DEFAULT_OPTION,
		JOptionPane.PLAIN_MESSAGE,null,ALTERNATIVER,ALTERNATIVER[0]);
		return valg;
	}
	
	//Metoden start behandler hovedmenyen og holder hele 
		//programmet i gang:	
		public void start() {
			boolean fortsett = true;
			while(fortsett) {
				int valg = lesValg();
				switch(valg) {
					case NYBIL : nyttKjøretøy();
						break;
					case FINNBIL : finnKjøretøy();
						break;
					case SKRIVBIL : skrivKjøretøy();
						break;
					case AVSLUTT : fortsett = false;
				} //switch
			} //while
		}
		
		public void nyttKjøretøy() {
			String regnr = JOptionPane.showInputDialog("Regnr: ");
			String modell = JOptionPane.showInputDialog("Modell:");
			String eiernavn = JOptionPane.showInputDialog("Eiers navn:");
			//Finner referanse til eieren:
			Person eier = kontroll.finnPerson(eiernavn);
			System.out.println(eier.toString());
			kontroll.nyttKjøretøy(new Kjøretøy(regnr, modell, eier));
		}
		
		public void finnKjøretøy() {
			String regnr = JOptionPane.showInputDialog("Regnr:");
			Kjøretøy kjøretøy = kontroll.finnKjøretøyBinært(regnr);
			if(kjøretøy !=null) JOptionPane.showMessageDialog(null, kjøretøy.toString());
			else JOptionPane.showMessageDialog(null, "Finner ikke kjøretøyet");
			
		}
		
		public void skrivKjøretøy() {
			ArrayList<Kjøretøy> kjøretøyene = kontroll.getKjøretøy();
			String uttekst = "";
			for(Kjøretøy k : kjøretøyene) {
				uttekst+=k.toString() + "\n";
			}
			JOptionPane.showMessageDialog(null,  uttekst);
		}
	

}
