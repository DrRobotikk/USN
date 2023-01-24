public class Kj�ret�y implements Comparable<Kj�ret�y> {
	private String regnr;
	private String modell;
	private Person eier;
	public Kj�ret�y(String regnr, String modell, Person eier) {
		super();
		this.regnr = regnr;
		this.modell = modell;
		this.eier = eier;
	}
	public String getRegnr() {
		return regnr;
	}
	public void setRegnr(String regnr) {
		this.regnr = regnr;
	}
	public String getModell() {
		return modell;
	}
	public void setModell(String modell) {
		this.modell = modell;
	}
	public Person getEier() {
		return eier;
	}
	public void setEier(Person eier) {
		this.eier = eier;
	}
	@Override
	public String toString() {
		return "Kj�ret�y [regnr=" + regnr + ", modell=" + modell + ", eier=" + eier + "]";
	}
	
	public int compareTo(Kj�ret�y kj�ret�y) {
		return this.regnr.compareTo(kj�ret�y.getRegnr());
	}
	
	public boolean equals(Kj�ret�y kj�ret�y) {
		return this.regnr.equals(kj�ret�y.getRegnr());
	}

}
