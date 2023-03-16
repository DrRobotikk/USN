package application;

public class Person {
	private String fornavn;
	private String etternavn;
	private String adresse;
	
	public Person(String fornavn, String etternavn, String adresse) {
		super();
		this.fornavn = fornavn;
		this.etternavn = etternavn;
		this.adresse = adresse;
	}

	public String getFornavn() {
		return fornavn;
	}

	public void setFornavn(String fornavn) {
		this.fornavn = fornavn;
	}

	public String getEtternavn() {
		return etternavn;
	}

	public void setEtternavn(String etternavn) {
		this.etternavn = etternavn;
	}

	public String getAdresse() {
		return adresse;
	}

	public void setAdresse(String adresse) {
		this.adresse = adresse;
	}	
	
}
