//Opgave 1a:
public class Kurs implements Comparable<Kurs>{
	private String kurskode;
	private String kursnavn;
	private double studiepoeng;
	
	public Kurs(String kurskode, String kursnavn, double studiepoeng) {
		this.kurskode = kurskode;
		this.kursnavn = kursnavn;
		this.studiepoeng = studiepoeng;
	}

	public String getKurskode() {
		return kurskode;
	}

	public String getKursnavn() {
		return kursnavn;
	}

	public double getStudiepoeng() {
		return studiepoeng;
	}
	
	public int compareTo(Kurs denandre) {
		return this.kurskode.compareTo(denandre.getKurskode());
		
	}
	
	public boolean equals(Kurs denandre) {
		return this.kurskode.contentEquals(denandre.getKurskode());
	}

	public String toString() {
		return "Kurskode: " + kurskode + ", kursnavn: " + kursnavn + ", studiepoeng: " + studiepoeng;
	}	

}
