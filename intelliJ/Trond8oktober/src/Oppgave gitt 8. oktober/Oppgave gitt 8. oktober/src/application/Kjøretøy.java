public class Kjøretøy implements Comparable<Kjøretøy> {
	private String registreringsnr;
	private String modell;
	private Person eier;
	
	//Jeg lager tre konstruktører her:
	public Kjøretøy(String registreringsnr) {
		this.registreringsnr = registreringsnr;
	}
	
	public Kjøretøy(String registreringsnr, String modell) {
		this.registreringsnr = registreringsnr;
		this.modell = modell;
	}
	
	public Kjøretøy(String registreringsnr, String modell, Person eier) {
		this.registreringsnr = registreringsnr;
		this.modell = modell;
		this.eier = eier;
	}

	public String getRegistreringsnr() {
		return registreringsnr;
	}
	
	public void setEier(Person eier) {
		this.eier = eier;
	}
	
	//Metode som returnerer en referanse til eieren:
	public Person getEier() {
		return eier;
	}

	public String getModell() {
		return modell;
	}
	
	public int compareTo(Kjøretøy kjøretøy) {
		return this.registreringsnr.compareTo(kjøretøy.getRegistreringsnr());
	}
	
	

	@Override
	public String toString() {
		return "Kjøretøy [registreringsnr=" + registreringsnr + ", modell=" + modell + "]";
	}	
	


}
