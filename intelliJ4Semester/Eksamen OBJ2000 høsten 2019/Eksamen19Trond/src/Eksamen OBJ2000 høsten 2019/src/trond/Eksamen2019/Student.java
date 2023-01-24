import java.util.ArrayList;

//Oppgave 1 c:
public class Student extends Person {
	private String studieprogram;
	private ArrayList<Kurs> kursdeltagelse = new ArrayList<>();;
	
	public Student(long personnummer, String navn, String adresse, String studieprogram) {
		super(personnummer, navn, adresse);
		this.studieprogram = studieprogram;
		this.kursdeltagelse = kursdeltagelse;
	}

	public String getStudieprogram() {
		return studieprogram;
	}

	public void setStudieprogram(String studieprogram) {
		this.studieprogram = studieprogram;
	}

	public ArrayList<Kurs> getKursdeltagelse() {
		return kursdeltagelse;		
	}
	
	public String toString() {
		return super.toString() + ", studieprogram: " + studieprogram;
	}

	//Oppgave 1 d:
	public void nyttKurs(Kurs kurset) {
		kursdeltagelse.add(kurset);
	}	

}
