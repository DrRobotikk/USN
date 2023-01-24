package StjerneTegning.StjerneTegning.src.no.usn.trond.stjerner;

public class TegneKontroll {
	
	public String tegnTrekant(int antall) {
		//Lager en tom String:
		String tegning = "";
		int antallStjerner = 1;
		//Løkke for å lage trekantens linjer:
		//Ytre løkke som tegner linjer:
		for(int i = 0; i < antall; i++) {
			//øker antall:
			antallStjerner++;
			//Indre løkke som skriver stjerner på en linje:
			for(int j = 1; j < antallStjerner; j++) {
				tegning+='*';
			} //Slutt indre løkke
			//Når vi er ferdig med en linje, legger vi til et linjeskift:
			tegning+='\n';
		} //Slutt yrer løkke
		//Returnerer tegningen:
		return tegning;
	}
	
	public String tegnPyramide(int antall) {
		String tegning = "";
		//Vi må finne ut hvor vi skal begynne å skrive stjerner:
		//Ytre løkke
		for(int i = 1; i < antall*2; i+=2) {
			//Midtre løkke bestemmer hvor vi skal begynne å skrive *:
			for(int j = 0; j < (antall - i/2); j++) {
				//Skriver mellomrom:
				tegning+=" ";
			} //Slutt midtre løkke
			//Ny løkke for å skrive stjerner:
			for(int k = 0; k < i; k++) {
				tegning+='*';
			}
			//Legger til linjeskift:
			tegning+='\n';
		}
		return tegning;
	}

}
