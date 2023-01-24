package trond.Oblig1_2019;

import javax.swing.JOptionPane;

public class Grensesnitt {
	//Definerer en array med tekstene på knappene i hovedmenyen:
	private final String[] ALTERNATIVER = {"Enkelt dikt","Avansert dikt","Avslutt"};
	//Definerer en array med tekstene på knappene i undermenyen for enkelt dikt:
	private final String[] ENKELTALTERNATIVER = {"Registrer ord", "Skriv dikt", "Tilbake"};
	//Definerer en array med tekstene på knappene i undermenyen for avansert dikt:
	private final String[] AVANSERTALTERNATIVER = {"Registrer verb", "Registrer substantiv", "Registrer adverb", "Registrer adjektiv", "Skriv dikt", "Tilbake"};
	//Definerer tallverdier som svarer til indeksene i array:
	//Det kan være lurt (men ikke nødvendig) å definere valg som konstanter:
	private final int ENKELT = 0;
	private final int AVANSERT = 1;
	private final int AVSLUTT = 2;
	//Så opprettes et objekt av applikasjonsklassen Dikter, som skal administrere ord og lage dikt:
	Dikter dikter = new Dikter();
	
	//Metoden lesValg() skriver ut hovedmenyen og leser menyvalg:
	public int lesValg( ) {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktgenerator",JOptionPane.DEFAULT_OPTION,
		JOptionPane.PLAIN_MESSAGE,null,ALTERNATIVER,ALTERNATIVER[0]);
		return valg;
	}
	
	//Metoden lesEnkeltValg skriver undermenyen for enkelt dikt og leser valget:
	public int lesEnkeltValg() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Enkelt dikt",JOptionPane.DEFAULT_OPTION,
				JOptionPane.PLAIN_MESSAGE,null,ENKELTALTERNATIVER,ENKELTALTERNATIVER[0]);
				return valg;
	}
	
	//Metoden lesAvansertValg skriver undermenyen for avansert dikt og leser valget:
	public int lesAvansertValg() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Avansert dikt",JOptionPane.DEFAULT_OPTION,
				JOptionPane.PLAIN_MESSAGE,null,AVANSERTALTERNATIVER,AVANSERTALTERNATIVER[0]);
				return valg;
	}
	
	//Metoden regOrd() tilhører enkelt dikt-delen:
	public void regOrd() {
		String ord = JOptionPane.showInputDialog("Skriv et ord: ");
		//Kaller metoden regOrd() i dikter. Denne metoden returnerer ikke noe:
		dikter.regOrd(ord);
	}
	
	//Metoden regVerb() tilhører den avanserte dikt-delen:
	public void regVerb() {
		String ord = JOptionPane.showInputDialog("Skriv et verb: ");
		//Kaller metoden regVerb() i dikter. Denne metoden returnerer true hvis det 
		//var plass til et nytt ord i arrayen for verb:
		boolean ok = dikter.regVerb(ord);
		if(!ok) JOptionPane.showMessageDialog(null, "Ikke plass til flere verb");
	}
	
	//Metoden regSunstantiv() tilhører den avanserte dikt-delen:
	public void regSubstantiv() {
		String ord = JOptionPane.showInputDialog("Skriv et substantiv: ");
		//Kaller metoden regSub() i dikter. Denne metoden returnerer true hvis det 
		//var plass til et nytt ord i arrayen for substantiv:
		boolean ok = dikter.regSub(ord);
		if(!ok) JOptionPane.showMessageDialog(null, "Ikke plass til flere substantiv");
	}
	
	//Metoden regAdjektiv() tilhører den avanserte dikt-delen:
	public void regAdjektiv() {
		String ord = JOptionPane.showInputDialog("Skriv et adjektiv: ");
		//Kaller metoden regAdj() i dikter. Denne metoden returnerer true hvis det 
		//var plass til et nytt ord i arrayen for adjektiv:
		boolean ok = dikter.regAdj(ord);
		if(!ok) JOptionPane.showMessageDialog(null, "Ikke plass til flere adjektiv");
	}
	
	//Metoden regAdverb() tilhører den avanserte dikt-delen:
	public void regAdverb() {
		String ord = JOptionPane.showInputDialog("Skriv et adverb: ");
		//Kaller metoden regAdv() i dikter. Denne metoden returnerer true hvis det 
		//var plass til et nytt ord i arrayen for adverb:
		boolean ok = dikter.regAdv(ord);
		if(!ok) JOptionPane.showMessageDialog(null, "Ikke plass til flere adverb");
	}
 	
	//Metode som behandler valg i menyen for avansert dikt:
	public void avansertDikt() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesAvansertValg();
			switch(valg) {
			case 0 : regVerb();
				break;
			case 1 : regSubstantiv();
				break;
			case 2 : regAdverb();
				break;
			case 3 : regAdjektiv();
				break;
			case 4 : lagAvansert();
				break;			 
			default : fortsett = false;
			} //switch
		} //while
	} 
	
	//Metode som behandler valg i menyen for enkelt dikt:
	public void enkeltDikt() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesEnkeltValg();
			switch(valg) {
			case 0 : regOrd();
				break;
			case 1 : lagDikt();
				break;
			default : fortsett = false;
			} //switch
		} //while
	}
	
	//Metoden start behandler hovedmenyen og holder hele 
	//programmet i gang:	
	public void start() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValg();
			switch(valg) {
				case ENKELT : enkeltDikt();
					break;
				case AVANSERT : avansertDikt();
					break;
				case AVSLUTT : fortsett = false;
			} //switch
		} //while
	}
	
	//Metoden som henter et avansert dikt fra dikter
	//ved å kalle metoden lagAvansert(), for deretter
	//å skrive det ut:
	public void lagAvansert() {
		String dikt = dikter.lagAvansert();
		JOptionPane.showMessageDialog(null,dikt);
	}
	
	
	//Metoden som henter et enkelt dikt fra dikter
	//ved å kalle metoden lagDikt(), for deretter
	//å skrive det ut:
	public void lagDikt() {
		String dikt = dikter.lagDikt();
		JOptionPane.showMessageDialog(null,dikt);
	}

}
