package application;

public class Kunde {
	private int kundenr;
	private String fornavn;
	private String etternavn;
	private String adresse;
	private String postnr;
	private String kj�nn;
	
	public Kunde(int kundenr, String fornavn, String etternavn, String adresse, String postnr, String kj�nn) {
		this.kundenr = kundenr;
		this.fornavn = fornavn;
		this.etternavn = etternavn;
		this.adresse = adresse;
		this.postnr = postnr;
		this.kj�nn = kj�nn;
	}

	public int getKundenr() {
		return kundenr;
	}

	public void setKundenr(int kundenr) {
		this.kundenr = kundenr;
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

	public String getPostnr() {
		return postnr;
	}

	public void setPostnr(String postnr) {
		this.postnr = postnr;
	}

	public String getKj�nn() {
		return kj�nn;
	}

	public void setKj�nn(String kj�nn) {
		this.kj�nn = kj�nn;
	}	
	
}
