import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

public class Kontroll {
	private ArrayList<Kurs> kursliste = new ArrayList<Kurs>();
	private LinkedList<Person> personliste = new LinkedList<>();
	
	public Kontroll() {
		nyPerson(new Student(123456789, "Ole", "Vei 1", "BIT"));
		nyPerson(new Student(234567891, "Nasse", "Vei 2", "�OL"));
		Kurs kurs1 = new Kurs("OBJ2000", "Objektorientert programmering 1", 7.5);
		nyttKurs(kurs1);
		Kurs kurs2 = new Kurs("OBJ2100", "Objektorientert programmering 2", 7.5);
		nyttKurs(kurs2);
		regKursP�Person(kurs1, 123456789);
		regKursP�Person(kurs2, 123456789);
	}
	
	//Oppgave 2a:
	public void nyPerson(Person personen) {
		personliste.add(personen);
	}
	
	public void nyttKurs(Kurs kurset) {
		kursliste.add(kurset);
	}
	
	//Oppgave 2b:
	public Person finnPerson(long personnummer) {
		Person let = new Person(personnummer, null, null);
		for(int i = 0; i < personliste.size(); i++) {
			Person enperson = personliste.get(i);
			if (enperson.equals(let)) return enperson;
		}
		return null;
	}
	
	//Oppgave 2c:
	public Kurs finnKursBin�rt(String kurskode) {
		Kurs let = new Kurs(kurskode, null, 0);
		Collections.sort(kursliste);
		int indeks = Collections.binarySearch(kursliste, let);
		if(indeks >= 0) return kursliste.get(indeks);
		else return null;
	}
	
	//Oppgave 2d:
	public LinkedList<Person> getPersoner() {
		return personliste;
	}
	
	//Oppgave 2e:
	public void regKursP�Person(Kurs kurset, long personnummer) {
		Student studenten = (Student)finnPerson(personnummer);
		if(studenten != null) studenten.nyttKurs(kurset);
	}

	//UTVIDELSE HJEMMELEKSE TIL 18.01.2023
	public ArrayList<Kurs> getKursliste() {
		return kursliste;
	}

	public String returnerKurs() {
		String utskrift ="";
		Iterator<Kurs> kurser = Kurs.getKursliste();
		while(kurser.hasNext()) {
			Kurs kurs = kurser.next();
			utskrift+=kurs.toString() + "\n";
		}
		return utskrift;
	}

	//TROND SIN LØSNING:
	public Iterator<Person> getPersoner() {
		return (Iterator)personliste.linkedIterator();
	}

}
