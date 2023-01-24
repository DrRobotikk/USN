public class Postadresse implements Comparable<Postadresse> {

	private String postnr;
	private String poststed;
	
	public Postadresse(String postnr, String poststed) {
		this.postnr = postnr;
		this.poststed = poststed;
	}
	
	public int compareTo(Postadresse detandre) {
		return this.postnr.compareTo(detandre.getPostnr());
	}
	
	public String getPostnr() {
		return postnr;
	}
	
	public void setPoststed(String poststed) {
		this.poststed = poststed;
	}
	
	public String getPoststed() {
		return poststed;
	}

	@Override
	public String toString() {
		return "postnr: " + postnr + ", poststed: " + poststed;
	}

}
