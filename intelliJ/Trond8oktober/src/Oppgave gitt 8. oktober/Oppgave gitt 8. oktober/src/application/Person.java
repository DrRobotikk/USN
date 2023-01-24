import java.util.ArrayList;

public class Person implements Comparable<Person> {
	private String navn;
	private String adresse;
	private Postadresse postadresse;
	private ArrayList<Kjøretøy> kjøretøyer = new ArrayList<>();
	
	public Person(String navn, String adresse, Postadresse postadresse) {
		this.navn = navn;
		this.adresse = adresse;
		this.postadresse = postadresse;
	}
	
	public int compareTo(Person denandre) {		
		return this.navn.compareTo(denandre.getNavn());
	}
	
	public String getNavn() {
		return navn;
	}
	
	public Postadresse getPostadresse() {
		return postadresse;
	}
	
	public void nyttKjøretøy(Kjøretøy kjøretøy) {
		kjøretøyer.add(kjøretøy);
	}

	@Override
	public String toString() {
		return "Navn: " + navn + ", adresse: " + adresse + ", " + postadresse.toString();
	}
	
	public ArrayList<Kjøretøy> getKjøretøy() {
		return kjøretøyer;
	}


}
