
public class Vare {
	String varenavn;
	int antall;
	double pris;
	
	public Vare(String varenavn, int antall, double pris) {
		this.varenavn = varenavn;
		this.antall = antall;
		this.pris = pris;
	}
	
	public String toString() {
		return "Varenavn: " + varenavn + ", Antall p� lager: " + antall + ", Pris: " + pris;
	}
	
	

}
