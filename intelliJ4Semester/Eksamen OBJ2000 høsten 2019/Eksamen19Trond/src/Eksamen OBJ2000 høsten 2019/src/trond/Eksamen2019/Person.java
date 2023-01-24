//Oppgave 1b:
public class Person implements Comparable<Person> {
	private long personnummer;
	private String navn;
	private String adresse;
	
	public Person(long personnummer, String navn, String adresse) {
		this.personnummer = personnummer;
		this.navn = navn;
		this.adresse = adresse;
	}

	public long getPersonnummer() {
		return personnummer;
	}

	public String getNavn() {
		return navn;
	}

	public String getAdresse() {
		return adresse;
	}

	public void setNavn(String navn) {
		this.navn = navn;
	}

	public void setAdresse(String adresse) {
		this.adresse = adresse;
	}
	
	public int compareTo(Person denandre) {
		if (this.personnummer > denandre.getPersonnummer()) return 1;
		else if (this.personnummer < denandre.getPersonnummer()) return -1;
		else return 0;
	}
	
	public boolean equals(Person denandre) {
		if (this.personnummer == denandre.getPersonnummer()) return true;
		else return false;
	}

	@Override
	public String toString() {
		return "Personnummer: " + personnummer + ", navn: " + navn + ", adresse: " + adresse;
	}	

}
