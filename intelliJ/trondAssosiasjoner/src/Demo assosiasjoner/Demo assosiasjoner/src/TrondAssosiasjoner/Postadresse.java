public class Postadresse implements Comparable<Postadresse> {
	private int postnr;
	private String poststed;
	
	public Postadresse(int postnr, String poststed) {
		super();
		this.postnr = postnr;
		this.poststed = poststed;
	}

	public int getPostnr() {
		return postnr;
	}

	public void setPostnr(int postnr) {
		this.postnr = postnr;
	}

	public String getPoststed() {
		return poststed;
	}

	public void setPoststed(String poststed) {
		this.poststed = poststed;
	}

	@Override
	public String toString() {
		return "Postadresse [postnr=" + postnr + ", poststed=" + poststed + "]";
	}
	
	public int compareTo(Postadresse postadresse) {
		//Postnr er deklarert som en integer:
		if(this.postnr == postadresse.getPostnr()) return 0; //samme postnr
		else if(this.postnr < postadresse.getPostnr()) return -1;//Dette postnummeret kommer foran det andre
		else return 1;
	}
	
	public boolean equals(Postadresse postadresse) {
		if(this.postnr == postadresse.getPostnr()) return true;
		else return false;
	}
	

}
