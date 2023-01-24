package no.usn.trond.verdier;

public class TegnKontroll {
	
	public String lagVerdier(char start, char slutt) {
		//Vi skal bygge opp en String som skal returneres.
		//Vi lager først en tom String:
		String uttekst = "";
		//Konverterer start og slutt til int:
		int startverdi = start; //En char er egentlig en int
		int sluttverdi = slutt;
		int verdi = startverdi;
		//Starter en løkke:
		for(int i = startverdi; i < sluttverdi + 1; i++) {
			uttekst+= "Tegnet " + start + " har Unicode-verdien " + verdi + "\n";
			verdi++;
			start++;
		} //Dlutt løkke
		return uttekst;
	}

}
